# %%
import pandas as pd 
import plotly.express as px
import seaborn as sns
import numpy as np
import matplotlib.pylab as plt
from sklearn.decomposition import PCA
from sklearn.preprocessing import StandardScaler

sns.set(font="monospace", font_scale=1.25, style='white')

# %%
iris_df = px.data.iris()
iris_df

# %%
# subset the variable columns
X = iris_df.loc[:, ["sepal_length", "sepal_width", "petal_length", "petal_width"]]
X

# %%
# subset the sample column
y = iris_df.loc[:, "species"]
y

# %%
# scale variable columns
X = StandardScaler().fit_transform(X)

# %%
# assess principal components
pca = PCA(n_components=4)
principal_components = pca.fit_transform(X)

# %%
# create barplot to visualize variance captured in each principal component
sns.barplot(x=['PC1','PC2','PC3','PC4'],
           y=(pca.explained_variance_ratio_)*100,
           edgecolor = 'black',
           palette = 'YlGnBu').set(title='Principal Components', ylabel='Percent (%)')
plt.show()

# %%
# create dataframe for PCA plot
principal_components_df = pd.DataFrame(data = principal_components, 
                                       columns = ['PC1', 'PC2', 'PC3', 'PC4'])
principal_components_df = pd.concat([principal_components_df, y], axis = 1)
principal_components_df

# %%
# get PCA loadings dataframe
loadings_df = pd.DataFrame(data = np.transpose(pca.components_), columns = ['PC1', 'PC2', 'PC3', 'PC4'])    
X = px.data.iris().loc[:, ["sepal_length", "sepal_width", "petal_length", "petal_width"]]
loadings_df["variable"] = list(X.columns)
loadings_df

# %%
# plot PCA plot with loadings 
fig = px.scatter(principal_components_df, 
                 x='PC1', 
                 y='PC2', 
                 color=principal_components_df["species"],
                 color_discrete_sequence=["#512C96", 
                                          "#3C6F9C", 
                                          "#DD6892"], 
                 labels={"PC1": "PC1 ({}%)".format(round((pca.explained_variance_ratio_[0] * 100),2)),
                         "PC2": "PC2 ({}%)".format(round((pca.explained_variance_ratio_[1] * 100),2)),
                         "species": "Species"},
                 title="PCA plot"+" ("+str(iris_df.shape[0])+" features)",
                 template="plotly_white")

#updates the range of x and y axis    
fig.update_xaxes(dtick=1, range=[-4, 4])
fig.update_yaxes(dtick=1, range=[-4, 4])

#determines if border of plot should be shown
fig.update_xaxes(showline=True, linewidth=2, linecolor='black', mirror=True)
fig.update_yaxes(showline=True, linewidth=2, linecolor='black', mirror=True)

#determines gridlines details
fig.update_xaxes(showgrid=True, gridwidth=2, gridcolor='#E8E8E8')
fig.update_yaxes(showgrid=True, gridwidth=2, gridcolor='#E8E8E8')

#determines how zerolines should be displayed
fig.update_xaxes(zerolinewidth=2, zerolinecolor='#E8E8E8')
fig.update_yaxes(zerolinewidth=2, zerolinecolor='#E8E8E8')

#updates size of feature points in plot
fig.update_traces(marker=dict(size=10),
                  selector=dict(mode='markers')) 

#specifies layout details
fig.update_layout(height=700, 
                  width=800, 
                  showlegend=True, 
                  legend_title_text='Species',
                  font=dict(family="Courier New, monospace",
                            size=18,
                            color="black"),
                  title_x=0.22)

#add loadings
n = loadings_df.shape[0]
for i in range(n):
    fig.add_annotation(x= 0, 
                       y= 0, 
                       ax=loadings_df.iloc[i,0] * 3,  
                       ay=loadings_df.iloc[i,1] * 3, 
                       xref='x',
                       yref='y',
                       axref='x',
                       ayref='y',
                       text=loadings_df.iloc[i,4],  
                       showarrow=True,
                       arrowhead=3,
                       arrowsize=1,
                       arrowwidth=1,
                       arrowcolor='red',
                       opacity=0.6,
                       arrowside='start')

fig.write_html("pca_plot_iris_data.html")
fig.show()

# %%
plt.figure(figsize=(4,2))
sns.heatmap(loadings_df.set_index("variable"),
           cmap='YlGnBu',
           linewidths=0.7,
           linecolor="black").set(title='Loadings', ylabel=None)
plt.savefig("loadings_heatmap.png", bbox_inches='tight')
plt.show()


