def dfs(data,x,y,xg,yg):
	if y<0 or len(data)<=y or x<0 or len(data[0])<=x or data[y][x]!=0: return False
	if x==xg and y==yg: return True
	data[y][x]=1
	if dfs(data,x,y-1,xg,yg): return True
	if dfs(data,x-1,y,xg,yg): return True
	if dfs(data,x+1,y,xg,yg): return True
	if dfs(data,x,y+1,xg,yg): return True
	data[y][x]=0
	return False

checkio=lambda data: dfs(data[0],data[1][1]-1,data[1][0]-1,data[2][1]-1,data[2][0]-1)

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