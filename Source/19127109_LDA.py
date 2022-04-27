# %%
# Importing Datasets From Sklearn
import matplotlib.pyplot as plt
from sklearn.discriminant_analysis import LinearDiscriminantAnalysis
import pandas as pd

# %%
# Loading seed Dataset 
df = pd.read_csv("data/china_population_forecast.csv")
df

# %%
y = df['China Global Rank'] # Split off classifications
X = df.iloc[:, [0, 1, 2, 3, 4, 5, 6,7,8,9,10,11]].values

# %%
# fitting the LDA model
lda = LinearDiscriminantAnalysis(n_components=2)
lda_X = lda.fit(X, y).transform(X)

# %%
plt.scatter(lda_X[y == 1, 0], lda_X[y == 1, 1], s =100,  c = 'yellow', label = 'Target 1')
plt.scatter(lda_X[y == 2, 0], lda_X[y == 2, 1], s =100,  c = 'green', label = 'Target 2')
plt.title('LDA plot for China Population Forecast')
plt.legend()


