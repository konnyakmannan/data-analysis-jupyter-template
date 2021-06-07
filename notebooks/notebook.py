# ---
# jupyter:
#   jupytext:
#     formats: ipynb,py:percent
#     text_representation:
#       extension: .py
#       format_name: percent
#       format_version: '1.3'
#       jupytext_version: 1.11.2
#   kernelspec:
#     display_name: 'Python 3.9.5 64-bit (''python-data-project-template-iQRL-cf6-py3.9'':
#       poetry)'
#     name: python395jvsc74a57bd0547178f094375aa6a99ffd8434afbefe68694ee5e04c3ec98fa8d224070e847a
# ---

# %% [markdown]
# ## notebook
#
# 1. read a file
# 1. pre-process

# %%
import sys
sys.path.append('../src')

import preprocess

import numpy as np
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
fig, axes = plt.subplots(figsize=(6, 4))
df.plot.box(ax=axes)
axes.grid()
