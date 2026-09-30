import numpy as np

def k_means_clustering(points: list[tuple[float, ...]], k: int, initial_centroids: list[tuple[float, ...]], max_iterations: int) -> list[tuple[float, ...]]:
	# Your code here
	points = np.array(points, dtype=float)
	centroids = np.array(initial_centroids, dtype=float)

	for _ in range(max_iterations):
		diffs = points[:, np.newaxis, :] - centroids
		squared_distances = np.sum(diffs ** 2, axis=2)
		labels = np.argmin(squared_distances, axis=1)

		old_centroids = centroids.copy()
		for i in range(k):
			cluster_points = points[labels == i]
			if len(cluster_points > 0):
				new_centroid = np.mean(cluster_points, axis=0)
				centroids[i] = new_centroid
		
		if np.allclose(old_centroids, centroids):
			break
	return [tuple(row) for row in np.round(centroids, 4)]