# %%
# importing the libraries
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import scipy.stats as stats
import seaborn as sns
from sklearn.preprocessing import scale
from sklearn.decomposition import PCA

# %%
# set NumPy options
np.set_printoptions(suppress=True)
pd.set_option('display.max_rows', 20)

# %%
# read CSV data with Pandas
data = pd.read_csv("data/china_population.csv")

# %%
# setup data column
data.columns = ["V" + str(i) for i in range(1, len(data.columns) + 1)]
# independent variables data
X = data.loc[:, "V1":"V12"]
# dependent variable data
y = data.V13

# %%
print("## Data:")
print(data)

# %%
print("## Head:")
print(data.head())

# %%
print("## Info:")
data.info()

# %%
# calculating correlations for multivariate data
corr = stats.pearsonr(X.V2, X.V3)
print("p-value:\t", corr[1])
print("cor:\t\t", corr[0])

corr_mat = X.corr()
print(corr_mat)

plt.figure()
sns.heatmap(corr_mat, vmax=1., square=False).xaxis.tick_top()
plt.show()

# %%
def most_highly_correlated(my_dataframe, num_to_report):
    # find the correlations
    cor_matrix = my_dataframe.corr()
    # set the correlations on the diagonal or lower triangle to zero,
    # so they will not be reported as the highest ones:
    cor_matrix *= np.tri(*cor_matrix.values.shape, k=-1).T
    # find the top n correlations
    cor_matrix = cor_matrix.stack()
    cor_matrix = cor_matrix.reindex(cor_matrix.abs().sort_values(ascending=False).index).reset_index()
    # assign human-friendly names
    cor_matrix.columns = ["FirstVariable", "SecondVariable", "Correlation"]
    return cor_matrix.head(num_to_report)


print(most_highly_correlated(X, 10))

# %%
def print_total_population_China():
    df = pd.read_csv('data/china_population.csv')
    df_ = pd.read_csv('data/china_population_forecast.csv')
    city_list = pd.read_csv('data/city_population_china.csv')
    df_.sort_index(ascending=False, inplace=True)
    df = pd.concat([df_, df])
    df.reset_index(inplace=True)
    df.drop(index=6, inplace=True)
    x = df['Year']
    y = df['Population']
    plt.figure(figsize=(13,5))
    plt.plot(x,y,color='#EDB120')
    plt.plot(x,y,'*',color='r',markersize=22)
    plt.xlabel('Year')
    plt.xticks([1960, 1970, 1980, 1990, 2000, 2010, 2020, 2030, 2040, 2050])
    plt.ylabel('Population')
    plt.yticks()
    plt.title('Total population of China   (1955-2050)')
    plt.show()
print_total_population_China()

# %%
def print_percentage_yearly_change_Population():
    df = pd.read_csv('data/china_population.csv')
    df_ = pd.read_csv('data/china_population_forecast.csv')
    city_list = pd.read_csv('data/city_population_china.csv')
    df_.sort_index(ascending=False, inplace=True)
    df = pd.concat([df_, df])
    df.reset_index(inplace=True)
    df.drop(index=6, inplace=True)
    x = df['Year']
    y = df['Yearly % Change']
    plt.figure(figsize=(13,5))
    plt.plot(x,y,'#4DBEEE')
    plt.plot(x,y,'h',color='#EDB120',markersize=18)
    plt.xlabel('Year')
    plt.ylabel('Yearly % Change')
    plt.title('Percentage Yearly Change in Population  (1955-2050)')
    plt.show()
print_percentage_yearly_change_Population()

# %%
# standardising variables
standardisedX = scale(X)
standardisedX = pd.DataFrame(standardisedX, index=X.index, columns=X.columns)

print(standardisedX.apply(np.mean))
print(standardisedX.apply(np.std))

# %%
# principal component analysis
pca = PCA().fit(standardisedX)
def pca_summary(pca, standardised_data, out=True):
    names = ["PC"+str(i) for i in range(1, len(pca.explained_variance_ratio_)+1)]
    a = list(np.std(pca.transform(standardised_data), axis=0))
    b = list(pca.explained_variance_ratio_)
    c = [np.sum(pca.explained_variance_ratio_[:i]) for i in range(1, len(pca.explained_variance_ratio_)+1)]
    columns = pd.MultiIndex.from_tuples([("sdev", "Standard deviation"), ("varprop", "Proportion of Variance"), ("cumprop", "Cumulative Proportion")])
    summary = pd.DataFrame(list(zip(a, b, c)), index=names, columns=columns)
    if out:
        print("Importance of components:")
        print(summary)
    return summary


summary = pca_summary(pca, standardisedX)
print(summary.sdev)
print(np.sum(summary.sdev**2))

# %%
# how many principal components to retain
def scree_plot(pca, standardised_values):
    y = np.std(pca.transform(standardised_values), axis=0)**2
    x = np.arange(len(y)) + 1
    plt.plot(x, y, "o-")
    plt.xticks(x, ["Comp."+str(i) for i in x], rotation=60)
    plt.ylabel("Variance")
    plt.show()


plt.figure()
scree_plot(pca, standardisedX)

print(summary.sdev**2)

# %%
# scatter plots of the principal components
def pca_scatter(pca, standardised_values, classifs):
    foo = pca.transform(standardised_values)
    bar = pd.DataFrame(list(zip(foo[:, 0], foo[:, 11], classifs)), columns=["PC1", "PC2", "Global Rank of China"])
    sns.lmplot(x="PC1", y="PC2", data=bar, hue="Global Rank of China", fit_reg=False)


pca_scatter(pca, standardisedX, y)


