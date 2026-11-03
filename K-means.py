import math
import random

def distance(point1, point2):
    return math.sqrt(sum((a - b) ** 2 for a, b in zip(point1, point2)))


def kmeans(data, k, max_iterations=100):
    centroids = random.sample(data, k)

    for _ in range(max_iterations):
        clusters = [[] for _ in range(k)]
        for point in data:
            distances = [distance(point, c) for c in centroids]
            closest_idx = distances.index(min(distances))
            clusters[closest_idx].append(point)
        new_centroids = []
        for cluster in clusters:
            if cluster:
                mean_point = [sum(dim) / len(cluster) for dim in zip(*cluster)]
                new_centroids.append(mean_point)
            else:
                new_centroids.append(random.choice(data))
        if new_centroids == centroids:
            break

        centroids = new_centroids

    return centroids, clusters
data = [[1, 2], [1, 4], [2, 2], [10, 2], [10, 4], [11, 3]]
centroids, clusters = kmeans(data, k=2)

print("Centroids:", centroids)
print("Clusters:", clusters)