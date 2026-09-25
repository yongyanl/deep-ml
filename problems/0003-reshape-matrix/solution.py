import numpy as np

def reshape_matrix(a: list[list[int|float]], new_shape: tuple[int, int]) -> list[list[int|float]]:
	#Write your code here and return a python list after reshaping by using numpy's tolist() method
	matrix = np.array(a)
	if new_shape[0] * new_shape[1] != matrix.size:
		return []

	reshaped_matrix = matrix.reshape(new_shape)
	return reshaped_matrix.tolist()