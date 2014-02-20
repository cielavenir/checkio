def checkio(matrix):
	for y in range(len(matrix)):
		for x in range(len(matrix[0])-3):
			if all(matrix[y][x]==matrix[y][x+k] for k in range(4)): return True
	for y in range(len(matrix)-3):
		for x in range(len(matrix[0])):
			if all(matrix[y][x]==matrix[y+k][x] for k in range(4)): return True
	for y in range(len(matrix)-3):
		for x in range(len(matrix[0])-3):
			if all(matrix[y][x]==matrix[y+k][x+k] for k in range(4)): return True
	matrix=list(reversed(matrix))
	for y in range(len(matrix)-3):
		for x in range(len(matrix[0])-3):
			if all(matrix[y][x]==matrix[y+k][x+k] for k in range(4)): return True
	return False

#These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
	assert checkio([
		[1, 2, 1, 1],
		[1, 1, 4, 1],
		[1, 3, 1, 6],
		[1, 7, 2, 5]
	]) == True, "Vertical"
	assert checkio([
		[7, 1, 4, 1],
		[1, 2, 5, 2],
		[3, 4, 1, 3],
		[1, 1, 8, 1]
	]) == False, "Nothing here"
	assert checkio([
		[2, 1, 1, 6, 1],
		[1, 3, 2, 1, 1],
		[4, 1, 1, 3, 1],
		[5, 5, 5, 5, 5],
		[1, 1, 3, 1, 1]
	]) == True, "Long Horizontal"
	assert checkio([
		[7, 1, 1, 8, 1, 1],
		[1, 1, 7, 3, 1, 5],
		[2, 3, 1, 2, 5, 1],
		[1, 1, 1, 5, 1, 4],
		[4, 6, 5, 1, 3, 1],
		[1, 1, 9, 1, 2, 1]
	]) == True, "Diagonal"