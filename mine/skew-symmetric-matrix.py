def checkio(matrix):
	tr=[list(e) for e in zip(*matrix)]
	for y in range(len(matrix)):
		for x in range(len(matrix[0])):
			if matrix[y][x]!=-tr[y][x]: return False
	return True

if __name__ == '__main__':
	assert checkio([
		[0, 1, 2],
		[-1, 0, 1],
		[-2, -1, 0]]) == True, "1st example"
	assert checkio([
		[0, 1, 2],
		[-1, 1, 1],
		[-2, -1, 0]]) == False, "2nd example"
	assert checkio([
		[0, 1, 2],
		[-1, 0, 1],
		[-3, -1, 0]]) == False, "3rd example"