# PhD Writing Toolkit

Suppose you are not familar with `Git` / `Github` things or you are the first time to see websites like this. If you do not know what to do in next. Please read this intro thoroughly. These technical toolkits are not difficult to handle it and you do not need to understand everything at first time.



**How to download these file?** Click the green botton `<>Code` below this repository title and choose download it as `zip` file.



A beginner-friendly, open repository for PhD students who want to use **LaTeX and Markdown without needing a technical background**.

This repository is designed for students who may know little or nothing about LaTeX, Markdown, Git, terminals, or programming. It includes long-form handbooks, quick-reference sheets, copy-ready templates, and a step-by-step setup guide.

> **You do not need to learn Git or install anything to start.** If you are completely new, use **Overleaf** and one of the templates in this repository.

---

## Start here: choose one way to use LaTeX

| Your situation | Recommended setup | Installation? | Best for |
|---|---|---:|---|
| “I just want LaTeX to work.” | **Overleaf** | None | First-time users, coursework, collaboration |
| "I want to do it offline"                 |                                        |               |                                                        |
| “I want to write locally on my computer.” | **VS Code + LaTeX Workshop + TinyTeX** |           Yes | Long-term paper writing, offline work, GitHub projects |
| “I already live in R/RStudio or Quarto.”  | **RStudio/Quarto + TinyTeX**           |           Yes | Empirical researchers using R, R Markdown, or Quarto |

If you are unsure, start with **Overleaf**. Move to VS Code later when you want local files, GitHub integration, or an offline workflow.

For detailed installation instructions, see **[SETUP_GUIDE.md](SETUP_GUIDE.md)**.

## Also new to Markdown? Choose one simple route

Markdown needs much less setup than LaTeX. For basic use, you do **not** need a compiler.

| Your situation | Recommended Markdown tool | Installation? | Best for |
|---|---|---:|---|
| "I already use VS Code." | **VS Code built-in Markdown preview** | VS Code only | Local notes, project documentation, GitHub repositories |
| "I want to edit a README without installing anything." | **GitHub web editor** | None | Repository documentation |
| "I want shared notes like a collaborative document." | **HackMD** | None | Coauthor meetings, seminars, shared outlines |
| "I want a simple browser editor with live preview." | **StackEdit** | None | Learning and quick Markdown writing |
| "My prose sits next to R/Python code." | **Jupyter / Colab / Quarto** | Depends | Computational and reproducible research |

Start with **[`00_Start_Here/Markdown_First_Note.md`](00_Start_Here/Markdown_First_Note.md)** or read **[`04_Markdown/Markdown_Setup_and_Editors_Guide.md`](04_Markdown/Markdown_Setup_and_Editors_Guide.md)**.

In VS Code, save a file as `.md`, then use:

```text
macOS:         Shift+Command+V     preview
               Command+K, then V   preview to the side
Windows/Linux: Ctrl+Shift+V        preview
               Ctrl+K, then V      preview to the side
```

Basic Markdown works in VS Code without installing a Markdown extension.

---

# 1. Option A — Overleaf: easiest for complete beginners

