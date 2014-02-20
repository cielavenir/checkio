def dfs(data,x,y,c):
	if y<0 or len(data)<=y or x<0 or len(data[0])<=x or data[y][x]!=c: return 0
	data[y][x]=0
	return 1+dfs(data,x,y-1,c)+dfs(data,x-1,y,c)+dfs(data,x+1,y,c)+dfs(data,x,y+1,c)

def checkio(data):
	r=[]
	for y in range(len(data)):
		for x in range(len(data[0])):
			if data[y][x]!=0:
				c=data[y][x]
				r.append([dfs(data,x,y,c),c])
	return max(r)

#These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
	assert checkio([
		[1, 2, 3, 4, 5],
		[1, 1, 1, 2, 3],
		[1, 1, 1, 2, 2],
		[1, 2, 2, 2, 1],
		[1, 1, 1, 1, 1]
	]) == [14, 1], '14 of 1'
	assert checkio([
		[2, 1, 2, 2, 2, 4],
		[2, 5, 2, 2, 2, 2],
		[2, 5, 4, 2, 2, 2],
		[2, 5, 2, 2, 4, 2],
		[2, 4, 2, 2, 2, 2],
		[2, 2, 4, 4, 2, 2]
	]) == [19, 2], '19 of 2'