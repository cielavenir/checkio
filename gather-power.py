def gather_people(building, time):
	for y in range(len(building)):
		for x in range(len(building[y])):
			if x!=y and building[y][x]==0: building[y][x]=99999
	for k in range(len(building)):
		for y in range(len(building)):
			for x in range(len(building[y])):
				if x!=y: building[y][x]=min(building[y][x],building[y][k]+building[k][x])
	return sum(building[i][i] for i in range(len(building)) if building[0][i]<=time)

if __name__ == '__main__':
	assert gather_people([[0, 40, 0, 40, 0, 0],
						  [40, 6, 0, 0, 40, 0],
						  [0, 0, 3, 0, 28, 0],
						  [40, 0, 0, 4, 40, 28],
						  [0, 40, 28, 40, 1, 0],
						  [0, 0, 0, 28, 0, 2]], 80), "Example"
	assert gather_people([[0, 40, 0, 40, 0, 0],
						  [40, 6, 0, 0, 40, 0],
						  [0, 0, 3, 0, 28, 0],
						  [40, 0, 0, 4, 40, 28],
						  [0, 40, 28, 40, 1, 0],
						  [0, 0, 0, 28, 0, 2]], 40), "Hurry"
	assert gather_people([[1, 0, 40, 0, 40, 40, 0, 40, 0],
						  [0, 1, 40, 0, 40, 0, 0, 0, 0],
						  [40, 40, 1, 40, 0, 0, 0, 0, 0],
						  [0, 0, 40, 1, 0, 89, 0, 0, 0],
						  [40, 40, 0, 0, 1, 0, 40, 0, 0],
						  [40, 0, 0, 89, 0, 1, 0, 0, 40],
						  [0, 0, 0, 0, 40, 0, 1, 40, 0],
						  [40, 0, 0, 0, 0, 0, 40, 1, 40],
						  [0, 0, 0, 0, 0, 40, 0, 40, 1]], 40), "Grid"