[Overleaf](https://www.overleaf.com/) is an online LaTeX editor that runs in your browser. You do **not** need to install LaTeX, TinyTeX, VS Code, or any compiler.

### Quick start

1. Create a free Overleaf account.
2. Download this GitHub repository as a ZIP, or download one of the `.tex` templates.
3. In Overleaf, choose **New Project → Upload Project** if you have a ZIP, or create a blank project and upload the `.tex` file.
4. Open the main `.tex` file.
5. Click **Recompile**.
6. Edit the sample text and compile again.

A good first file is:

```text
03_LaTeX_Templates/LaTeX_Template_02_PhD_Homework.tex
```

### Why begin with Overleaf?

- no local installation;
- no terminal or command line;
- PDF preview appears beside the source;
- easy sharing with coauthors;
- journal templates are widely available;
- useful error messages and documentation.

### When might you move away from Overleaf?

A local workflow becomes attractive when you want:

- offline writing;
- Git/GitHub version control;
- very large projects;
- tighter integration with R, Python, Stata, or local data/code;
- more control over files and compilation.

Official beginner resources: [Overleaf Learn LaTeX](https://www.overleaf.com/learn) and [Learn LaTeX in 30 minutes](https://www.overleaf.com/learn/latex/Learn_LaTeX_in_30_minutes).

---

# 2. Option B — VS Code + TinyTeX: recommended local setup

This is the local setup I recommend for students who want a lightweight, modern workflow without installing the full multi-gigabyte TeX Live distribution.

You need **three pieces**:

1. **VS Code** — the editor where you type your `.tex` file;
2. **LaTeX Workshop** — a VS Code extension that adds LaTeX build/preview tools;
3. **TinyTeX** — the actual LaTeX distribution/compiler installed on your computer.

A common beginner confusion is thinking VS Code itself compiles LaTeX. It does not. VS Code is the editor; TinyTeX supplies programs such as `pdflatex`, `xelatex`, and `latexmk`.

## Step 1 — Install VS Code

Download and install [Visual Studio Code](https://code.visualstudio.com/).

Open VS Code once after installation.

## Step 2 — Install LaTeX Workshop

In VS Code:

1. click the **Extensions** icon in the left sidebar;
2. search for **LaTeX Workshop**;
3. install the extension by James Yu;
4. restart VS Code if prompted.

Official extension page: [LaTeX Workshop](https://marketplace.visualstudio.com/items?itemName=James-Yu.latex-workshop).

## Step 3 — Install TinyTeX

TinyTeX is a lightweight distribution based on TeX Live. It works on Windows, macOS, and Linux.

### Recommended route if you already use R

Open R or RStudio and run:

```r
install.packages("tinytex")
tinytex::install_tinytex(bundle = "TinyTeX")
```

The first line installs the **R package** named `tinytex`. The second installs the actual **TinyTeX LaTeX distribution**.

Why use `bundle = "TinyTeX"` here? It includes more commonly requested LaTeX packages than the smallest default bundle, which can reduce missing-package interruptions for beginners.

After installation, **restart R/RStudio and VS Code**.

Official documentation: [TinyTeX](https://yihui.org/tinytex/).

### macOS without R

Open Terminal and run:

```bash
curl -sL "https://tinytex.yihui.org/install-bin-unix.sh" | sh
```

After it finishes, close and reopen Terminal and VS Code.

### Linux without R

The TinyTeX website provides a Unix installation script. For most Linux systems:

```bash
wget -qO- "https://tinytex.yihui.org/install-bin-unix.sh" | sh
```

Restart your terminal and VS Code afterwards.

### Windows without R

For a non-technical user, the simplest route is usually to install R and use the two R commands above. TinyTeX also provides a Windows batch installer and pre-built Windows releases; see the official [TinyTeX installation page](https://yihui.org/tinytex/) if you prefer not to install R.

## Step 4 — Verify that LaTeX is installed

Open a **new** terminal after installation and run:

```bash
pdflatex --version
```

Then:

```bash
latexmk --version
```

If each command prints version information, VS Code should normally be able to find your LaTeX installation.

If the command says “not found” or “not recognized,” first restart your computer. PATH changes made during installation are sometimes not visible to applications that were already open.

## Step 5 — Test this repository

Open the entire repository folder in VS Code:

```text
File → Open Folder...
```

Then open:

```text
00_Start_Here/LaTeX_Installation_Test.tex
```

Use the VS Code Command Palette and run:

```text
LaTeX Workshop: Build LaTeX project
```

Then open the generated PDF using LaTeX Workshop's PDF viewer.

If that works, open one of the real templates and start editing.

---

# 3. Option C — RStudio / Quarto + TinyTeX

If most of your empirical work already happens in **R**, **RStudio**, or **Quarto**, TinyTeX fits naturally into that workflow.

Install it in R:

```r
install.packages("tinytex")
tinytex::install_tinytex(bundle = "TinyTeX")
```

TinyTeX is especially convenient for R Markdown and Quarto PDF output because the R `tinytex` package can help identify and install missing LaTeX packages during compilation.

This workflow is useful when your paper, notes, or appendix combine:

- prose;
- equations;
- R code;
- automatically generated tables;
- automatically generated figures.

You do **not** have to choose only one editor forever. Many researchers use RStudio or Jupyter for analysis, VS Code for `.tex` files, and Overleaf for collaboration.

---

# 4. What is TinyTeX, and why is it here?

A LaTeX editor is not enough by itself. Your computer needs a **LaTeX distribution**, which contains the programs and packages that turn `.tex` source into PDF.

Common distributions include:

- TeX Live;
- MacTeX;
- MiKTeX;
- TinyTeX.

This repository mentions **TinyTeX** because it is cross-platform, relatively lightweight, and particularly convenient for R users. TinyTeX is based on TeX Live.

For a beginner, the important distinction is:

```text
VS Code          = editor
LaTeX Workshop   = VS Code helper/extension
TinyTeX          = LaTeX compiler/distribution
.tex             = source file
.pdf             = compiled output
```

If you use Overleaf, Overleaf handles the compiler for you, so you do not need TinyTeX locally.

---

# 5. Downloading this GitHub repository without knowing Git

You do not need Git to use this repository.

On the GitHub repository page:

1. click **Code**;
2. choose **Download ZIP**;
3. unzip the folder;
4. open the PDF guides directly;
5. open `.tex` files in Overleaf or VS Code;
6. open `.md` files in any text editor or VS Code.

That is enough for most students.

If you later want automatic syncing and version history, consider **GitHub Desktop** before learning command-line Git.

---

# 6. What is included?

## LaTeX Handbooks

### `PhD_LaTeX_Beginner_Handbook`

**Start here if you are new to LaTeX.**

A detailed handbook built around:

> What it does → what you type → what appears in the PDF → common mistake / when to use it

Topics include:

- how `.tex` files compile into PDF;
- document structure and the preamble;
- headings, paragraphs, lists, comments, and reserved characters;
- inline and display math;
- equations and alignment;
- spacing commands such as `\,`, `\quad`, `\qquad`, `\hfill`, and `~`;
- tables and figures;
- citations and bibliography files;
- labels and cross-references;
- theorem, assumption, definition, proposition, and proof environments;
- appendices and multi-file projects;
- inline code and code blocks;
- common compiler errors and debugging;
- research-paper writing patterns;
- daily quick-reference tables.

Use it as both a first tutorial and a long-term reference manual.

### `PhD_LaTeX_Preamble_and_Setup_Guide`

Use this when you understand the basics and want to modify the setup of a LaTeX project.

It covers:

- document classes;
- page geometry;
- fonts and engines;
- core math packages;
- tables and figure packages;
- citation packages;
- hyperlinks and smart references;
- theorem environments;
- custom commands;
- project organization;
- ready-to-copy preambles for homework, empirical papers, and theory papers.

---

## LaTeX Cheat Sheet

### `PhD_LaTeX_Paper_Writing_Cheat_Sheet`

Keep this open beside your editor while writing.

It includes quick references for:

- common syntax;
- math notation;
- spacing and alignment;
- `\quad`, `\qquad`, `\,`, `\!`, `\hfill`, `~`, `&`, and related micro-commands;
- equations;
- tables;
- figures;
- citations;
- labels and references;
- appendices;
- reserved characters;
- common mistakes and compiler errors.

---

## LaTeX Templates

### `LaTeX_Template_01_Minimal`

Use this to test LaTeX or start the smallest possible document.

### `LaTeX_Template_02_PhD_Homework`

Use this for problem sets, coursework, and take-home assignments.

### `LaTeX_Template_03_PhD_Paper`

Use this as a clean starting point for a research paper; the included examples lean toward economics and quantitative social science.

---

## Markdown Guides

### `Markdown_Setup_and_Editors_Guide`

Start here if you are unsure **where to write Markdown**. It gives step-by-step instructions for VS Code, GitHub's web editor, HackMD, StackEdit, Jupyter/Colab, and Quarto, plus a first five-minute practice exercise. Both `.md` and compiled `.pdf` versions are included.

### `PhD_Markdown_Beginner_Guide`

Use this for research notes, READMEs, project documentation, seminar notes, replication instructions, and lightweight reproducible writing.

It explains:

- headings and paragraphs;
- lists and task lists;
- links and images;
- inline code and fenced code blocks;
- tables;
- LaTeX-style math inside Markdown;
- footnotes;
- YAML front matter;
- Pandoc/Quarto citations;
- paper-reading notes;
- seminar/advisor notes;
- research logs;
- data dictionaries;
- replication documentation;
- GitHub-flavored Markdown and other Markdown variants.

---

# 7. Recommended learning path

If you are completely new:

1. **Choose Overleaf or install VS Code + TinyTeX.**
2. Open `PhD_LaTeX_Beginner_Handbook.pdf`.
3. Read only enough to understand commands, environments, text, and basic math.
4. Open `LaTeX_Template_02_PhD_Homework.tex`.
5. Replace sample content with one of your real assignments.
6. Compile after small changes.
7. Keep the cheat sheet open while writing.
8. Use the Preamble Guide only when you need to modify packages or setup.
9. Move to the paper template when you begin research writing.
10. For Markdown, open `Markdown_First_Note.md`, then use the Markdown setup guide and beginner guide for notes, READMEs, replication instructions, and research logs.

The fastest way to learn is:

> **Start from a working template → change one thing → compile → repeat.**

Do not try to memorize LaTeX before using it.

---

# 8. Which format should I use?

| Task | Recommended format |
|---|---|
| Quantitative / math-heavy problem set | LaTeX |
| Mathematical derivation | LaTeX |
| Research paper | LaTeX |
| Journal submission | Journal-required format, often LaTeX |
| Research notes | Markdown |
| Paper-reading notes | Markdown |
| Seminar notes | Markdown |
| Advisor meeting notes | Markdown |
| Project README | Markdown |
| Replication instructions | Markdown |
| Quick equations inside notes | Markdown + LaTeX math |
| Presentation slides | Beamer / PowerPoint / Quarto, depending on context |

A useful rule:

> **Markdown for thinking and documenting; LaTeX for formal mathematical writing and final papers.**

---

# 9. `.tex`, `.pdf`, and `.md`

Most LaTeX materials appear in two forms:

- `.tex` — editable LaTeX source;
- `.pdf` — compiled output.

Use the PDF when you want to read a guide or inspect the result. Use the `.tex` file when you want to copy, edit, or study the source.

The Markdown guide appears as:

- `.md` — editable Markdown source;
- `.pdf` — rendered reading version.

---

# 10. Common local-setup problems

## “VS Code cannot find `latexmk` / `pdflatex`”

First:

1. close VS Code;
2. close your terminal;
3. reopen them;
4. try `pdflatex --version` and `latexmk --version` again.

If the commands still cannot be found, your TinyTeX executable folder may not be on your system `PATH`. See the official TinyTeX documentation and the troubleshooting section in `SETUP_GUIDE.md`.

## “File `something.sty` not found”

That usually means a LaTeX package is missing.

With TinyTeX/TeX Live, packages are managed by `tlmgr`. For example:

```bash
tlmgr install booktabs
```

If you installed TinyTeX through R, you can also manage packages from R:

```r
tinytex::tlmgr_install("booktabs")
```

Do not randomly edit the `.tex` file just because a `.sty` file is missing.

## “The PDF shows `??` instead of a reference”

Cross-references and citations often require more than one compilation. `latexmk` normally handles this automatically.

## “It works on Overleaf but not on my computer”

The two systems may have different packages or TeX versions installed. Read the **first real error** in the compilation log; later errors are often consequences of the first one.

---

# 11. Good habits for PhD research

A simple project can be organized as:

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
- avoid manually typing results that can be imported;
- use labels instead of manually typing figure/table numbers;
- use relative file paths;
- keep a project README;
- use Git for version control once you are comfortable;
- archive the exact code/data used for important results.

### Important for a public GitHub repository

Do **not** upload:

- confidential or licensed datasets;
- personally identifiable information;
- API keys or passwords;
- private referee reports;
- unpublished coauthor materials without permission;
- restricted university files.

The `.gitignore` in this repository excludes common LaTeX build files and common local data/output folders, but you should still check files before publishing.

---

# 12. GitHub workflow for non-technical users

You can use this repository at three levels:

### Level 1 — Download only

Use **Code → Download ZIP**. No Git knowledge required.

### Level 2 — GitHub Desktop

Use GitHub Desktop if you want version history and syncing without using the command line.

### Level 3 — Git in VS Code / terminal

Learn command-line Git only if and when your workflow requires it. It is not a prerequisite for learning LaTeX.

---

# 13. Learn patterns, not isolated commands

Rather than memorizing only `\qquad`, learn the spacing family:

```latex
\,       % small math space
\:       % medium-small space
\;       % medium space
\!       % negative space
\quad    % large space
\qquad   % very large space
```

Likewise, learn complete reference patterns:

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

# 14. File map

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
    ├── PhD_Markdown_Beginner_Guide.pdf
    └── PhD_Markdown_Beginner_Guide.md
```

---

# 15. Where should I begin?

**Never used LaTeX and do not want to install anything?**  
Use **Overleaf**, then open the Beginner Handbook and Homework Template.

**Never used LaTeX but want a local workflow?**  
Follow `SETUP_GUIDE.md` for **VS Code + LaTeX Workshop + TinyTeX**.

**Already use R/RStudio?**  
Install TinyTeX from R, then use RStudio, Quarto, VS Code, or a combination.

**Already know basic LaTeX?**  
Keep the Cheat Sheet open while writing.

**Writing a research paper?**  
Start from the PhD Paper Template.

**Writing notes or documentation?**  
Open `00_Start_Here/Markdown_First_Note.md`. If you are unsure which editor to use, read `04_Markdown/Markdown_Setup_and_Editors_Guide.md`, then keep the Markdown Beginner Guide as a reference.

---

# 16. Repository philosophy

The goal is not to turn PhD students into TeX programmers.

The goal is to make formatting infrastructure boring and predictable so that you can spend your time on research: theory, data, evidence, proofs, writing, and revision.

Start simple. Compile often. Add complexity only when the research requires it.

---

## Official resources

- [Overleaf](https://www.overleaf.com/)
- [Overleaf Learn](https://www.overleaf.com/learn)
- [Visual Studio Code](https://code.visualstudio.com/)
- [LaTeX Workshop](https://marketplace.visualstudio.com/items?itemName=James-Yu.latex-workshop)
- [TinyTeX](https://yihui.org/tinytex/)
- [TinyTeX releases](https://github.com/rstudio/tinytex-releases)
- [VS Code Markdown](https://code.visualstudio.com/Docs/languages/markdown)
- [GitHub Markdown](https://docs.github.com/en/get-started/writing-on-github/getting-started-with-writing-and-formatting-on-github/basic-writing-and-formatting-syntax)
- [HackMD](https://hackmd.io/)
- [StackEdit](https://stackedit.io/)

