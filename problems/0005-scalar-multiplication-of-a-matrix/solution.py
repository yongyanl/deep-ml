def scalar_multiply(matrix: list[list[int|float]], scalar: int|float) -> list[list[int|float]]:
	# Your code here
	if not matrix or not any(matrix): 
		return matrix

	result = []
	for row in matrix:
		new_row = []
		for ele in row:
			new_row.append(ele * scalar)

		result.append(new_row)

	return result
