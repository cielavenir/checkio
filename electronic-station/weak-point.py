def weak_point(matrix):
	row=float("inf")
	row_idx=0
	for i in range(len(matrix)):
		s=sum(matrix[i][j] for j in range(len(matrix[i])))
		if row>s:
			row=s
			row_idx=i
	col=float("inf")
	col_idx=0
	for j in range(len(matrix[0])):
		s=sum(matrix[i][j] for i in range(len(matrix)))
		if col>s:
			col=s
			col_idx=j
	return (row_idx,col_idx)

if __name__ == '__main__':
	assert isinstance(weak_point([[1]]), (list, tuple)), "The result should be a list or a tuple"
	assert list(weak_point([[7, 2, 7, 2, 8],
							[2, 9, 4, 1, 7],
							[3, 8, 6, 2, 4],
							[2, 5, 2, 9, 1],
							[6, 6, 5, 4, 5]])) == [3, 3], "Example"
	assert list(weak_point([[7, 2, 4, 2, 8],
							[2, 8, 1, 1, 7],
							[3, 8, 6, 2, 4],
							[2, 5, 2, 9, 1],
							[6, 6, 5, 4, 5]])) == [1, 2], "Two weak point"
	assert list(weak_point([[1, 1, 1],
							[1, 1, 1],
							[1, 1, 1]])) == [0, 0], "Top left"