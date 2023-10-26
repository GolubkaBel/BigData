from sklearn import datasets
import matplotlib.pyplot as plt
import numpy as np
import time
import umap
import seaborn as sns
import pandas as pd
import warnings
import matplotlib

matplotlib.use('TkAgg')
warnings.filterwarnings("ignore")


data = datasets.fetch_openml('mnist_784', version=1, return_X_y=True)
pixel_values, targets = data
targets = targets.astype(int)
t = time.perf_counter()
um = umap.UMAP(n_neighbors=5, min_dist=0.1, random_state=123).fit_transform(pixel_values.iloc[:3000, :])
umap_df = pd.DataFrame(np.column_stack((um, targets[:3000])),
                       columns=["x", "y", "targets"])
print(time.perf_counter()-t)
fig = plt.figure()
sns.scatterplot(x='x', y='y', hue=umap_df['targets'], data=umap_df, palette='bright')
plt.show()
