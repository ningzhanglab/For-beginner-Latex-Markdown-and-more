# Cheat Sheet

Quick lookup for the commands you will use most. The full 12-page PDF is below the tables. Use the search box (top of the page) to find a command.

<div class="actions" markdown>
[:material-download: Download the PDF](files/02_LaTeX_Cheat_Sheets/LaTeX_Paper_Writing_Cheat_Sheet.pdf){ .md-button .md-button--primary }
[:material-file-code: Source (.tex)](files/02_LaTeX_Cheat_Sheets/LaTeX_Paper_Writing_Cheat_Sheet.tex){ .md-button }
</div>

## Commands to learn first

| Command | What it does | Result |
|---|---|---|
| `\section{...}` | Section heading | Numbered heading |
| `\textbf{...}` | Bold text | **bold** |
| `\emph{...}` | Emphasis (usually italic) | *emphasis* |
| `$...$` | Inline math | x<sub>i</sub> |
| `\[ ... \]` | Display math | Centered equation |
| `_` and `^` | Subscript and superscript | x<sub>i</sub>, x² |
| `\frac{a}{b}` | Fraction | a/b stacked |
| `\sum` | Summation | Σ |
| `\begin{align*}` | Aligned derivation | Aligned lines |
| `\text{...}` | Words inside math | Upright text in an equation |
| `\begin{table}` | Table float | Numbered table |
| `\begin{tabular}` | Rows and columns | Table body |
| `\includegraphics` | Import an image | Figure |
| `\caption{...}` | Table or figure title | Caption |
| `\label{...}` | Target for a reference | Invisible anchor |
| `\ref{...}` | Reference to a table, figure, or section | Number |
| `\eqref{...}` | Reference to an equation | (Number) |
| `\footnote{...}` | Footnote | Footnote marker |
| `\citet{key}` | Textual citation | Author (year) |
| `\citep{key}` | Parenthetical citation | (Author, year) |
| `\multicolumn` | Heading that spans columns | Spanning cell |
| `\input{file}` | Insert another `.tex` file | File contents |
| `\appendix` | Begin the appendix | Lettered sections |
| `\newcommand` | Your own shortcut | Custom command |

## Special characters

These characters mean something to LaTeX. To print them, escape them.

| To print | Type |
|---|---|
| `%` | `\%` |
| `&` | `\&` |
| `_` | `\_` |
| `#` | `\#` |
| `$` | `\$` |
| `{` `}` | `\{` `\}` |
| `\` | `\textbackslash` |

An unescaped `%` turns the rest of the line into a comment.

## Math spacing

Math mode ignores the spaces you type. Add space with these commands, smallest to largest:

| Command | Size | Example |
|---|---|---|
| `\!` | Small **negative** space | `a\!b` |
| `\,` | Tiny | `a\,b` |
| `\:` | Small | `a\:b` |
| `\;` | Medium | `a\;b` |
| `\quad` | About 1 em | `a\quad b` |
| `\qquad` | About 2 em | `a\qquad b` |

!!! tip "Do not over-space"
    Good spacing shows structure. If you add `\quad` everywhere to make an equation "look nicer", the real fix is usually a better layout.

## Rules of thumb

- Refer to numbers with `\ref` or `\cref`; never type them.
- Put `\label` **after** `\caption`.
- Start float placement with `[htbp]`.
- Use `\[ ... \]` or `equation`, not `$$ ... $$`.
- Use a blank line for a new paragraph, not `\\`.

Stuck on an error? See [Troubleshooting](learn/troubleshooting.md).

## The full PDF

<iframe class="pdf-frame" src="../files/02_LaTeX_Cheat_Sheets/LaTeX_Paper_Writing_Cheat_Sheet.pdf" title="LaTeX Paper-Writing Cheat Sheet"></iframe>

!!! note
    If the PDF does not display in your browser, use the download button above.
