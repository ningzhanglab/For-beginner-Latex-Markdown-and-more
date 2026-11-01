#!/usr/bin/env python3
"""Prepare generated inputs for the MkDocs site.

Run from the repository root:  python3 scripts/prepare_site.py
Creates (all git-ignored):
  docs/files/...          copies of every .tex / .pdf / .bib / figure
  docs/files/templates/   one .zip per template (for Overleaf and download)
  docs/assets/thumbs/     first-page PNG thumbnails of the template PDFs
  docs/setup.md           SETUP_GUIDE.md rewritten for the site
  docs/learn.md           table of contents extracted from the handbook source
"""
import re
import shutil
import subprocess
import zipfile
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
DOCS = ROOT / "docs"
FILES = DOCS / "files"
THUMBS = DOCS / "assets" / "thumbs"
SOURCE_DIRS = [
    "00_Start_Here",
    "01_LaTeX_Handbooks",
    "02_LaTeX_Cheat_Sheets",
    "03_LaTeX_Templates",
]

# template name -> (main tex, extra files that must travel with it)
TEMPLATES = {
    "minimal": ("LaTeX_Template_01_Minimal", []),
    "homework": ("LaTeX_Template_02_Homework", []),
    "paper": ("LaTeX_Template_03_Paper", ["references.bib", "figures/example_figure.pdf"]),
    "slides": ("LaTeX_Template_04_Slide", []),
}


def copy_sources():
    if FILES.exists():
        shutil.rmtree(FILES)
    for d in SOURCE_DIRS:
        src = ROOT / d
        for f in src.rglob("*"):
            if f.is_file() and f.suffix in {".tex", ".pdf", ".bib"}:
                dest = FILES / d / f.relative_to(src)
                dest.parent.mkdir(parents=True, exist_ok=True)
                shutil.copy2(f, dest)


def make_zips():
    out = FILES / "templates"
    out.mkdir(parents=True, exist_ok=True)
    tdir = ROOT / "03_LaTeX_Templates"
    for key, (stem, extras) in TEMPLATES.items():
        with zipfile.ZipFile(out / f"{key}.zip", "w", zipfile.ZIP_DEFLATED) as z:
            z.write(tdir / f"{stem}.tex", "main.tex")
            for e in extras:
                z.write(tdir / e, e)


def make_thumbs():
    THUMBS.mkdir(parents=True, exist_ok=True)
    tdir = ROOT / "03_LaTeX_Templates"
    for key, (stem, _) in TEMPLATES.items():
        subprocess.run(
            ["pdftoppm", "-png", "-r", "70", "-f", "1", "-l", "1", "-singlefile",
             str(tdir / f"{stem}.pdf"), str(THUMBS / key)],
            check=True,
        )


def make_setup():
    text = (ROOT / "SETUP_GUIDE.md").read_text()
    # The site gives the page its own title; drop the first H1 and the Markdown-for-Beginners aside is kept.
    text = re.sub(r"\A# .*\n", "", text, count=1)
    text = text.replace("Download this repository as a ZIP from GitHub.",
                        "Download a template from the [Templates](templates.md) page (each one has an *Open in Overleaf* button).")
    (DOCS / "setup.md").write_text("# Setup Guide\n" + text)


def clean_tex(s: str) -> str:
    s = re.sub(r"\\(?:texttt|code|textbf|emph|textit)\{([^{}]*)\}", r"\1", s)
    s = s.replace("``", "\u201c").replace("''", "\u201d").replace("\\&", "&").replace("\\_", "_")
    s = s.replace("\\textbackslash ", "\\").replace("\\textbackslash", "\\").replace("\\\\", " ")
    s = re.sub(r"\\[a-zA-Z]+\*?", "", s)
    return re.sub(r"[{}]", "", s).strip()


def make_learn():
    tex = (ROOT / "01_LaTeX_Handbooks" / "LaTeX_Beginner_Handbook.tex").read_text().splitlines()
    parts, in_code = [], False
    for line in tex:
        if re.match(r"\\begin\{(lstlisting|verbatim)\}", line):
            in_code = True
            continue
        if re.match(r"\\end\{(lstlisting|verbatim)\}", line):
            in_code = False
            continue
        if in_code:
            continue
        m = re.match(r"\\part\{(.*)\}\s*$", line)
        if m:
            parts.append((clean_tex(m.group(1)), []))
            continue
        m = re.match(r"\\section\*?\{(.*)\}\s*$", line)
        if m and parts:
            parts[-1][1].append(clean_tex(m.group(1)))
    n_sections = sum(len(s) for _, s in parts)
    out = [
        "# Learn LaTeX\n",
        "The **Beginner Handbook** teaches LaTeX from zero. Most examples show the source "
        "code and the compiled result side by side.\n",
        '<div class="actions" markdown>\n'
        '[:material-file-pdf-box: Read the handbook (PDF)](files/01_LaTeX_Handbooks/LaTeX_Beginner_Handbook.pdf){ .md-button .md-button--primary }\n'
        '[:material-file-code: Preamble & setup guide (PDF)](files/01_LaTeX_Handbooks/LaTeX_Preamble_and_Setup_Guide.pdf){ .md-button }\n'
        "</div>\n",
        f"The handbook has **{len(parts)} parts** and **{n_sections} short sections**. Use the list below "
        "to see what each part covers, then search the PDF (Ctrl/Cmd+F) for the section name.\n",
    ]
    for i, (title, secs) in enumerate(parts, 1):
        out.append(f'??? note "Part {i}. {title}"\n')
        for s in secs:
            out.append(f"    - {s}")
        out.append("")
    (DOCS / "learn.md").write_text("\n".join(out) + "\n")


if __name__ == "__main__":
    copy_sources()
    make_zips()
    make_thumbs()
    make_setup()
    make_learn()
    print("site inputs ready")
