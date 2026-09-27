# LaTeX Setup Guide for Non-Technical Beginners

This guide is intentionally written for someone who has never configured a LaTeX environment before.

> Looking for Markdown instead? Markdown usually needs no compiler. See [`04_Markdown_Handbooks/Markdown_Setup_and_Editors_Guide.md`](04_Markdown_Handbooks/Markdown_Setup_and_Editors_Guide.md) for VS Code, GitHub, HackMD, StackEdit, Jupyter/Colab, and Quarto workflows.

If you only want to start writing immediately, use **Overleaf**. If you want a local workflow, use **VS Code + LaTeX Workshop + TinyTeX**.

---

## 1. Understand the pieces first

A local LaTeX workflow has several separate parts:

```text
Your .tex file
      ↓
Editor: VS Code
      ↓
VS Code helper: LaTeX Workshop
      ↓
Compiler/distribution: TinyTeX
      ↓
Your .pdf file
```

Installing VS Code alone is not enough. Installing TinyTeX alone does not give you a pleasant editor. They do different jobs.

---

## 2. Route A: Overleaf — no local setup

Use this route if:

- you are brand new to LaTeX;
- you use a managed university computer;
- you do not want to troubleshoot software installation;
- you mainly collaborate with coauthors online.

### Steps

1. Go to <https://www.overleaf.com/>.
2. Create an account.
3. Download this repository as a ZIP from GitHub.
4. In Overleaf, choose **New Project → Upload Project**.
5. Upload a LaTeX project ZIP, or upload one `.tex` template to a blank project.
6. Click **Recompile**.

Try the homework template first.

### Advantage

There is no local TeX installation to maintain.

### Limitation

Your source files live in an online project. For sensitive research files, follow your institution's data-security rules and do not upload restricted data.

---

## 3. Route B: LyX — visual LaTeX editing

Use this route if:

- you want LaTeX-quality output but prefer a visual editor;
- you would rather insert equations, sections, figures, and citations through menus;
- you are writing a dissertation or long technical document;
- you do not want to memorize many LaTeX commands at the beginning.

LyX is a structured document editor built on top of LaTeX. It is not a normal word processor: you still work with document structure such as sections, equations, figures, references, and theorem environments, but LyX hides much of the raw LaTeX syntax.

### Step 1: install a TeX distribution first

LyX needs a working LaTeX installation to produce PDF output. The LyX project recommends installing the TeX system before installing LyX so it can detect it during setup.

Typical beginner combinations are:

| Operating system | Recommended TeX system for LyX |
|---|---|
| Windows | TeX Live or MiKTeX |
| macOS | MacTeX |
| Linux | TeX Live from your distribution/package manager |

Official LyX download page:

<https://www.lyx.org/Download>

Official LyX documentation:

<https://www.lyx.org/Documentation>

### Step 2: install LyX

Download the installer for your operating system and install it after the TeX distribution.

### Step 3: run the built-in tutorial

Open LyX and use the **Help** menu. LyX includes an **Introduction**, **Tutorial**, and **User Guide**. These are especially useful for beginners because they demonstrate LyX using LyX itself.

### Step 4: test PDF output

1. Create a new LyX document.
2. Type one sentence.
3. Insert a displayed equation.
4. Preview/export the document as PDF.
5. If the PDF is created, the basic setup works.

### Can LyX use TinyTeX?

TinyTeX is based on TeX Live, so experienced users can often configure LyX to use an existing TinyTeX installation. However, for a complete beginner, the standard LyX-documented combinations above are usually easier because LyX expects to discover a conventional TeX installation automatically.

If you already have TinyTeX working, you do not necessarily need to replace it. If LyX cannot find it, consult the LyX configuration documentation rather than installing multiple TeX systems blindly.

### LyX or VS Code?

Choose **LyX** if you want a visual, structured writing experience. Choose **VS Code** if you want to learn and control the actual `.tex` source. Both ultimately rely on LaTeX to create the PDF.

---

## 4. Route C: VS Code + LaTeX Workshop + TinyTeX

### Step 1: Install VS Code

Download VS Code from:

<https://code.visualstudio.com/>

Install it normally and open it once.

### Step 2: Install LaTeX Workshop

In VS Code:

1. open **Extensions**;
2. search **LaTeX Workshop**;
3. choose the extension by James Yu;
4. click **Install**.

Official page:

