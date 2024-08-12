# Ethan Dibble
# kmeans

import math
import numpy as np
import matplotlib.pyplot as plt
from sklearn.datasets import make_blobs

def distance(point, centroid):
    # euclidean norm distance
    return math.sqrt((centroid[0]-point[0])**2 + (centroid[1]-point[1])**2)

def calculate_centroid(cluster):
    # calc new centroid
    x1, x2 = map(sum, zip(*cluster))
    return (x1 / len(cluster), x2 / len(cluster))

def calculate_mse(cluster, centroid):
    # calculate the mse of the cluster
    sum = 0
    for point in cluster:
        sum += (distance(point, centroid)**2)

    return sum / len(cluster)

def calculate_average_mse(clusters, centroids):
    # calculate the average mse for all clusters
    mse = 0
    for cluster, centroid in zip(clusters, centroids):
        mse += calculate_mse(cluster, centroid)

    return mse / len(centroids)

def kmeans(k, points):
    # Initialization centroids
    indices = np.random.choice(a=points.shape[0], size=k, replace=False)
    centroids = points[indices]
    
    # Loop until convergence
    converged = False
    while not converged:
        # Initialize or Clear previous clusters
        clusters = [[] for _ in range(k)]
    
        # Assign each point to the "closest" centroid 
        for point in points:
            distances_to_each_centroid = [distance(point, centroid) for centroid in centroids]
            cluster_assignment = np.argmin(distances_to_each_centroid)
            clusters[cluster_assignment].append(point)
        
        # Calculate new centroids
        new_centroids = [calculate_centroid(cluster) for cluster in clusters]
        
        converged = np.array_equal(new_centroids, centroids)
        centroids = new_centroids

        if converged:
            return clusters, np.array(centroids)

def main(k, rounds):
    points, labels = make_blobs(n_features=2, centers=k)

    for i in range(rounds):
        # run k means
        clusters, centroids = kmeans(k, points)

        # Plot results
        plt.scatter(points[:, 0], points[:, 1], c='blue', s=10)
        plt.scatter(centroids[:, 0], centroids[:, 1], c='red', s=50, alpha=0.75)
        plt.title(f'K-means Clustering round {i+1}')
        plt.show()

        print(calculate_average_mse(clusters, centroids))

if __name__ == "__main__":
    k = 5
    rounds = 10
    main(k, rounds)