# Contributing

Thank you for helping make this collection clearer for beginners. The most useful contributions are small:

- **A typo, broken example, or unclear sentence** — open an issue with the file name and page (or line) number.
- **A command beginners keep missing** — open an issue describing what you were trying to do.
- **A fix** — edit the `.tex` source, recompile the PDF, and open a pull request.

## Editing rules

1. Edit the `.tex` file, never only the PDF. A PDF in this repository is a reading copy.
2. Recompile with `latexmk -pdf <file>.tex` from inside that file's folder and commit the new PDF with its source.
3. Keep examples runnable with standard packages. If a new package is needed, say why in the pull request.
4. Do not commit restricted data, confidential drafts, credentials, or personal information.

## Checking your work

Every push runs a GitHub Action that compiles all `.tex` files and builds the website. To check the site locally:

```bash
pip install -r requirements.txt
python3 scripts/prepare_site.py
mkdocs build --strict
```
