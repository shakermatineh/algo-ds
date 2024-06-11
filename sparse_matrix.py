class SparseMatrixWithDict:
	# problem with dict based implmentation:
	# each key has to be hashed to determine position in internal array.
	# hash comupation overhead and more importantly hash storage overhead.
	# key as a coordinate has to be stored as well.
	# internal array is larger than number of items to reduce collison and 
	# maintain efficient access. Additional pointer storage overheads, for 
	# example pointer to next position in case of collison.

	def __init__(self, rows, cols):
		self.rows = rows
		self.cols = cols
		self.data = {}

	def set(self, row, col, val):
		if val != 0:
			self.data[(row, col)] = val
		else:
			if (row, col) in self.data:
				del self.data[(row, col)]

	def get(self, row, col):
		if (row, col) in self.data:
			return self.data[(row, col)]
		else:
			return 0

	def add(self, matrix):
		if not isinstance(matrix, SparseMatrixWithDict):
			# argument with inappropriate type 
			raise TypeError("matrix must be instance of SparseMatrixWithDict.")
		if self.rows != matrix.rows or self.cols != matrix.cols:
			# argument with inappropriate value
			raise ValueError("Matrix dimensions do not match.")

		result = SparseMatrixWithDict(matrix.rows, matrix.cols)
		for (r, c), val in self.data.items():
			result.set(r, c, val)

		for (r, c), val in matrix.data.items():
			result.set(r, c, val + result.get(r, c))

		return result





matrix1 = SparseMatrixWithDict(2, 2)
matrix1.set(0, 0, 1)
matrix1.set(0, 1, 1)

matrix2 = SparseMatrixWithDict(2, 2)
matrix2.set(0, 0, 1)
matrix2.set(1, 0, 1)

result = matrix1.add(matrix2)

print(result.get(0, 0))  # Output: 2
print(result.get(0, 1))  # Output: 1
print(result.get(1, 0))  # Output: 1
print(result.get(1, 1))  # Output: 0