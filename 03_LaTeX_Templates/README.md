# 03 · Templates

Copy one template into your own project folder, change one thing, and recompile.

| Template | Use it for | Needs |
|---|---|---|
| `LaTeX_Template_01_Minimal` | Your very first document | nothing else |
| `LaTeX_Template_02_Homework` | Problem sets and short solutions | nothing else |
| `LaTeX_Template_03_Paper` | Research papers | `references.bib`, `figures/example_figure.pdf` (keep them next to the `.tex`) |
| `LaTeX_Template_04_Slide` | Beamer talks (16:9) | nothing else |

All templates compile with **pdfLaTeX** (the default in Overleaf and VS Code + LaTeX Workshop). The paper template uses **BibTeX**; both tools run it automatically.

**Slide shape:** the Beamer template is widescreen (16:9). For 4:3, change the first line to `\documentclass[10pt]{beamer}`.

**No `references.bib` yet?** The paper template has a commented-out manual bibliography you can switch to.
