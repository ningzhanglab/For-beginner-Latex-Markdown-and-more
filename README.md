# Writing Toolkit

A beginner-friendly collection of **LaTeX and Markdown handbooks, cheat sheets, and templates for graduate students, researchers, and academic writers**.

This repository is written for students who may have **little or no technical background**. You do not need to know programming, Git, GitHub, terminals, or LaTeX before you start.

Economics and quantitative social-science examples appear in some materials because they are useful for showing equations, tables, figures, citations, and research-paper structure. The toolkit itself is intended for **students and researchers across disciplines**.

> **If this is your first time on GitHub:** click the green **`<> Code`** button, choose **Download ZIP**, unzip the folder, and start by opening the PDFs. You do not need Git to use this repository.

---

# 1. First decision: where do you want to write LaTeX?

LaTeX is a document typesetting system. You normally write a `.tex` source file and a LaTeX compiler turns it into a PDF.

You have several ways to work with it. You only need **one**.

| What you want | Recommended route | Setup | What it feels like | Good for |
|---|---|---:|---|---|
| **“I just want LaTeX to work.”** | **Overleaf** | Very easy | Write LaTeX in a browser and see the PDF beside it | First-time users, coursework, collaboration |
| **“I prefer a visual editor.”** | **LyX** | Easy–medium | Use menus for sections, equations, figures, and citations | Students who do not want to type much raw LaTeX |
| **“I want to learn real LaTeX and work locally.”** | **VS Code + LaTeX Workshop + TinyTeX** | Medium | Edit `.tex` source directly on your computer | Long-term research writing, offline work, GitHub projects |
| **“I already use R or Quarto.”** | **RStudio / Positron / Quarto + TinyTeX** | Medium | Combine prose, code, tables, figures, and PDF output | Reproducible and data-heavy research |

A simple decision rule:

```text
Never used LaTeX?
    |
    +-- Want zero installation? ----------> Overleaf
    |
    +-- Prefer a visual editor? ----------> LyX
    |
    +-- Want to learn LaTeX source? ------> VS Code + TinyTeX
    |
    +-- Already use R / Quarto? ----------> RStudio / Positron + TinyTeX
```

**If you are unsure, start with Overleaf.** The LaTeX syntax you learn there can be moved to another editor later.

For more detailed troubleshooting, see [`SETUP_GUIDE.md`](SETUP_GUIDE.md).

---

# 2. Route A — Overleaf: easiest setup

