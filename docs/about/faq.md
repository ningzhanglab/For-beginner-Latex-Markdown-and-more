# FAQ

## Should I use Overleaf or install LaTeX on my computer?

Use **Overleaf** if you are new, use a managed computer, or collaborate online. Install locally (VS Code + LaTeX Workshop + TinyTeX) if you want files on your own machine and a version-controlled workflow. You can switch later; the `.tex` files are the same.

## Do I need Git or GitHub?

No. Download the files as a ZIP, or use the **Downloads** page. Learn Git later if your research workflow benefits from it.

## Which engine should I use: pdfLaTeX, XeLaTeX, or LuaLaTeX?

All templates here use **pdfLaTeX**. Choose XeLaTeX or LuaLaTeX only when you need system fonts or full Unicode in the source. The *Preamble and Setup Guide* explains when.

## Why does my reference or citation show `??` or `?`?

LaTeX needs more than one pass to resolve references. Compile again. If it persists, check that the label or citation key exists and is spelled identically. See [Troubleshooting](../learn/troubleshooting.md).

## BibTeX or biblatex?

The research-paper template uses **natbib + BibTeX**, which is common in economics and works everywhere. `biblatex` + Biber is more flexible but a different workflow. Pick one; do not mix them in the same document.

## Why did my figure or table move?

Floats are placed by LaTeX using your placement request (`[htbp]`), not at the exact spot in the source. That is normal. Refer to floats with `\ref`/`\cref`, and avoid forcing every float with `[H]`.

## Can I use these templates for my own paper or class?

Yes. Everything here is licensed under CC BY 4.0, so you may copy, edit, and share it, including the templates, if you give credit. What you write is yours. See [License](license.md).

## Where do I report a mistake?

Open an issue on [GitHub](https://github.com/ningzhanglab/LaTeX-for-Beginners/issues/new/choose). Include the file and page number.
