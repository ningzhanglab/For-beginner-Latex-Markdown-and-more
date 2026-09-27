Suppose you are not familar with `Git` / `Github` things or you are the first time to see websites like this. If you do not know what to do in next. Please read this intro thoroughly. These technical toolkits are not difficult to handle it and you do not need to understand everything at first time.

**How to download these files?** Click the green botton `<>Code` below this repository title and choose download it as `zip` file.

# PhD Writing Toolkit

A beginner-friendly toolkit for PhD students who want to use **LaTeX and Markdown without needing a technical background**.

This repository is designed for students who may know little or nothing about LaTeX, Markdown, Git, terminals, or programming. It includes:

- a step-by-step LaTeX beginner handbook;
- a preamble and setup guide;
- a paper-writing cheat sheet;
- three copy-ready LaTeX templates;
- a Markdown beginner handbook;
- a Markdown editor/setup guide;
- tiny test files so you can check that your setup works before starting a real paper.

Economics and quantitative social-science examples appear throughout because they are useful for demonstrating equations, tables, figures, citations, and research-paper structure, but the toolkit is intended for **PhD students across disciplines**.

> **You do not need Git, a terminal, or programming knowledge to start.**  
> If you want the easiest route, use **Overleaf**. If you prefer a visual editor, try **LyX**.

---

## Start here: choose how you want to write LaTeX

| What you want                                             | Recommended route                         | Setup difficulty | What writing feels like                                      | Best for                                                |
| --------------------------------------------------------- | ----------------------------------------- | ---------------: | ------------------------------------------------------------ | ------------------------------------------------------- |
| **“I just want LaTeX to work.”**                          | **Overleaf**                              |         Very low | You type LaTeX source in a browser and see the PDF beside it | First-time users, coursework, collaboration             |
| **“I want LaTeX quality, but I prefer a visual editor.”** | **LyX**                                   |       Low–medium | You work with sections, equations, figures, citations, and menus while LyX generates LaTeX underneath | Students who dislike writing lots of raw LaTeX commands |
| **“I want to learn real LaTeX and work locally.”**        | **VS Code + LaTeX Workshop + TinyTeX**    |           Medium | You edit `.tex` source directly with strong local tooling    | Long-term paper writing, offline work, GitHub projects  |
| **“I already work in R or Quarto.”**                      | **RStudio / Positron / Quarto + TinyTeX** |           Medium | Prose, code, tables, figures, and PDF output can live in one reproducible workflow | Data-heavy and reproducible research                    |

### A simple decision rule

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

If you are unsure, start with **Overleaf**. You can move to another workflow later without relearning LaTeX.

For detailed local-installation instructions, see **[SETUP_GUIDE.md](SETUP_GUIDE.md)**.

---

# 1. Overleaf — easiest setup for complete beginners