[Overleaf](https://www.overleaf.com/) is an online LaTeX editor that runs in a browser.

You do **not** need to install:

- LaTeX;
- TinyTeX;
- VS Code;
- a compiler;
- Git.

## Quick start

1. Create an Overleaf account.
2. Download this repository as a ZIP, or download one `.tex` template.
3. In Overleaf choose **New Project → Upload Project**.
4. Upload the ZIP or create a blank project and add the `.tex` file.
5. Open the main `.tex` file.
6. Click **Recompile**.
7. Change one sentence and compile again.

A good first file is:

```text
03_LaTeX_Templates/LaTeX_Template_02_Homework.tex
```

### Why choose Overleaf?

- almost no setup;
- source and PDF appear side by side;
- easy collaboration;
- useful university and journal templates;
- good for learning by editing a working example.

### One caution

Do not upload restricted or confidential research data unless your institution and data-use agreement permit it.

---

# 3. Route B — LyX: visual LaTeX writing

[LyX](https://www.lyx.org/) is a visual, structured document editor built around LaTeX.

Instead of typing every command yourself, you can insert many things through menus:

- sections;
- equations;
- figures;
- tables;
- citations;
- theorem-like environments.

Think of it as:

```text
visual/structured editing
        +
LaTeX-quality typesetting
```

LyX is **not exactly Microsoft Word**. It still encourages you to describe the structure of a document rather than manually positioning every object.

## Basic setup

LyX needs a TeX/LaTeX distribution to create PDFs. For beginners, a conventional setup is usually easiest:

| Operating system | Typical setup |
|---|---|
| Windows | TeX Live or MiKTeX → then LyX |
| macOS | MacTeX → then LyX |
| Linux | TeX Live → then LyX |

Then:

1. install the TeX distribution;
2. install LyX;
3. open LyX;
4. use **Help → Tutorial** or the built-in Introduction/User Guide;
5. create a short document;
6. insert one displayed equation;
7. preview/export it as PDF.

### Choose LyX if

- raw `.tex` code feels intimidating;
- you write many equations;
- you prefer menus and a visual document structure;
- you are writing a long thesis/dissertation.

### Limitation

Highly customized journal templates or unusual packages may eventually require some direct LaTeX knowledge.

---

# 4. Route C — VS Code + LaTeX Workshop + TinyTeX

This is the recommended local route if you want to learn normal LaTeX source and keep your projects on your computer.

The most important beginner idea is that these are **three different pieces**:

```text
VS Code          = editor
LaTeX Workshop   = VS Code helper/extension
TinyTeX          = LaTeX distribution/compiler
```

The workflow is:

```text
.tex source
    ↓
VS Code
    ↓
LaTeX Workshop
    ↓
TinyTeX / latexmk / pdflatex
    ↓
.pdf output
```

Installing VS Code alone does **not** install LaTeX.

## Step 1 — Install VS Code

Download and install:

<https://code.visualstudio.com/>

## Step 2 — Install LaTeX Workshop

In VS Code:

1. open **Extensions**;
2. search for **LaTeX Workshop**;
3. choose the extension by James Yu;
4. click **Install**.

LaTeX Workshop gives VS Code build commands, LaTeX syntax support, logs, and a PDF viewer. It still needs a LaTeX distribution.

## Step 3 — Install TinyTeX

TinyTeX is a lightweight TeX Live-based LaTeX distribution.

Official documentation:

<https://yihui.org/tinytex/>

### If you already use R / RStudio

Open the R console and run:

```r
install.packages("tinytex")
tinytex::install_tinytex(bundle = "TinyTeX")
```

Then restart R/RStudio and VS Code.

A useful distinction:

```text
tinytex   = R package
TinyTeX   = LaTeX distribution
```

### macOS without R

Open Terminal and run:

```bash
curl -sL "https://tinytex.yihui.org/install-bin-unix.sh" | sh
```

Then quit and reopen Terminal and VS Code.

### Linux without R

```bash
wget -qO- "https://tinytex.yihui.org/install-bin-unix.sh" | sh
```

Then restart the terminal and VS Code.

### Windows without R

For a complete beginner, the R installation route above is often the simplest. Otherwise follow the Windows instructions in the official TinyTeX documentation.

## Step 4 — Check that LaTeX is installed

Open a **new** terminal and run:

```bash
pdflatex --version
latexmk --version
```

You do not need to understand the output. You just want version information instead of “command not found.”

## Step 5 — Test this repository

In VS Code:

1. choose **File → Open Folder...**;
2. open the whole repository folder;
3. open:

```text
00_Start_Here/LaTeX_Installation_Test.tex
```

4. open the Command Palette;
5. run:

```text
LaTeX Workshop: Build LaTeX project
```

6. open the PDF preview.

If the PDF appears, your basic setup works.

## If a package is missing

You may see an error like:

```text
LaTeX Error: File `booktabs.sty' not found.
```

With TinyTeX / TeX Live, install the package with:

```bash
tlmgr install booktabs
```

or from R:

```r
tinytex::tlmgr_install("booktabs")
```

More troubleshooting is in [`SETUP_GUIDE.md`](SETUP_GUIDE.md).

---

# 5. Route D — RStudio / Positron / Quarto + TinyTeX

Use this route if your research already combines writing with R, Python, Julia, tables, and figures.

Install TinyTeX from R:

```r
install.packages("tinytex")
tinytex::install_tinytex(bundle = "TinyTeX")
```

This route is especially useful when you want one reproducible workflow containing:

- prose;
- equations;
- code;
- automatically generated tables;
- automatically generated figures;
- citations;
- PDF / HTML / Word output.

You do **not** need Quarto to learn LaTeX. It is simply another workflow that becomes useful for reproducible research.

---

# 6. What should I open after LaTeX is working?

If you are completely new, use this order:

```text
00_Start_Here/LaTeX_Installation_Test.tex
        ↓
01_LaTeX_Handbooks/LaTeX_Beginner_Handbook.pdf
        ↓
02_LaTeX_Cheat_Sheets/LaTeX_Paper_Writing_Cheat_Sheet.pdf
        ↓
03_LaTeX_Templates/
```

Do **not** try to memorize the handbook.

Use it to understand LaTeX once, then keep the cheat sheet nearby while writing.

---

# 7. LaTeX section of this repository

## 01 — LaTeX Handbooks

### `LaTeX_Beginner_Handbook`

A detailed beginner handbook with source examples and compiled output.

Use it when you need to understand:

- what commands and environments are;
- normal text and document structure;
- equations;
- tables and figures;
- citations and references;
- spacing/alignment commands such as `\quad` and `\qquad`;
- reserved characters;
- common errors;
- research-paper patterns.

### `LaTeX_Preamble_and_Setup_Guide`

A focused guide to the material before `\begin{document}`:

- document classes;
- packages;
- margins;
- fonts;
- bibliography packages;
- table/figure packages;
- theorem environments;
- useful custom commands;
- copy-ready preambles.

## 02 — LaTeX Cheat Sheets

### `LaTeX_Paper_Writing_Cheat_Sheet`

A compact lookup reference for commands you repeatedly need while writing.

Use the cheat sheet when you know roughly what you want but cannot remember the syntax.

## 03 — LaTeX Templates

| Template | Use it for |
|---|---|
| `LaTeX_Template_01_Minimal.tex` | Smallest possible starting point |
| `LaTeX_Template_02_Homework.tex` | Homework / problem sets / coursework |
| `LaTeX_Template_03_Paper.tex` | Research paper draft |

Copy a template, rename it, and edit the copy.

---

# 8. Markdown: the simpler companion tool

Markdown is much lighter than LaTeX. A Markdown file is plain text ending in `.md`.

You can use Markdown for:

- AI prompt

- research notes and daily logs;
- paper-reading notes;
- seminar and meeting notes;
- project `README.md` files;
- replication instructions;
- simple documentation;
- notes beside R / Python / Julia code;
- lightweight drafts and outlines.

A very small Markdown file might look like this:

```markdown
# Research Notes

**Main finding:** The result is stable.

## Tasks

- Read the paper
- Check Table 2
- [ ] Write a short summary
```

Unlike LaTeX, basic Markdown usually does **not** need a compiler. You type plain text, save the file, and open a preview.

## Where can I write Markdown?

You do not need one special Markdown program. The same `.md` file can usually move between different editors and websites. You even can write in `.txt` then change the extension to `.md`.

| What you want | Good choice | Installation? | Best for |
|---|---|---:|---|
| **“I already use VS Code.”** | **VS Code** | VS Code only | Local notes, research folders, GitHub projects |
| **“I want a simple visual Markdown editor.”** | **Typora (Paid) / Moeka (Free)** | Yes | Distraction-free local writing, live preview |
| **“I only want to edit a README online.”** | **GitHub web editor** | No | Repository documentation |
| **“I want several people to edit the same note.”** | **HackMD** | No | Meetings, shared notes, collaborative outlines |
| **“I want a browser editor with live preview.”** | **StackEdit** | No | Learning Markdown and quick browser writing |
| **“I want a personal research-note system.”** | **Obsidian** | Yes | Connected notes, literature notes, personal knowledge base |
| **“My writing sits next to Python/R code.”** | **Jupyter / Google Colab** | Depends | Computational notebooks and data analysis |
| **“I want citations, code, and PDF/HTML/Word output.”** | **Quarto** | Yes | Reproducible academic documents |

### A simple beginner rule

```text
Want normal local notes? ------------> VS Code
Want a visual writing experience? ---> Typora or another live-preview editor
Want to edit README.md online? ------> GitHub
Want shared collaborative notes? ----> HackMD
Want a browser-only editor? ---------> StackEdit
Want a personal note library? -------> Obsidian
Want notes beside code? -------------> Jupyter / Colab
Want a reproducible report? ---------> Quarto
```

If you are unsure, **start with VS Code** if you already installed it for LaTeX. If you want zero setup, try **GitHub's web editor** for repository files or **HackMD / StackEdit** for browser-based notes.

## Markdown in VS Code

VS Code has basic Markdown support built in. You do **not** need a Markdown extension to begin.

1. Create a new text file.
2. Save it with a `.md` ending, for example:

```text
research_notes.md
```

3. Type some Markdown.
4. Open the preview.

### Preview shortcuts

macOS:

```text
Shift + Command + V      open preview
Command + K, then V      preview beside the source
```

Windows / Linux:

```text
Ctrl + Shift + V         open preview
Ctrl + K, then V         preview beside the source
```

A useful beginner layout is:

```text
left side                      right side
Markdown source                rendered preview

# Results                     Results
**Finding:** ...              Finding: ...
```

This side-by-side view makes Markdown easy to learn because you can immediately see what each symbol does.

## Markdown directly on GitHub

GitHub automatically renders `README.md` and other Markdown files.

You can edit a Markdown file without using Git or a terminal:

1. open the file on GitHub;
2. click the edit/pencil button;
3. change the Markdown text;
4. switch to the preview if available;
5. commit/save the change.

Good uses include:

- repository introductions;
- installation instructions;
- replication instructions;
- folder explanations;
- public teaching material.

## HackMD: shared notes in a browser

HackMD is useful when several people need to edit the same Markdown document.

Typical uses:

- coauthor meeting notes;
- seminar notes;
- reading-group notes;
- project outlines;
- shared task lists.

Because it is browser-based, it can feel closer to a collaborative document editor than a local text editor.

## StackEdit: simple browser Markdown practice

StackEdit is useful when you want to practice Markdown or write a quick note without configuring VS Code.

A simple workflow is:

```text
open StackEdit
      ↓
type Markdown on the left
      ↓
watch the rendered result on the right
```

## Obsidian: personal research notes

Obsidian is useful when you want to keep many Markdown notes and link them together.

For example, you might create separate notes for:

```text
Papers/
Ideas/
Methods/
Meetings/
Projects/
```

This is helpful for a personal literature or research knowledge base. Obsidian adds its own features, but the underlying notes can still be ordinary Markdown files.

## Jupyter / Google Colab: Markdown beside code

Jupyter and Colab notebooks contain both **code cells** and **Markdown cells**.

For example, one Markdown cell might explain a result:

```markdown
## Results

The coefficient is positive in the baseline sample.
```

and the next cell can contain the Python or R code that produced the result.

This is useful when explanation and computation belong together.

## Quarto: Markdown for reproducible academic documents

Quarto is a good next step when ordinary Markdown becomes too limited.

It can combine:

- Markdown-style writing;
- citations;
- equations;
- cross-references;
- R / Python / Julia code;
- automatically generated figures and tables;
- PDF, HTML, and Word output.

Quarto files usually end in `.qmd` rather than `.md`.

You do **not** need Quarto to learn Markdown. Start with ordinary `.md` files first.

## Important: Markdown can look different in different tools

Markdown has a common basic syntax, but different tools support different extra features.

These are very portable:

```markdown
# Heading

**bold**

*italic*

- bullet

1. numbered item

[link](https://example.com)

`inline code`
```

These may depend on the tool:

- mathematical equations;
- footnotes;
- citations;
- special callout boxes;
- collapsible sections;
- advanced cross-references.

So if something works in Quarto or Obsidian but not on GitHub, it does not necessarily mean your Markdown is wrong. The tools may simply use different Markdown features.

For the full editor/setup walkthrough, open:

```text
04_Markdown_Handbooks/Markdown_Setup_and_Editors_Guide.md
```

For syntax, start with:

```text
05_Markdown_Cheat_Sheets/Markdown_Simple_Cheat_Sheet.pdf
```

---

# 9. Markdown learning path

The Markdown folders deliberately mirror the LaTeX folders:

```text
LaTeX
  Handbooks
  Cheat Sheets
  Templates

Markdown
  Handbooks
  Cheat Sheets
  Templates
```

For a beginner:

```text
00_Start_Here/Markdown_First_Note.md
        ↓
05_Markdown_Cheat_Sheets/Markdown_Simple_Cheat_Sheet.pdf
        ↓
04_Markdown_Handbooks/Markdown_Beginner_Handbook.pdf
        ↓
06_Markdown_Templates/
        ↓
05_Markdown_Cheat_Sheets/Markdown_Advanced_Cheat_Sheet.pdf
        only when needed
```

## 04 — Markdown Handbooks

- `Markdown_Beginner_Handbook` — learn Markdown from zero.
- `Markdown_Setup_and_Editors_Guide` — where to write Markdown: VS Code, GitHub, HackMD, StackEdit, Jupyter/Colab, and Quarto.

## 05 — Markdown Cheat Sheets

- `Markdown_Simple_Cheat_Sheet` — headings, bold/italic, lists, links, images, code, one simple table, and basic math.
- `Markdown_Advanced_Cheat_Sheet` — relative paths, heading links, more tables/code/math, footnotes, YAML, citations, and research/GitHub patterns.

## 06 — Markdown Templates

| Template | Use it for |
|---|---|
| `Markdown_Template_01_Minimal_Note.md` | A simple note |
| `Markdown_Template_02_Research_Notes.md` | Research log / reading notes / daily notes |
| `Markdown_Template_03_Project_README.md` | A research-project or GitHub README |

---

# 10. Repository structure

```text
Writing_Toolkit_GitHub/
│
├── README.md
├── SETUP_GUIDE.md
├── .gitignore
│
├── 00_Start_Here/
│   ├── LaTeX_Installation_Test.tex
│   ├── LaTeX_Installation_Test.pdf
│   └── Markdown_First_Note.md
│
├── 01_LaTeX_Handbooks/
│   ├── LaTeX_Beginner_Handbook.*
│   └── LaTeX_Preamble_and_Setup_Guide.*
│
├── 02_LaTeX_Cheat_Sheets/
│   └── LaTeX_Paper_Writing_Cheat_Sheet.*
│
├── 03_LaTeX_Templates/
│   ├── LaTeX_Template_01_Minimal.*
│   ├── LaTeX_Template_02_Homework.*
│   └── LaTeX_Template_03_Paper.*
│
├── 04_Markdown_Handbooks/
│   ├── Markdown_Beginner_Handbook.*
│   └── Markdown_Setup_and_Editors_Guide.*
│
├── 05_Markdown_Cheat_Sheets/
│   ├── Markdown_Simple_Cheat_Sheet.*
│   └── Markdown_Advanced_Cheat_Sheet.*
│
└── 06_Markdown_Templates/
    ├── Markdown_Template_01_Minimal_Note.*
    ├── Markdown_Template_02_Research_Notes.*
    └── Markdown_Template_03_Project_README.*
```

`.*` means both a readable/rendered version and an editable source are included when appropriate.

---

# 11. Which file type should I edit?

| Extension | What it is | What you normally do with it |
|---|---|---|
| `.pdf` | Rendered document | Read it |
| `.tex` | LaTeX source | Edit it, then compile to PDF |
| `.md` | Markdown source | Edit it and preview/render it |
| `.bib` | Bibliography database | Store citation information |
| `.zip` | Folder archive | Download/unzip or upload as a project |

---

# 12. LaTeX or Markdown?

They solve different problems.

## Use LaTeX when

- writing a paper or dissertation;
- equations matter;
- you need precise citations and cross-references;
- you have complex tables/figures;
- a journal or department provides a `.tex` template.

## Use Markdown when

- taking research notes;
- writing a project README;
- keeping a research log;
- documenting code or data;
- drafting quickly;
- writing GitHub documentation.

A common research workflow is:

```text
Markdown  → notes, planning, README, documentation
LaTeX     → formal paper, dissertation, technical manuscript
```

---

# 13. Three beginner rules

1. **Start from a working example.** Do not begin with an empty file unless you want to.
2. **Make one small change and render/compile again.** Small steps are easier to debug.
3. **Do not memorize everything.** Use the handbooks to learn and the cheat sheets to look things up.

---

# 14. Privacy and research data

Do not put restricted data, confidential participant information, private API keys, passwords, or files prohibited by a data-use agreement into a public GitHub repository or an online editor.

Keep sensitive research materials in storage approved by your institution.

---

# 15. Suggested first 15 minutes

If you want to try LaTeX:

```text
1. Choose Overleaf or set up VS Code + TinyTeX.
2. Compile LaTeX_Installation_Test.tex.
3. Open the homework template.
4. Change your name/title.
5. Change one equation.
6. Compile again.
```

If you want to try Markdown:

```text
1. Open Markdown_First_Note.md.
2. Change the title.
3. Add one bullet point.
4. Add **bold text**.
5. Preview it in VS Code or GitHub.
```

That is enough to start.

---

## Need more setup help?

Open [`SETUP_GUIDE.md`](SETUP_GUIDE.md) for a longer explanation of:

- Overleaf;
- LyX;
- VS Code + LaTeX Workshop;
- TinyTeX installation;
- `pdflatex` / `latexmk` checks;
- missing LaTeX packages;
- PATH problems;
- local compilation troubleshooting.
