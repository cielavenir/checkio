def dfs(data,x,y):
	if y<0 or len(data)<=y or x<0 or len(data[0])<=x or data[y][x]==1: return 0
	data[y][x]=1
	return 1+dfs(data,x,y-1)+dfs(data,x-1,y)+dfs(data,x+1,y)+dfs(data,x,y+1)

def checkio(data):
	r=[]
	for y in range(len(data)):
		for x in range(len(data[0])):
			if data[y][x]==0:
				r.append(dfs(data,x,y))
	return sorted(r)

if __name__ == '__main__':
	assert checkio([[0,0,0,0,1,0,1,0,0],
					[0,0,0,1,1,0,1,0,0],
					[0,0,0,1,0,0,1,0,0],
					[0,0,1,1,1,1,1,1,1],
					[1,1,1,0,1,1,0,1,0],
					[0,0,1,0,1,1,0,1,0],
					[0,0,1,0,0,0,0,1,0],
					[0,0,1,1,1,1,1,1,0],
					[0,0,0,0,0,0,0,1,0]]) == [4,5,6,8,12,13]
	print('Done')