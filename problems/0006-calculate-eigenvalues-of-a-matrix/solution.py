import math

def calculate_eigenvalues(matrix: list[list[float|int]]) -> list[float]:
	trace = matrix[0][0] + matrix[1][1]
	determinant = matrix[0][0] * matrix[1][1] - matrix[0][1] * matrix[1][0]
	discriminant = trace ** 2 - 4 * determinant

	eigenvalue_1 = (trace + math.sqrt(discriminant)) / 2
	eigenvalue_2 = (trace - math.sqrt(discriminant)) / 2
	eigenvalues = [eigenvalue_1, eigenvalue_2]
	
	return eigenvalues