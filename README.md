# python-data-project-template

## Features

### jupytext

By using [Jupytext](https://github.com/mwouts/jupytext), do version control notebooks as plain text, instead of `*.ipynb`. You can edit the notebook on your favorite text editor.

Run the following code, convert your notebook to a `*.py` in the double percent format.

```bash
poetry shell
jupytext --sync notebooks/your_notebooks.ipynb
```

If you'd like to change other formats under version control,  improve [`jupytext.toml`](https://jupytext.readthedocs.io/en/latest/config.html#configuring-paired-notebooks-globally).
