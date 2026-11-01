# Troubleshooting

Most LaTeX problems are small typos. Use the table to find your symptom, then read the fix below it.

## Find your error

| Message or symptom | First thing to check |
|---|---|
| `Undefined control sequence` | Typo in a command, or a missing package. |
| `Missing $ inserted` | A math command used outside math mode, or an unmatched `$`. |
| `Extra alignment tab has been changed to \cr` | Too many `&` in a table or `align` row. |
| `Missing } inserted` | A missing closing brace nearby. |
| `Runaway argument?` | Usually a missing `}` or `\end{...}`. |
| `Environment ... undefined` | A misspelled environment or a missing package. |
| `\begin{...} ended by \end{...}` | `\begin` and `\end` names do not match. |
| Reference shows `??` | Compile again; check the label exists and is spelled the same. |
| Citation shows `?` | Check the citation key and that the `.bib` file is loaded. |
| `File ... not found` | Wrong path, file name, extension, or capitalization. |
| `Overfull \hbox` | Something is too wide for the line (a URL, equation, or table). |
| Figure or table "moved" | Normal. Placement is a request, not a command. |

## How to debug, step by step

1. Read the **first** error, not the twenty that follow it.
2. Look at the reported line **and several lines above it**.
3. Check braces, dollar signs, `\begin`/`\end` pairs, and special characters.
4. Ask what you changed most recently.
5. Comment out the suspicious block with `%` and compile again.
6. Restore pieces gradually until the error comes back.

This "reduce the problem" method is much faster than changing commands at random.

## Common mistakes and their fixes

=== "Missing brace"

    **Wrong**

    ```latex
    \frac{a}{b
    ```

    **Correct**

    ```latex
    \frac{a}{b}
    ```

    A missing brace can confuse LaTeX far from the typo, so check the lines before the reported one.

=== "Math outside math mode"

    **Wrong**

    ```latex
    The coefficient is \beta.
    ```

    **Correct**

    ```latex
    The coefficient is $\beta$.
    ```

=== "Special characters"

    **Wrong**

    ```latex
    The response rate is 80%.
    R&D spending increases.
    data_clean.csv
    ```

    **Correct**

    ```latex
    The response rate is 80\%.
    R\&D spending increases.
    data\_clean.csv
    ```

    A bare `%` turns the rest of the line into a comment.

=== "Mismatched environments"

    **Wrong**

    ```latex
    \begin{align}
    a &= b+c
    \end{equation}
    ```

    **Correct**

    ```latex
    \begin{align}
    a &= b+c
    \end{align}
    ```

=== "Typed numbers"

    **Avoid**

    ```latex
    As shown in Table 3 ...
    Equation (5) implies ...
    ```

    **Prefer labels**

    ```latex
    As shown in Table~\ref{tab:main} ...
    Equation~\eqref{eq:model} implies ...
    ```

    If you later add a table earlier in the paper, the numbers update by themselves.

=== "Caption and label"

    ```latex
    \caption{Main Results}
    \label{tab:main}
    ```

    Put `\label` **after** `\caption`, or the reference may point to the wrong number.

=== "Old display math"

    You may see `$$ y = a + bx $$` in old files. In modern LaTeX, prefer:

    ```latex
    \[
      y = a + bx
    \]
    ```

    or a numbered `equation` environment.

## Habits that prevent problems

- **Do not use `\\` for paragraph spacing.** Leave a blank line in the source instead. Use `\\` only where a break is structurally required, such as table rows or aligned equations.
- **Start float placement with `[htbp]`.** Forcing every float with `[H]` can leave large blank areas.
- **Wrap long URLs in `\url{...}`** so they can break across lines.
- **Overfull `\hbox`** means a line is too wide. **Underfull `\hbox`** means LaTeX struggled to space a line nicely; it is often cosmetic, but look at the page.

## Setup problems

### A package is missing

The error looks like this:

```text
LaTeX Error: File `booktabs.sty' not found.
```

Your document is fine; your TeX installation just lacks the package. With TinyTeX or TeX Live:

```bash
tlmgr install booktabs
```

If you do not know which package holds a file:

```bash
tlmgr search --global --file "/booktabs.sty"
```

In R, use `tinytex::tlmgr_install("booktabs")`. Do not delete useful LaTeX code just to silence a missing-package error.

### VS Code cannot find LaTeX

Symptoms: `spawn latexmk ENOENT` or `latexmk: command not found`. Try these in order:

1. Restart VS Code.
2. Open a **new** terminal.
3. Restart your computer.
4. Check `pdflatex --version` and `latexmk --version`.
5. Confirm TinyTeX is installed (in R, `tinytex::tinytex_root()`).

More detail is in the [Setup Guide](../setup.md).

### Still stuck?

Compile the [installation test](../files/00_Start_Here/LaTeX_Installation_Test.tex). If that works, the problem is in your document. If it fails, the problem is in your setup. Overleaf is a good fallback while you sort out a local install.
