def calculate_covariance_matrix(vectors: list[list[float]]) -> list[list[float]]:
	# Your code here
	if not vectors or not vectors[0]:
		return []

	n_features = len(vectors)
	n_observations = len(vectors[0])

	means = [
		sum(feature) / n_observations
		for feature in vectors
	]

	covariance_matrix = [
		[0 for _ in range(n_features)] 
		for _ in range(n_features)
	]

	for i in range(n_features):
		for j in range(n_features):

			feature_i = vectors[i]
			feature_j = vectors[j]

			covariance_sum = 0
			for k in range(n_observations):
				covariance_sum += (feature_i[k] - means[i]) * (feature_j[k] - means[j])
			
			covariance_matrix[i][j] = covariance_sum / (n_observations - 1)
	
	return covariance_matrix