# LaTeX for Beginners

**Website:** <https://ningzhanglab.github.io/LaTeX-for-Beginners/>

**A beginner-friendly LaTeX handbook, command reference, and template collection** for students, researchers, and academic writers. You can start without Git or programming experience.

## Start here

1. **Choose how to write LaTeX.** [Overleaf](https://www.overleaf.com/) is simplest if you want to begin in a browser. For local editing, use VS Code + LaTeX Workshop + a TeX distribution. LyX is an option if you prefer visual editing. See the [setup guide](SETUP_GUIDE.md).
2. **Test your installation.** Open [LaTeX_Installation_Test.tex](00_Start_Here/LaTeX_Installation_Test.tex) and compile it, or compare with the [reference PDF](00_Start_Here/LaTeX_Installation_Test.pdf).
3. **Read the beginner handbook.** [Open PDF](01_LaTeX_Handbooks/LaTeX_Beginner_Handbook.pdf) · [Editable TeX source](01_LaTeX_Handbooks/LaTeX_Beginner_Handbook.tex).
4. **Keep a quick reference nearby.** [Paper-Writing Cheat Sheet](02_LaTeX_Cheat_Sheets/LaTeX_Paper_Writing_Cheat_Sheet.pdf).
5. **Copy a working template.** Select one below, copy its `.tex` file to your own project, edit it, and compile.

## Contents

| Section | Files | Best use |
|---|---|---|
| [Start Here](00_Start_Here/) | Installation test in `.tex` and `.pdf` | Confirm your editor/compiler works |
| [Handbooks](01_LaTeX_Handbooks/) | Beginner handbook; preamble and setup guide | Learn LaTeX concepts and configure documents |
| [Cheat Sheets](02_LaTeX_Cheat_Sheets/) | Paper-writing quick reference | Look up frequently used commands |
| [Templates](03_LaTeX_Templates/) | Minimal; homework; research paper; Beamer slides | Begin from an editable example |

### Ready-to-use templates

| Template | Editable source | Compiled preview |
|---|---|---|
| Minimal | [`.tex`](03_LaTeX_Templates/LaTeX_Template_01_Minimal.tex) | [PDF](03_LaTeX_Templates/LaTeX_Template_01_Minimal.pdf) |
| Homework / problem set | [`.tex`](03_LaTeX_Templates/LaTeX_Template_02_Homework.tex) | [PDF](03_LaTeX_Templates/LaTeX_Template_02_Homework.pdf) |
| Research paper | [`.tex`](03_LaTeX_Templates/LaTeX_Template_03_Paper.tex) | [PDF](03_LaTeX_Templates/LaTeX_Template_03_Paper.pdf) |
| Presentation / slides | [`.tex`](03_LaTeX_Templates/LaTeX_Template_04_Slide.tex) | [PDF](03_LaTeX_Templates/LaTeX_Template_04_Slide.pdf) |

## Which file should I use?

- **`.pdf`** — read the finished material.
- **`.tex`** — edit the LaTeX source, then compile to PDF.
- **`.bib`** — bibliography data; the research-paper template ships with `references.bib`.

You do not need to install Git. Use **Code → Download ZIP** on GitHub if you only want the teaching materials.

## Setup options

| Route | Best for |
|---|---|
| [Overleaf](https://www.overleaf.com/) | Fastest start; no local LaTeX installation |
| VS Code + LaTeX Workshop + TinyTeX | Local writing and version-controlled research |
| LyX + a TeX distribution | Visual editing and structured documents |
| RStudio / Quarto + TinyTeX | Reproducible reports with code and equations |

Read [SETUP_GUIDE.md](SETUP_GUIDE.md) for installation, compiler tests, missing packages, and troubleshooting.

## Run the website locally

The site is built with [MkDocs Material](https://squidfunk.github.io/mkdocs-material/). You need Python and `pdftoppm` (from poppler).

```bash
pip install -r requirements.txt
python3 scripts/prepare_site.py   # copies PDFs/.tex, builds thumbnails and the Learn page
mkdocs serve                      # http://127.0.0.1:8000
```

Hand-written pages live in `docs/`. Edit the `.tex` sources, recompile the PDFs, and re-run `prepare_site.py`.

## License

Copyright (c) 2026 Ning Zhang. Everything in this repository is licensed under [CC BY 4.0](LICENSE). You may copy, adapt, and share it, including commercially, as long as you give credit and note any changes. What you write using the templates belongs to you.

Suggested credit: *Ning Zhang, "LaTeX for Beginners", https://github.com/ningzhanglab/LaTeX-for-Beginners (CC BY 4.0).*

## Companion collection

For notes, GitHub README files, and research logs, see [Markdown for Beginners](https://github.com/ningzhanglab/Markdown-for-Beginners). Markdown is usually more convenient for lightweight documentation; LaTeX is better for typeset academic documents.

## Source and maintenance

This collection was separated from the original combined [Writing Toolkit](https://github.com/ningzhanglab/For-beginner-Latex-Markdown-and-more). Existing tutorial source files and compiled PDF previews are preserved. A PDF in this repository is a reading copy; make changes to the editable source when revising a template.

Do not put restricted data, confidential drafts, or credentials in a public repository.
