# A one-week learning path

You do not need to read the whole handbook. This path gets you from nothing to a compiled research paper in about a week of short sessions (30–60 minutes each). Skip ahead if a step is easy for you. It expands the short "First-Week Learning Plan" at the end of the handbook.

!!! tip "The one habit that matters"
    Compile after **every small change**. When something breaks, you will know exactly which change caused it.

## Day 1 — Get a working setup

**Goal:** compile a document and see a PDF.

1. Pick a route on the [Setup](../setup.md) page. Overleaf is the fastest.
2. Compile the [installation test](../files/00_Start_Here/LaTeX_Installation_Test.tex).
3. Change the sentence and compile again.

**Handbook:** Part 1, *Start Here: How LaTeX Works*.

## Day 2 — Write text

**Goal:** a document with a title, sections, bold and italic text, and a list.

1. Open the [Minimal template](../templates.md).
2. Add a new `\section{...}` and two paragraphs.
3. Type `5%` once without a backslash and see what happens, then fix it with `5\%`.

**Handbook:** Part 2, *Text, Punctuation, and Document Structure*.

## Day 3 — Write math

**Goal:** inline math, a numbered equation, and a multi-line derivation.

1. Write `$y = \alpha + \beta x$` in a sentence.
2. Add a numbered `equation` and refer to it with `\eqref{...}`.
3. Turn a two-step derivation into an `align` block.

**Handbook:** Part 3, *Math from Zero*, and Part 4, *Equations in an Academic Paper*.

## Day 4 — Homework

**Goal:** finish a real problem set in LaTeX.

1. Copy the [Homework template](../templates.md).
2. Replace the course name, your name, and the due date.
3. Solve one question with an `align` derivation and one with a lettered list.

**Cheat sheet:** keep the [command list](../cheatsheet.md) open.

## Day 5 — Tables and figures

**Goal:** a booktabs table and an included figure, both with captions and labels.

1. Make a three-column table with `\toprule`, `\midrule`, `\bottomrule`.
2. Add a figure with `\includegraphics`.
3. Refer to both with `\ref{...}` or `\cref{...}`; never type the number by hand.

**Handbook:** Part 8, *Tables*, and Part 9, *Figures and Graphics*.

## Day 6 — Citations and references

**Goal:** a bibliography built from a `.bib` file.

1. Open the [Research paper template](../templates.md) and its `references.bib`.
2. Add one entry of your own and cite it with `\citet{...}` and `\citep{...}`.
3. Compile twice if a citation shows `?`.

**Handbook:** Part 10, *Cross-References, Footnotes, Links, and Citations*.

## Day 7 — Put it together

**Goal:** a short paper with abstract, sections, one table, one figure, and citations.

1. Start from the research-paper template.
2. Replace every placeholder with your own text.
3. Keep the [troubleshooting guide](troubleshooting.md) handy.

**Handbook:** Part 11, *Research Paper-Writing Patterns You Will Actually Reuse*.

## After the first week

- Give a talk: use the Beamer template.
- Tidy your preamble: the *Preamble and Setup Guide* has ready-to-copy preambles for homework, empirical papers, and theory papers.
- Learn the small spacing and layout commands (handbook Parts 5 and 6) when you want finer control.

## Before you submit: ten checks

Run through this list before sending a paper or problem set.

- [ ] Compile from a clean state and check for real errors.
- [ ] Search the PDF for `??` and unresolved citations.
- [ ] Every figure and table is mentioned in the text.
- [ ] Every figure and table has a useful caption.
- [ ] Table notes give the sample, standard errors, units, and abbreviations where relevant.
- [ ] Equation symbols are defined near first use.
- [ ] Wide equations and tables do not overflow the margin.
- [ ] TODO notes and draft comments are removed.
- [ ] The bibliography style and every cited reference are correct.
- [ ] You opened the final PDF separately and looked at several pages, especially tables and figures.
