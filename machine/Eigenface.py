# @Time : 2022/12/2 15:14
# @Author : WZG
# --coding:utf-8--

# 特征脸
import numpy as np
import matplotlib.pyplot as plt
from sklearn.datasets import fetch_lfw_people
faces = fetch_lfw_people()

random_indexes = np.random.permutation(len(faces.data))
X = faces.data[random_indexes]
example_faces = X[:36,:]


def plot_faces(faces):
    fig, axes = plt.subplots(6, 6, figsize=(10, 10),
                             subplot_kw={'xticks': [], 'yticks': []},
                             gridspec_kw=dict(hspace=0.1, wspace=0.1))
    for i, ax in enumerate(axes.flat):
        ax.imshow(faces[i].reshape(62, 47), cmap='bone')
    plt.show()


plot_faces(example_faces)

from sklearn.decomposition import PCA
pca = PCA(svd_solver='randomized')
pca.fit(X)

plot_faces(pca.components_[:36,:])

faces2 = fetch_lfw_people(min_faces_per_person=60)