from sklearn.cluster import KMeans
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import style
style.use("ggplot")

# Plotting and visualizing our data before feeding it into the Machine learning Algorithm
x = [1, 5, 1.5, 8, 1, 9]
y = [2, 8, 1.8, 8, 0.6, 11]
plt.scatter(x, y)
plt.show()

# Converting our data to a Numpy array
X = np.array([[1, 2], [5, 8], [1.5, 1.8], [8, 8], [1, 0.6], [9, 11], [4, 7], [9, 6], [2, 3], [1.4, 2.3]])

# We initialize K-Means algorithm with the required parameter and we use fit() to fit the data
kmeans = KMeans(n_clusters=2)
kmeans.fit(X)

# Getting the values of centroids and labels based on the fitment
centroids = kmeans.cluster_centers_
labels = kmeans.labels_
print(centroids)
print(labels)

# Plotting and visualinzing output
colors = ["g.", "r.", "c,", "y."]
for i in range(len(X)):
    print("Coordinate:", X[i], "label:", labels[i])
    plt.plot(X[i][0], X[i][1], colors[labels[i]], markersize=10)

plt.scatter(centroids[:, 0], centroids[:, 1], marker="x", s=150, linewidths=5, zorder=10)
plt.show()



