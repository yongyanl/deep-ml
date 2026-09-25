def scalar_multiply(matrix: list[list[int|float]], scalar: int|float) -> list[list[int|float]]:
	# Your code here
	if not matrix or not any(matrix): 
		return matrix

	for r in range(len(matrix)):
		for c in range(len(matrix[0])):
			matrix[r][c] *= scalar

	return matrix
