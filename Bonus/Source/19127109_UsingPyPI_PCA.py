# %%
import numpy as np
from sklearn.datasets import load_iris
import pandas as pd

# Load pca
from pca import pca


# %%
# Load dataset
label = load_iris().feature_names
y = load_iris().target
X = pd.DataFrame(data=load_iris().data, columns=label, index=y)

# %%
# Initialize to reduce the data up to the nubmer of componentes that explains 95% of the variance.
model = pca(n_components=0.95)

# Reduce the data towards 3 PCs
model = pca(n_components=3)

# Fit transform
results = model.fit_transform(X)

# %%
# Cumulative explained variance
print(model.results['explained_var'])
# [0.92461872 0.97768521 0.99478782]

# Explained variance per PC
print(model.results['variance_ratio'])
[0.92461872, 0.05306648, 0.01710261]

# Make plot
fig, ax = model.plot()

# %%
# 2D plot
fig, ax = model.scatter()

# 3d Plot
fig, ax = model.scatter3d()

# %%
# 2D plot
fig, ax = model.biplot(n_feat=4, PC=[0,1])

# 3d Plot
fig, ax = model.biplot3d(n_feat=2, PC=[0,1,2])


