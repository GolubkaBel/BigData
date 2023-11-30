import matplotlib
import numpy as np
import pandas as pd
import seaborn as sns

matplotlib.use('TkAgg')
import plotly.graph_objs as go
import matplotlib.pyplot as plt
from sklearn.manifold import TSNE
from sklearn.cluster import KMeans
from sklearn.cluster import DBSCAN
from sklearn.metrics import silhouette_score
from sklearn.cluster import AgglomerativeClustering

data = pd.read_csv('insurance.csv')
data.drop(['region', 'smoker'], axis=1, inplace=True)
data['sex'].replace({'male': 0, 'female': 1}, inplace=True)
data['charges'] = data['charges'].apply(lambda x: x/100)
print(data)

'''models = []
score1 = []
score2 = []
for i in range(2, 10):
    model = KMeans(n_clusters=i, random_state=123, init='k-means++').fit(data)
    models.append(model)
    score1.append(model.inertia_)
    score2.append(silhouette_score(data, model.labels_))

fig1, im = plt.subplots(1, 2)
im[0].plot(np.arange(2, 10), score1, marker='o')
im[1].plot(np.arange(2, 10), score2, marker='o')
plt.show()'''

model1 = KMeans(n_clusters=4, random_state=123, init='k-means++').fit(data)
print(model1.cluster_centers_)
#data['claster'] = model1.labels_
'''
fig3 = go.Figure(data=[go.Scatter3d(x=data['bmi'], y=data['age'], z=data['charges'],
                                    mode='markers', marker_color=data['claster'], marker_size=4)])
fig3.show()

model2 = AgglomerativeClustering(4, compute_distances=True).fit(data)
data['claster'] = model2.labels_
fig4 = go.Figure(data=[go.Scatter3d(x=data['bmi'], y=data['age'], z=data['charges'],
                                    mode='markers', marker_color=data['claster'], marker_size=4)])
fig4.show()

model3 = DBSCAN(eps=11, min_samples=5).fit(data)
data['claster'] = model3.labels_
fig5 = go.Figure(data=[go.Scatter3d(x=data['bmi'], y=data['age'], z=data['charges'],
                                    mode='markers', marker_color=data['claster'], marker_size=4)])
fig5.show()'''

tsne = TSNE(n_components=3, perplexity=25, random_state=42)
transformed_data = tsne.fit_transform(data.iloc[:1000, :])
tsne_df = pd.DataFrame(np.column_stack((transformed_data, model1.labels_[:1000])),
                       columns=["x", "y", "z", "targets"])
fig6 = plt.figure()
fig6 = go.Figure(data=[go.Scatter3d(x=tsne_df['x'], y=tsne_df['y'], z=tsne_df['z'],
                                    mode='markers', marker_color=tsne_df['targets'], marker_size=4)])
fig6.show()