<https://marketplace.visualstudio.com/items?itemName=James-Yu.latex-workshop>

LaTeX Workshop provides build commands, syntax support, log viewing, and an integrated PDF viewer. It still needs a LaTeX distribution installed on your computer.

---

## 5. Install TinyTeX

TinyTeX is a lightweight distribution based on TeX Live.

Official documentation:

<https://yihui.org/tinytex/>

### Route 1: install through R — easiest for many beginners

If you already use R/RStudio, open the R console and run:

```r
install.packages("tinytex")
tinytex::install_tinytex(bundle = "TinyTeX")
```

Then restart R/RStudio and VS Code.

The capitalization matters conceptually:

- `tinytex` = the R package;
- `TinyTeX` = the LaTeX distribution.

The larger `TinyTeX` bundle contains more packages than the minimal default bundle, which is useful for beginners who would rather avoid frequent missing-package messages.

### Route 2: macOS without R

Open **Terminal** and run:

```bash
curl -sL "https://tinytex.yihui.org/install-bin-unix.sh" | sh
```

When it finishes:

1. quit Terminal;
2. quit VS Code;
3. reopen them.

### Route 3: Linux without R

Open a terminal and run:

```bash
wget -qO- "https://tinytex.yihui.org/install-bin-unix.sh" | sh
```

Then restart your terminal and VS Code.

### Route 4: Windows without R

For a beginner, installing TinyTeX from R is usually the least confusing route.

If you do not want R, use the official Windows installer instructions on:

<https://yihui.org/tinytex/>

Pre-built releases are also available at:

<https://github.com/rstudio/tinytex-releases>

---

## 6. Verify the installation

Open a **new** terminal window.

Run:

```bash
pdflatex --version
```

Then:

```bash
latexmk --version
```

You do not need to understand the output. You only want to see version information instead of an error saying that the command does not exist.

If the commands are not found, restart your computer once before changing configuration files.

---

## 7. Compile your first file in VS Code

1. Download/unzip this repository.
2. In VS Code choose **File → Open Folder...**.
3. Open the repository folder, not just one isolated `.tex` file.
4. Open:

```text
00_Start_Here/LaTeX_Installation_Test.tex
```

5. Open the Command Palette.
6. run:

```text
LaTeX Workshop: Build LaTeX project
```

7. Open the PDF preview from LaTeX Workshop.

If the test document builds, your basic setup works.

---

## 8. Then test a real research-paper template

Open:

```text
03_LaTeX_Templates/LaTeX_Template_02_Homework.tex
```

Build it.

Then change one sentence and build again.

Next change one equation and build again.

This small-cycle workflow is much easier to debug than editing ten pages before compiling.

---

## 9. Missing LaTeX packages

A package error often looks like:

```text
LaTeX Error: File `booktabs.sty' not found.
```

The source file may be perfectly fine. Your local TeX installation is simply missing the package.

With TinyTeX/TeX Live, install a package with:

```bash
tlmgr install booktabs
```

If you use R:

```r
tinytex::tlmgr_install("booktabs")
```

If you do not know which package contains a missing `.sty` file, search TeX Live:

```bash
tlmgr search --global --file "/booktabs.sty"
```

Do not remove useful LaTeX code simply to silence a missing-package error.

---

## 10. TinyTeX maintenance

You usually do not need to maintain TinyTeX frequently.

For R users:

```r
tinytex::tlmgr_update()
```

If a TeX Live year transition causes repository-version problems, the TinyTeX documentation may recommend reinstalling:

```r
tinytex::reinstall_tinytex()
```

Do not reinstall LaTeX as your first response to every compilation error. Most errors are source-code errors, missing packages, or path problems.

---

## 11. If VS Code cannot find TinyTeX

Symptom:

```text
spawn latexmk ENOENT
```

or the terminal says:

```text
latexmk: command not found
```

Try in this order:

1. restart VS Code;
2. open a new terminal;
3. restart your computer;
4. check `pdflatex --version`;
5. check `latexmk --version`;
6. confirm TinyTeX is installed;
7. consult TinyTeX PATH documentation.

If TinyTeX was installed from R, you can check its location with:

```r
tinytex::tinytex_root()
```

You can also ask TinyTeX to re-register itself:

```r
tinytex::use_tinytex()
```

Then restart VS Code.

---

## 12. Should I install MacTeX/TeX Live/MiKTeX instead?

You can. TinyTeX is not mandatory.

### TinyTeX

Good if you want:

- a smaller installation;
- cross-platform behavior;
- integration with R/R Markdown/Quarto;
- a TeX Live-based system.

### MacTeX

Good if you are on macOS and prefer a traditional comprehensive installation with many packages already included.

### TeX Live

Good if you want the standard full TeX ecosystem and disk size is not a concern.

### MiKTeX

Common on Windows and can automatically install missing packages.

For this repository, any normal modern LaTeX distribution should work. TinyTeX is recommended because it is relatively lightweight and works especially well for researchers who already use R or Quarto.

---

## 13. VS Code quality-of-life setup

For beginners, **do not copy a huge `settings.json` from the internet**.

Start with LaTeX Workshop defaults. Change settings only when you understand why.

Useful features to learn gradually:

- Build LaTeX project;
- View LaTeX PDF;
- SyncTeX: jump between source and PDF;
- autocomplete for `\ref`, `\cite`, and commands;
- error/warning navigation;
- recipe selection when you later need XeLaTeX/LuaLaTeX.

For the templates in this repository, a standard `latexmk`/pdfLaTeX workflow is a good default unless the document explicitly says otherwise.

---

## 14. RStudio + TinyTeX

If you already use RStudio, you may not need VS Code immediately.

TinyTeX works especially well with:

- R Markdown;
- Quarto;
- PDF reports;
- automatically generated regression tables and figures.

Install:

```r
install.packages("tinytex")
tinytex::install_tinytex(bundle = "TinyTeX")
```

You can later use VS Code for the paper source while continuing to run R code in RStudio.

A very common research workflow is:

```text
R/Stata/Python → generate tables/figures → LaTeX paper imports them
```

---

## 15. GitHub is optional at first

Do not try to learn LaTeX, Git, GitHub, VS Code, R, and the terminal on the same day.

### Beginner level

Download the repository as ZIP.

### Next level

Use GitHub Desktop.

### Later

Learn Git commands such as `clone`, `pull`, `commit`, and `push` if your research workflow benefits from them.

---

## 16. Public-repository safety

Never commit secrets or restricted research materials.

Before pushing to GitHub, check for:

- raw restricted data;
- student or participant identifiers;
- API tokens;
- passwords;
- private SSH keys;
- proprietary datasets;
- referee reports;
- confidential coauthor drafts.

Use `.gitignore`, but do not rely on it blindly. Once sensitive material is committed and pushed, deleting the visible file may not remove it from Git history.

---

## 17. Setup decision tree

```text
Do you want zero installation?
│
├── Yes → Use Overleaf.
│
└── No
    │
    ├── Do you prefer a visual editor and want to avoid raw LaTeX source?
    │   │
    │   └── Yes → Install a TeX distribution, then install LyX.
    │
    ├── Do you already use R/RStudio or Quarto?
    │   │
    │   ├── Yes → Install TinyTeX from R.
    │   │          Use RStudio/Quarto and/or VS Code.
    │   │
    │   └── No → Install VS Code + LaTeX Workshop.
    │              Install TinyTeX using the standalone instructions.
    │
    └── If local setup becomes frustrating → use Overleaf first and return later.
```

---

## 18. Five-minute sanity checklist

Before debugging your document, confirm:

- [ ] the file ends in `.tex`;
- [ ] you opened the correct project folder;
- [ ] `pdflatex --version` works locally;
- [ ] `latexmk --version` works locally;
- [ ] LaTeX Workshop is installed;
- [ ] you are building the intended root `.tex` file;
- [ ] image paths are relative and correct;
- [ ] bibliography files exist if cited;
- [ ] the first real error in the log is identified;
- [ ] you tried the minimal installation-test file.

---

## Official setup links

- LyX: <https://www.lyx.org/>
- LyX download: <https://www.lyx.org/Download>
- LyX documentation: <https://www.lyx.org/Documentation>

- Overleaf: <https://www.overleaf.com/>
- Overleaf Learn: <https://www.overleaf.com/learn>
- VS Code: <https://code.visualstudio.com/>
- LaTeX Workshop: <https://marketplace.visualstudio.com/items?itemName=James-Yu.latex-workshop>
- TinyTeX: <https://yihui.org/tinytex/>
- TinyTeX releases: <https://github.com/rstudio/tinytex-releases>

