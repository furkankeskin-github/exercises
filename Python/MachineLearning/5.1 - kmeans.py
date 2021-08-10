# -*- coding: utf-8 -*-
"""
Created on Fri Jul 10 16:16:03 2020

@author: furkankeskin
"""



import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

veriler = pd.read_csv('musteriler.csv')

X = veriler.iloc[:,3:].values

from sklearn.cluster import KMeans

kmeans = KMeans ( n_clusters = 4, init = 'k-means++')
Y_tahmin=kmeans.fit_predict(X)
print(Y_tahmin)

plt.scatter(X[Y_tahmin==0,0],X[Y_tahmin==0,1], s=100, c='red')
plt.scatter(X[Y_tahmin==1,0],X[Y_tahmin==1,1], s=100, c='green')
plt.scatter(X[Y_tahmin==2,0],X[Y_tahmin==2,1], s=100, c='blue')
plt.show()

print(kmeans.cluster_centers_)
sonuclar = []
for i in range(1,11):
    kmeans = KMeans (n_clusters = i, init='k-means++', random_state= 123)
    kmeans.fit(X)
    #inertia bizim wcss değerlerimiz.
    sonuclar.append(kmeans.inertia_)

plt.plot(range(1,11),sonuclar)

#Hierarchical Clustering
from sklearn.cluster import AgglomerativeClustering
#Cluster sayısı, affinity/uzaklık türü, linkage/kümeler arası uzaklık hesaplama türü
ac = AgglomerativeClustering(n_clusters=3, affinity='euclidean', linkage='ward')
Y_tahmin = ac.fit_predict(X)
#Dataların clusterlarını gösterir
print(Y_tahmin)

plt.scatter(X[Y_tahmin==0,0],X[Y_tahmin==0,1], s=100, c='red')
plt.scatter(X[Y_tahmin==1,0],X[Y_tahmin==1,1], s=100, c='green')
plt.scatter(X[Y_tahmin==2,0],X[Y_tahmin==2,1], s=100, c='blue')
plt.show()

