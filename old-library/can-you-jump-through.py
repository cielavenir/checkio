def dfs(data,x,y,xg,yg,c):
	if y<0 or len(data)<=y or x<0 or len(data[0])<=x or data[y][x]!=c: return False
	if x==xg and y==yg: return True
	data[y][x]=-1
	if dfs(data,x,y-1,xg,yg,c): return True
	if dfs(data,x-1,y,xg,yg,c): return True
	if dfs(data,x+1,y,xg,yg,c): return True
	if dfs(data,x,y+1,xg,yg,c): return True
	data[y][x]=c
	return False

dfs_=lambda data,x,y,xg,yg:dfs(data,x,y,xg,yg,data[y][x])

can_pass=lambda data,first,second: dfs_(list(map(list,data)),first[1],first[0],second[1],second[0])
#old library can-you-jump-through compatibility
checkio=lambda data: dfs_(data[0],data[1][1]-1,data[1][0]-1,data[2][1]-1,data[2][0]-1,)

if __name__ == '__main__':
	assert checkio(([
		[0, 0, 5, 4, 0],
		[0, 1, 5, 0, 0],
		[0, 0, 0, 7, 2],
		[8, 0, 0, 0, 0],
		[0, 9, 0, 1, 0]],
		[1, 1], [5, 5])) == True, 'First example'
	assert checkio([[
		[0, 0, 5, 4, 0],
		[0, 0, 5, 0, 0],
		[0, 0, 0, 7, 2],
		[8, 0, 0, 4, 0],
		[0, 9, 0, 1, 0]],
		[1,1], [1,5]]) == False, 'Second example'
	assert can_pass(((0, 0, 0, 0, 0, 0),
					 (0, 2, 2, 2, 3, 2),
					 (0, 2, 0, 0, 0, 2),
					 (0, 2, 0, 2, 0, 2),
					 (0, 2, 2, 2, 0, 2),
					 (0, 0, 0, 0, 0, 2),
					 (2, 2, 2, 2, 2, 2),),
					(3, 2), (0, 5)) == True, 'First example'
	assert can_pass(((0, 0, 0, 0, 0, 0),
					 (0, 2, 2, 2, 3, 2),
					 (0, 2, 0, 0, 0, 2),
					 (0, 2, 0, 2, 0, 2),
					 (0, 2, 2, 2, 0, 2),
					 (0, 0, 0, 0, 0, 2),
					 (2, 2, 2, 2, 2, 2),),
					(3, 3), (6, 0)) == False, 'First example'