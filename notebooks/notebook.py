# ---
# jupyter:
#   jupytext:
#     formats: ipynb,py:percent
#     text_representation:
#       extension: .py
#       format_name: percent
#       format_version: '1.3'
#       jupytext_version: 1.11.3
#   kernelspec:
#     display_name: Python 3 (ipykernel)
#     language: python
#     name: python3
# ---

# %% [markdown]
# ## notebook

# %%
import sys
sys.path.append('../src')

import preprocess

from matplotlib import pyplot as plt
import pandas as pd

# %%
df = pd.read_csv(
    '../data/data.csv'
)
df['c'] = df.apply(
    lambda x: preprocess.foo(x['a'], x['b']), axis=1
)
df.head()

# %%
fig, axes = plt.subplots(figsize=(10, 4))
df.plot.box(ax=axes)
axes.grid();
