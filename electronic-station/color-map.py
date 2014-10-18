from collections import defaultdict

def links(_a,_b):
	for a in _a:
		for b in _b:
			minx=min(a[0],b[0])
			maxx=max(a[0],b[0])
			miny=min(a[1],b[1])
			maxy=max(a[1],b[1])
			#manhattan==1
			if (maxx-minx)+(maxy-miny)==1: return True
	return False

def dfs(linkage,result,d,n):
	if d==n:
		yield result
	else:
		for i in range(1,5):
			if all(result[e]!=i for e in linkage[d] if e<d):
				for e in dfs(linkage,result+[i],d+1,n): yield e

def color_map(m):
	n=0
	a=defaultdict(set) # a[country] => set of (x,y)
	for y in range(len(m)):
		for x in range(len(m[y])):
			n=max(n,m[y][x]+1)
			a[m[y][x]].add((x,y))
	linkage=defaultdict(list)
	for i in range(n):
		for j in range(i+1,n):
			if links(a[i],a[j]):
				linkage[i].append(j)
				linkage[j].append(i)
	return next(e for e in dfs(linkage,[1],1,n))

if __name__ == '__main__':
	NEIGHS = ((-1, 0), (1, 0), (0, 1), (0, -1))
	COLORS = (1, 2, 3, 4)
	ERROR_NOT_FOUND = "Didn't find a color for the country {}"
	ERROR_WRONG_COLOR = "I don't know about the color {}"
	def checker(func, region):
		user_result = func(region)
		if not isinstance(user_result, (tuple, list)):
			print("The result must be a tuple or a list")
			return False
		country_set = set()
		for i, row in enumerate(region):
			for j, cell in enumerate(row):
				country_set.add(cell)
				neighbours = []
				if j < len(row) - 1:
					neighbours.append(region[i][j + 1])
				if i < len(region) - 1:
					neighbours.append(region[i + 1][j])
				try:
					cell_color = user_result[cell]
				except IndexError:
					print(ERROR_NOT_FOUND.format(cell))
					return False
				if cell_color not in COLORS:
					print(ERROR_WRONG_COLOR.format(cell_color))
					return False
				for n in neighbours:
					try:
						n_color = user_result[n]
					except IndexError:
						print(ERROR_NOT_FOUND.format(n))
						return False
					if cell != n and cell_color == n_color:
						print("Same color neighbours.")
						return False
		if len(country_set) != len(user_result):
			print("Excess colors in the result")
			return False
		return True
	assert checker(color_map,[
		[11, 0, 0, 0, 0, 0, 7, 0],
		[0, 0, 0, 0, 0, 0, 7, 0],
		[0, 0, 4, 4, 4, 0, 7, 0],
		[0, 0, 0, 0, 0, 0, 0, 0],
		[0, 0, 1, 0, 1, 0, 0, 0],
		[5, 5, 1, 2, 1, 6, 6, 0],
		[0, 0, 1, 0, 1, 0, 0, 0],
		[0, 0, 0, 0, 0, 0, 0, 0],
		[0, 0, 3, 3, 3, 0, 8, 0],
		[0, 0, 10, 10, 9, 0, 8, 0],
		[0, 0, 0, 10, 9, 9, 8, 0],
	])