def matrix_dot_vector(a: list[list[int|float]], b: list[int|float]) -> list[int|float]:
	# Return a list where each element is the dot product of a row of 'a' with 'b'.
	# If the number of columns in 'a' does not match the length of 'b', return -1.
	if not a or not b:
		return -1

	if any(len(row) != len(b) for row in a):
		return -1

	result = []
	for row in a:
		dot_product = 0
		for x, y in zip(row, b):
			dot_product += x * y 
		result.append(dot_product)

	return result