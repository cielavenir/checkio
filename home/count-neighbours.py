count_neighbours=lambda a,y,x:sum(0<=x+dx<len(a[0])and 0<=y+dy<len(a)and a[y+dy][x+dx]for dx in range(-1,2)for dy in range(-1,2)if dx|dy)

#count_neighbours=lambda a,y0,x0:sum(0<=x<len(a[0])and 0<=y<len(a)and a[y][x]for x in range(x0-1,x0+2)for y in range(y0-1,y0+2)if (x-x0)|(y-y0))

if __name__ == '__main__':
	assert count_neighbours(((1, 0, 0, 1, 0),
							 (0, 1, 0, 0, 0),
							 (0, 0, 1, 0, 1),
							 (1, 0, 0, 0, 0),
							 (0, 0, 1, 0, 0),), 1, 2) == 3, "1st example"
	assert count_neighbours(((1, 0, 0, 1, 0),
							 (0, 1, 0, 0, 0),
							 (0, 0, 1, 0, 1),
							 (1, 0, 0, 0, 0),
							 (0, 0, 1, 0, 0),), 0, 0) == 1, "2nd example"
	assert count_neighbours(((1, 1, 1),
							 (1, 1, 1),
							 (1, 1, 1),), 0, 2) == 3, "Dense corner"
	assert count_neighbours(((0, 0, 0),
							 (0, 1, 0),
							 (0, 0, 0),), 1, 1) == 0, "Single"