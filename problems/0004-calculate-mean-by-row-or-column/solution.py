import numpy as np

def calculate_matrix_mean(matrix: list[list[float]], mode: str) -> list[float]:
	means = []
	if mode == 'row':
		for row in matrix:
			row_sum = np.sum(row);
			means.append(row_sum/len(matrix[0]));

	if mode == 'column':
		for j in range(len(matrix[0])):
			col_sum = 0;
			for row in range(len(matrix)):
				col_sum += matrix[row][j];

			means.append(col_sum/len(matrix))
	return means