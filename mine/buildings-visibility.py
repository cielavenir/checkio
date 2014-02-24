def checkio(buildings):
	xmax=max(int(e[2]) for e in buildings)
	ymax=max(int(e[3]) for e in buildings)
	a=[[0]*xmax for i in range(ymax)]
	for xm,ym,xM,yM,h in buildings:
		for y in range(ym,yM):
			for x in range(xm,xM):
				a[y][x]=h
	for x in range(xmax):
		h=0
		for y in range(ymax):
			if a[y][x]>h: h=a[y][x]
			else: a[y][x]=0
	return sum(
		any(any(a[y][x]>0 for x in range(xm,xM)) for y in range(ym,yM))
		for xm,ym,xM,yM,h in buildings
	)

if __name__ == '__main__':
	assert checkio([
		[1, 1, 4, 5, 3.5],
		[2, 6, 4, 8, 5],
		[5, 1, 9, 3, 6],
		[5, 5, 6, 6, 8],
		[7, 4, 10, 6, 4],
		[5, 7, 10, 8, 3]
	]) == 5, "First"
	assert checkio([
		[1, 1, 11, 2, 2],
		[2, 3, 10, 4, 1],
		[3, 5, 9, 6, 3],
		[4, 7, 8, 8, 2]
	]) == 2, "Second"
	assert checkio([
		[1, 1, 3, 3, 6],
		[5, 1, 7, 3, 6],
		[9, 1, 11, 3, 6],
		[1, 4, 3, 6, 6],
		[5, 4, 7, 6, 6],
		[9, 4, 11, 6, 6],
		[1, 7, 11, 8, 3.25]
	]) == 4, "Third"
	assert checkio([
		[0, 0, 1, 1, 10]
	]) == 1, "Alone"
	assert checkio([
		[2, 2, 3, 3, 4],
		[2, 5, 3, 6, 4]
	]) == 1, "Shadow"