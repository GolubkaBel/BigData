from sklearn.manifold import TSNE
from sklearn import datasets
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns
import pandas as pd
import warnings
import time
import matplotlib

matplotlib.use('TkAgg')
warnings.filterwarnings("ignore")

data = datasets.fetch_openml('mnist_784', version=1, return_X_y=True)
pixel_values, targets = data
targets = targets.astype(int)
t = time.perf_counter()
tsne = TSNE(n_components=2, perplexity=25, random_state=42)
transformed_data = tsne.fit_transform(pixel_values.iloc[:3000, :])
print(transformed_data)
tsne_df = pd.DataFrame(np.column_stack((transformed_data, targets[:3000])),
                       columns=["x", "y", "targets"])
print(time.perf_counter() - t)
print(tsne_df)
tsne_df.loc[:, "targets"] = tsne_df.targets.astype(int)
print(tsne_df)

fig = plt.figure()
sns.scatterplot(x='x', y='y', hue=tsne_df['targets'], data=tsne_df, palette='bright')
#plt.show()
