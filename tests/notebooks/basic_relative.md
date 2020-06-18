---
jupytext:
  text_representation:
    extension: .md
    format_name: myst
    format_version: '0.8'
    jupytext_version: 1.5.0
kernelspec:
  display_name: Python 3
  language: python
  name: python3
---

# a title

some text

```{code-cell} ipython3
# Test reading a relative file to make sure relative paths work
with open("./conf.py") as ff:
    ff.read()
```
