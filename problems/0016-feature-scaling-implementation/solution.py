import numpy as np

def feature_scaling(data: np.ndarray) -> (np.ndarray, np.ndarray):
	# Your code here
	means = np.mean(data, axis=0)
	stds = np.std(data, axis=0)
	stds_safe = np.where(stds == 0, 1, stds)
	standardized = (data - means) / stds_safe
	standardized_data = np.round(standardized, 4)

	max_values = np.max(data, axis=0)
	min_values = np.min(data, axis=0)
	data_range = max_values - min_values
	data_range_safe = np.where(data_range == 0, 1, data_range)
	normalized = (data - min_values) / data_range_safe
	normalized_data = np.round(normalized, 4)

	return standardized_data, normalized_data