[Overleaf](https://www.overleaf.com/) is an online LaTeX editor that runs in your browser.

You do **not** need to install:

- LaTeX;
- TinyTeX;
- VS Code;
- a compiler;
- Git.

### Quick start

1. Create an Overleaf account.
2. Download this repository as a ZIP, or download one of the `.tex` templates.
3. In Overleaf choose **New Project → Upload Project** if you have a ZIP.
4. Open the main `.tex` file.
5. Click **Recompile**.
6. Change one sentence and compile again.

A good first file is:

```text
03_LaTeX_Templates/LaTeX_Template_02_PhD_Homework.tex
```

### Why use Overleaf?

- no local setup;
- source and PDF appear side by side;
- easy sharing with supervisors and coauthors;
- many journal and university templates are available;
- good for learning by changing a working example.

### When might you move away from Overleaf?

A local workflow becomes useful when you want:

- offline writing;
- Git/GitHub version control;
- very large projects;
- tighter integration with local R, Python, Stata, Julia, or data files;
- full control over compilation and folders.

Official resources: [Overleaf Learn](https://www.overleaf.com/learn) and [Learn LaTeX in 30 minutes](https://www.overleaf.com/learn/latex/Learn_LaTeX_in_30_minutes).

---

# 2. LyX — visual LaTeX writing

[LyX](https://www.lyx.org/) is a visual document editor built around LaTeX.

It is useful if you want the **structure and typesetting quality of LaTeX** but do not want to type every command manually.

Instead of writing everything as raw source such as:

```latex
\section{Introduction}

\[
  y_i = x_i'\beta + \varepsilon_i,
  \qquad i=1,\ldots,n.
\]
```

LyX lets you insert a section, equation, figure, citation, or table through its interface. LyX then generates LaTeX behind the scenes.

### Think of LyX as

```text
Word-like editing experience
        +
LaTeX document structure and typesetting
```

It is **not exactly Microsoft Word**. LyX still encourages you to describe what something *is*—a section, theorem, equation, citation, figure—rather than manually positioning every object.

### Good reasons to choose LyX

- you are uncomfortable editing raw `.tex` source;
- you write many equations;
- you want structured long documents such as a dissertation;
- you want LaTeX-quality output with fewer commands to memorize;
- you prefer menus and visual document structure.

### Main limitation

LyX gives you less direct control over the underlying source. Highly customized journal templates, unusual packages, or complicated publisher requirements may eventually require some LaTeX knowledge.

Knowing basic LaTeX is therefore still useful even if LyX is your main editor.

## LyX setup

LyX still needs a **TeX/LaTeX distribution** to create the final PDF.

The LyX project recommends installing the TeX system before LyX so LyX can detect it during configuration.

Typical combinations are:

| Operating system | Simple LyX setup                                           |
| ---------------- | ---------------------------------------------------------- |
| Windows          | TeX Live or MiKTeX → then LyX                              |
| macOS            | MacTeX → then LyX                                          |
| Linux            | TeX Live from your distribution/package manager → then LyX |

Download LyX from:

<https://www.lyx.org/Download>

Official LyX documentation:

<https://www.lyx.org/Documentation>

### What about TinyTeX with LyX?

TinyTeX is a TeX Live-based distribution and can work with many LaTeX tools. However, for a **complete beginner using LyX**, a standard TeX Live/MacTeX/MiKTeX installation is usually the simpler documented route because LyX is designed to discover a normal TeX installation automatically.

If you already have TinyTeX working, you do not necessarily need to replace it; advanced users can point LyX to an existing TeX installation. For first-time setup, follow the LyX documentation for your operating system.

### First LyX test

After installation:

1. open LyX;
2. choose **File → New**;
3. type a short sentence;
4. insert a displayed equation;
5. use **View → PDF** or the corresponding preview command;
6. confirm that a PDF is generated.

LyX includes built-in **Introduction**, **Tutorial**, and **User Guide** documents under its Help menu. These are excellent places to start.

### LyX vs. Overleaf

|                                   | LyX               | Overleaf                       |
| --------------------------------- | ----------------- | ------------------------------ |
| Editing style                     | Visual/structured | Raw LaTeX source               |
| Installation                      | Yes               | No                             |
| Local/offline                     | Yes               | Mainly browser-based           |
| Learn LaTeX commands immediately? | Not necessary     | Yes, gradually                 |
| Collaboration                     | File/Git-based    | Very easy online collaboration |
| Direct control of `.tex`          | Less direct       | Full source editing            |

A useful shorthand is:

> **Overleaf = easiest setup**  
> **LyX = easiest visual writing**  
> **VS Code = most direct control**  
> **RStudio/Quarto = strongest reproducible-research workflow**

---

# 3. VS Code + LaTeX Workshop + TinyTeX — recommended local source workflow

This route is useful if you want to learn normal LaTeX source and keep your projects locally.

You need **three separate pieces**:

```text
VS Code          = editor
LaTeX Workshop   = VS Code extension/helper
TinyTeX          = LaTeX distribution/compiler
```

A common beginner mistake is assuming VS Code itself compiles LaTeX. It does not.

Your workflow is:

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

## Step 1 — Install VS Code

Download:

<https://code.visualstudio.com/>

## Step 2 — Install LaTeX Workshop

In VS Code:

1. click **Extensions**;
2. search for **LaTeX Workshop**;
3. install the extension by James Yu;
4. restart VS Code if requested.

Official extension page:

<https://marketplace.visualstudio.com/items?itemName=James-Yu.latex-workshop>

## Step 3 — Install TinyTeX

TinyTeX is a lightweight TeX Live-based LaTeX distribution.

Official documentation:

<https://yihui.org/tinytex/>

### If you already use R or RStudio

Run:

```r
install.packages("tinytex")
tinytex::install_tinytex(bundle = "TinyTeX")
```

Then restart R/RStudio and VS Code.

The names are easy to confuse:

```text
tinytex   = R package
TinyTeX   = LaTeX distribution
```

The `TinyTeX` bundle includes more commonly used packages than the smallest installation and is convenient for beginners.

### macOS without R

```bash
curl -sL "https://tinytex.yihui.org/install-bin-unix.sh" | sh
```

### Linux without R

```bash
wget -qO- "https://tinytex.yihui.org/install-bin-unix.sh" | sh
```

### Windows without R

For beginners, using the R installation route above is often straightforward. Otherwise follow the official TinyTeX Windows instructions.

## Step 4 — Verify the installation

Open a **new** terminal and run:

```bash
pdflatex --version
latexmk --version
```

You only need to see version information rather than an error saying the command cannot be found.

## Step 5 — Test this repository

Open the full repository folder in VS Code, then open:

```text
00_Start_Here/LaTeX_Installation_Test.tex
```

Run:

```text
LaTeX Workshop: Build LaTeX project
```

If the PDF appears, your basic local setup works.

For more detailed troubleshooting, see **[SETUP_GUIDE.md](SETUP_GUIDE.md)**.

---

# 4. RStudio / Positron / Quarto + TinyTeX

This route is especially useful if your research already combines prose and analysis code.

Install TinyTeX from R:

```r
install.packages("tinytex")
tinytex::install_tinytex(bundle = "TinyTeX")
```

This workflow is convenient when a document includes:

- prose;
- equations;
- R or Python code;
- automatically generated tables;
- automatically generated figures;
- citations;
- reproducible appendices.

You do not have to use one editor for everything. A common research workflow is:

```text
R / Python / Stata   → analysis
Quarto / Markdown    → notes and reproducible reports
VS Code / LyX        → paper writing
Overleaf             → collaboration or submission
GitHub               → version control and public documentation
```

---

# 5. Also new to Markdown? Choose one simple route

Markdown requires much less setup than LaTeX. For basic use, you do **not** need a compiler.

| Your situation                                      | Recommended Markdown tool             | Installation? | Best for                                                |
| --------------------------------------------------- | ------------------------------------- | ------------: | ------------------------------------------------------- |
| “I already use VS Code.”                            | **VS Code built-in Markdown preview** |  VS Code only | Local notes, project documentation, GitHub repositories |
| “I want to edit a README in my browser.”            | **GitHub web editor**                 |          None | Repository documentation                                |
| “I want collaborative notes.”                       | **HackMD**                            |          None | Coauthor meetings, seminars, shared outlines            |
| “I want a simple browser editor with live preview.” | **StackEdit**                         |          None | Learning and quick Markdown writing                     |
| “My prose sits next to R/Python code.”              | **Jupyter / Colab / Quarto**          |       Depends | Computational and reproducible research                 |

Start with:

```text
00_Start_Here/Markdown_First_Note.md
```

Then read:

```text
04_Markdown/Markdown_Setup_and_Editors_Guide.md
```

## Markdown in VS Code

Save a file with the `.md` extension.

Preview it with:

```text
macOS:         Shift+Command+V
Windows/Linux: Ctrl+Shift+V
```

Preview beside the source with:

```text
macOS:         Command+K, then V
Windows/Linux: Ctrl+K, then V
```

Basic Markdown support is built into VS Code; you do not need a Markdown extension to begin.

---

# 6. Download this repository without learning Git

You do **not** need Git to use the toolkit.

On GitHub:

1. click **Code**;
2. choose **Download ZIP**;
3. unzip the folder;
4. open the PDF guides directly;
5. open `.tex` files in Overleaf, LyX-compatible workflows, or VS Code;
6. open `.md` files in VS Code, GitHub, HackMD, StackEdit, or another Markdown editor.

That is enough for most beginners.

If you later want version history and automatic syncing without using the command line, **GitHub Desktop** is a good next step.

---

# 7. What is included?

## 7.1 LaTeX Beginner Handbook

### `PhD_LaTeX_Beginner_Handbook`

**Start here if you are new to LaTeX.**

The handbook uses the pattern:

> **What it does → what you type → what appears in the PDF → common mistake / when to use it**

It covers:

- `.tex` → compile → `.pdf`;
- commands, arguments, options, environments, and packages;
- headings, paragraphs, lists, comments, and reserved characters;
- inline and display math;
- equations and alignment;
- spacing commands such as `\,`, `\quad`, `\qquad`, `\hfill`, and `~`;
- tables and figures;
- citations and bibliographies;
- labels and cross-references;
- theorem, assumption, definition, proposition, and proof environments;
- appendices and multi-file projects;
- inline code and code blocks;
- compiler errors and debugging;
- research-paper writing patterns;
- quick-reference tables.

Economics-style examples appear where they are especially useful for equations, regression-style tables, notation, or paper structure, but the LaTeX techniques are general.

---

## 7.2 Preamble and Setup Guide

### `PhD_LaTeX_Preamble_and_Setup_Guide`

Use this when you want to understand or modify the setup of a LaTeX project.

Topics include:

- document classes;
- page geometry;
- fonts and LaTeX engines;
- math packages;
- tables and figures;
- bibliography packages;
- hyperlinks and smart references;
- theorem environments;
- custom commands;
- project organization;
- ready-to-copy preambles for homework and research papers.

---

## 7.3 Paper-Writing Cheat Sheet

### `PhD_LaTeX_Paper_Writing_Cheat_Sheet`

Keep this open beside your editor while writing.

It includes fast lookup for:

```latex
\,
\;
\!
\quad
\qquad
~
\hfill
&
\\
\notag
```

as well as equations, tables, figures, citations, labels, references, appendices, reserved characters, and common mistakes.

---

## 7.4 LaTeX Templates

### `LaTeX_Template_01_Minimal`

The smallest working template. Use it to test an installation or start a tiny document.

### `LaTeX_Template_02_PhD_Homework`

For problem sets, quantitative coursework, take-home assignments, and derivations.

### `LaTeX_Template_03_PhD_Paper`

A clean research-paper starting point. Some sample content uses economics and quantitative-social-science conventions, but the structure is general.

---

## 7.5 Markdown Guides

### `Markdown_Setup_and_Editors_Guide`

Use this if you are unsure **where to write Markdown**.

It covers:

- VS Code;
- GitHub's web editor;
- HackMD;
- StackEdit;
- Jupyter / Colab;
- Quarto;
- basic preview workflows;
- when different Markdown environments behave differently.

### `PhD_Markdown_Beginner_Guide`

Use this for:

- research notes;
- paper-reading notes;
- seminar notes;
- advisor-meeting notes;
- project READMEs;
- replication instructions;
- research logs;
- data dictionaries;
- lightweight reproducible documentation.

---

# 8. Recommended learning path

If you are completely new:

1. **Choose one writing route**: Overleaf, LyX, VS Code, or RStudio/Quarto.
2. Open `PhD_LaTeX_Beginner_Handbook.pdf`.
3. Learn only commands, environments, text, and basic math at first.
4. Open a working template.
5. Replace sample content with your own work.
6. Compile after small changes.
7. Keep the cheat sheet open while writing.
8. Read the Preamble Guide only when you need to change packages or formatting.
9. Use Markdown for research notes and repository documentation.
10. Learn Git only when version control becomes useful to you.

The fastest way to learn is:

> **Start from something that already works → change one thing → compile → repeat.**

Do not try to memorize LaTeX before using it.

---

# 9. Which format should I use?

| Task                          | Good default                                       |
| ----------------------------- | -------------------------------------------------- |
| Math-heavy homework           | LaTeX                                              |
| Mathematical derivation       | LaTeX                                              |
| Dissertation chapter          | LaTeX or LyX                                       |
| Research paper                | LaTeX, LyX, or journal-required format             |
| Journal submission            | Follow the journal's requirements                  |
| Research notes                | Markdown                                           |
| Paper-reading notes           | Markdown                                           |
| Seminar / meeting notes       | Markdown                                           |
| Project README                | Markdown                                           |
| Replication instructions      | Markdown                                           |
| Reproducible report with code | Quarto / R Markdown / Jupyter                      |
| Quick equations inside notes  | Markdown + LaTeX math                              |
| Slides                        | Beamer / PowerPoint / Quarto, depending on context |

A useful rule is:

> **Markdown for thinking and documenting; LaTeX/LyX for formal technical writing and polished long documents.**

---

# 10. `.tex`, `.lyx`, `.pdf`, and `.md`

| Extension | What it is                                                  |
| --------- | ----------------------------------------------------------- |
| `.tex`    | Editable LaTeX source                                       |
| `.lyx`    | LyX's editable document format                              |
| `.pdf`    | Final/readable output                                       |
| `.md`     | Editable Markdown source                                    |
| `.bib`    | Bibliography database used by LaTeX and many research tools |

Use a PDF when you only want to read the guide or inspect the result. Use the source file when you want to edit or study how it was produced.

---

# 11. Common setup problems

## “VS Code cannot find `latexmk` or `pdflatex`”

First:

1. quit VS Code;
2. quit your terminal;
3. reopen both;
4. run:

```bash
pdflatex --version
latexmk --version
```

If the commands still cannot be found, your TeX executable folder may not be on your system `PATH`. See `SETUP_GUIDE.md`.

## “File `something.sty` not found”

A LaTeX package is probably missing.

With TinyTeX/TeX Live:

```bash
tlmgr install booktabs
```

Or from R:

```r
tinytex::tlmgr_install("booktabs")
```

## “The PDF shows `??` instead of a reference”

LaTeX often needs multiple compilation passes for cross-references and bibliographies. `latexmk` usually handles this automatically.

## “LyX cannot create a PDF”

Check that a TeX distribution is installed and recognized by LyX. If you installed or changed the TeX system after installing LyX, use LyX's reconfiguration tools and restart the application.

## “It works on Overleaf but not locally”

The two environments may have different TeX versions or packages. Find the **first real error** in the local compilation log; later errors are often consequences of the first one.

---

# 12. A sensible PhD research-project structure

```text
project/
├── paper/
│   ├── main.tex
│   ├── references.bib
│   ├── tables/
│   └── figures/
├── code/
├── data/
├── output/
├── notes/
└── README.md
```

Useful habits:

- keep source data separate from derived data;
- generate tables and figures from code when possible;
- avoid manually retyping numerical results;
- use labels instead of manually typing figure/table numbers;
- use relative file paths;
- keep a project README;
- use version control once it becomes useful;
- archive the exact code and data used for important results.

### Important for public GitHub repositories

Do **not** upload:

- confidential or licensed datasets;
- personally identifiable information;
- API keys, passwords, or `.env` secrets;
- private referee reports;
- unpublished coauthor materials without permission;
- restricted university or employer files.

The included `.gitignore` removes common LaTeX build files and some local folders, but you should still inspect your files before publishing.

---

# 13. GitHub workflow for non-technical users

You can use this repository at three levels.

### Level 1 — Download only

Use **Code → Download ZIP**. No Git knowledge is required.

### Level 2 — GitHub Desktop

Use GitHub Desktop if you want syncing and version history without command-line Git.

### Level 3 — Git in VS Code / terminal

Learn command-line Git only if your workflow eventually benefits from it.

Git is useful, but it is **not a prerequisite** for LaTeX or Markdown.

---

# 14. Learn patterns, not isolated commands

Instead of memorizing only `\qquad`, learn the spacing family:

```latex
\,       % small math space
\:       % medium-small space
\;       % medium space
\!       % negative space
\quad    % large space
\qquad   % very large space
```

Instead of remembering only `\ref`, learn the complete figure pattern:

```latex
\begin{figure}[htbp]
  \centering
  \includegraphics[width=0.75\linewidth]{figures/main_result.pdf}
  \caption{Main result}
  \label{fig:main}
\end{figure}

As shown in Figure~\ref{fig:main}, ...
```

Patterns are more reusable than isolated commands.

---

# 15. Repository map

```text
PhD_Writing_Toolkit/
│
├── README.md
├── SETUP_GUIDE.md
├── .gitignore
│
├── 00_Start_Here/
│   ├── LaTeX_Installation_Test.tex
│   └── Markdown_First_Note.md
│
├── 01_LaTeX_Handbooks/
│   ├── PhD_LaTeX_Beginner_Handbook.pdf
│   ├── PhD_LaTeX_Beginner_Handbook.tex
│   ├── PhD_LaTeX_Preamble_and_Setup_Guide.pdf
│   └── PhD_LaTeX_Preamble_and_Setup_Guide.tex
│
├── 02_LaTeX_Cheat_Sheet/
│   ├── PhD_LaTeX_Paper_Writing_Cheat_Sheet.pdf
│   └── PhD_LaTeX_Paper_Writing_Cheat_Sheet.tex
│
├── 03_LaTeX_Templates/
│   ├── LaTeX_Template_01_Minimal.pdf
│   ├── LaTeX_Template_01_Minimal.tex
│   ├── LaTeX_Template_02_PhD_Homework.pdf
│   ├── LaTeX_Template_02_PhD_Homework.tex
│   ├── LaTeX_Template_03_PhD_Paper.pdf
│   └── LaTeX_Template_03_PhD_Paper.tex
│
└── 04_Markdown/
    ├── Markdown_Setup_and_Editors_Guide.md
    ├── Markdown_Setup_and_Editors_Guide.pdf
    ├── PhD_Markdown_Beginner_Guide.md
    └── PhD_Markdown_Beginner_Guide.pdf
```

---

# 16. Where should I begin?

**I have never used LaTeX and want zero setup.**  
→ Start with **Overleaf**.

**I dislike code and want a visual editor.**  
→ Try **LyX**.

**I want to learn normal LaTeX and keep everything locally.**  
→ Use **VS Code + LaTeX Workshop + TinyTeX**.

**I already work mainly in R or Quarto.**  
→ Use **RStudio / Positron / Quarto + TinyTeX**.

**I already know basic LaTeX.**  
→ Keep the **Paper-Writing Cheat Sheet** open while writing.

**I am writing a paper or dissertation chapter.**  
→ Start with the **PhD Paper Template**, or use LyX if you prefer visual editing.

**I am writing notes or documentation.**  
→ Start with `Markdown_First_Note.md` and the Markdown editor guide.

---

# 17. Repository philosophy

The goal is **not** to turn PhD students into TeX programmers.

The goal is to make writing infrastructure predictable enough that you can spend your time on the work that matters: ideas, evidence, analysis, proofs, experiments, writing, and revision.

Start simple. Use a working template. Compile often. Add complexity only when your project actually needs it.

---

## Official resources

### LaTeX and editors

- [Overleaf](https://www.overleaf.com/)
- [Overleaf Learn](https://www.overleaf.com/learn)
- [LyX](https://www.lyx.org/)
- [LyX Download](https://www.lyx.org/Download)
- [LyX Documentation](https://www.lyx.org/Documentation)
- [Visual Studio Code](https://code.visualstudio.com/)
- [LaTeX Workshop](https://marketplace.visualstudio.com/items?itemName=James-Yu.latex-workshop)
- [TinyTeX](https://yihui.org/tinytex/)
- [TinyTeX releases](https://github.com/rstudio/tinytex-releases)

### Markdown

- [VS Code Markdown](https://code.visualstudio.com/Docs/languages/markdown)
- [GitHub Markdown](https://docs.github.com/en/get-started/writing-on-github/getting-started-with-writing-and-formatting-on-github/basic-writing-and-formatting-syntax)
- [HackMD](https://hackmd.io/)
- [StackEdit](https://stackedit.io/)

---

## License and contribution

If this repository is published publicly, add the license you want contributors and students to follow (for example, MIT, CC BY 4.0, or another appropriate license), plus a short `CONTRIBUTING.md` if you want to accept corrections or examples from other students.
