---
title: LaTeX for Beginners
hide:
  - navigation
  - toc
---

<div class="hero" markdown>

# LaTeX for Beginners

<p class="lead">A handbook, a cheat sheet, and working templates for students, researchers, and academic writers. No Git or programming experience needed.</p>

<div class="actions" markdown>
[:material-rocket-launch: Start in Overleaf](setup.md#2-route-a-overleaf-no-local-setup){ .md-button .md-button--primary }
[:material-laptop: Install locally](setup.md#4-route-c-vs-code-latex-workshop-tinytex){ .md-button }
[:material-file-document-multiple: Grab a template](templates.md){ .md-button }
</div>

</div>

<div class="demo">
<div>
<p class="label">You write</p>

```latex
\documentclass{article}
\begin{document}
Hello, \LaTeX!
\[
  y_i = \alpha + \beta x_i + \varepsilon_i
\]
\end{document}
```
</div>
<div>
<p class="label">LaTeX produces</p>
<div class="paper">Hello, LaTeX!
<p class="eq">y<sub>i</sub> = α + β x<sub>i</sub> + ε<sub>i</sub></p></div>
</div>
</div>

## Where to go

<div class="gallery compact">
<div class="card"><div class="body">
<h3>1. Set up</h3>
<p>Pick a route (browser or local), then compile a tiny test file to confirm it works.</p>
<div class="btns"><a class="primary" href="setup/">Setup guide</a><a href="files/00_Start_Here/LaTeX_Installation_Test.tex">Test file (.tex)</a></div>
</div></div>
<div class="card"><div class="body">
<h3>2. Learn</h3>
<p>110-page handbook from "what does compile mean" to tables, figures, citations, and paper patterns.</p>
<div class="btns"><a class="primary" href="learn/path/">One-week path</a><a href="learn/">Contents</a><a href="files/01_LaTeX_Handbooks/LaTeX_Beginner_Handbook.pdf">PDF</a></div>
</div></div>
<div class="card"><div class="body">
<h3>3. Look things up</h3>
<p>A 12-page cheat sheet of the commands you will use most often when writing a paper.</p>
<div class="btns"><a class="primary" href="cheatsheet/">Open cheat sheet</a><a href="learn/troubleshooting/">Fix an error</a></div>
</div></div>
<div class="card"><div class="body">
<h3>4. Copy a template</h3>
<p>Minimal, homework, research paper, and Beamer slides. Open in Overleaf or download.</p>
<div class="btns"><a class="primary" href="templates/">Browse templates</a></div>
</div></div>
</div>

<div class="stats">
<div><strong>110</strong><span>page handbook</span></div>
<div><strong>171</strong><span>short sections</span></div>
<div><strong>4</strong><span>ready templates</span></div>
<div><strong>12</strong><span>page cheat sheet</span></div>
</div>

!!! tip "Not sure where to start?"
    Use **Overleaf** if you want zero installation. Come back to a local setup later if you want it. Or follow the [one-week learning path](learn/path.md).

## Questions

See the [FAQ](about/faq.md), or report a mistake via [GitHub issues](https://github.com/ningzhanglab/LaTeX-for-Beginners/issues/new/choose).

## Companion project

Looking for lightweight notes and README files? See [Markdown for Beginners](https://github.com/ningzhanglab/Markdown-for-Beginners).
