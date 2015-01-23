def chk(grid,x,y,n):
	siz=2*(n-1)+1
	for i in range(-n,n+1):
		a=[0] if i==-n or i==n else [0]+[1]*(2*(n-abs(i)-1)+1)+[0]
		start_point=x-len(a)//2
		for j in range(len(a)):
			if 0<=y+i<len(grid) and 0<=start_point+j<len(grid[0]) and grid[y+i][start_point+j]!=a[j]: return False
	return True

def healthy(grid):
	result=(0,0)
	n=2
	while n-1<=min(len(grid)-n,len(grid[0])-n):
		for i in range(n-1,len(grid[0])-n+1):
			for j in range(n-1,len(grid)-n+1):
				if chk(grid,i,j,n): result=(j,i)
		n+=1
	return result

if __name__ == '__main__':
	def check(result, answers):
		return list(result) in answers
	assert check(healthy(((0, 1, 0),
				 		  (1, 1, 1),
						  (0, 1, 0),)), [[1, 1]])
	assert check(healthy(((0, 0, 1, 0, 0),
						   (0, 1, 1, 1, 0),
						   (0, 0, 1, 0, 0),
						   (0, 0, 0, 0, 0),
						   (0, 0, 1, 0, 0),)), [[1, 2]])
	assert check(healthy(((0, 0, 1, 0, 0),
						   (0, 1, 1, 1, 0),
						   (0, 0, 1, 0, 0),
						   (0, 0, 1, 0, 0),
						   (0, 0, 1, 0, 0),)), [[0, 0]])
	assert check(healthy(((0, 0, 0, 0, 0, 0, 1, 0),
						   (0, 0, 1, 0, 0, 1, 1, 1),
						   (0, 1, 1, 1, 0, 0, 1, 0),
						   (1, 1, 1, 1, 1, 0, 0, 0),
						   (0, 1, 1, 1, 0, 0, 1, 0),
						   (0, 0, 1, 0, 0, 1, 1, 1),
						   (0, 0, 0, 0, 0, 0, 1, 0),)), [[3, 2]])
	assert check(healthy(((0, 0, 0, 0, 0, 0, 2, 0),
						   (0, 0, 0, 2, 2, 2, 2, 2),
						   (0, 0, 1, 0, 0, 0, 2, 0),
						   (0, 1, 1, 1, 0, 0, 2, 0),
						   (1, 1, 1, 1, 1, 0, 2, 0),
						   (0, 1, 1, 1, 0, 0, 2, 0),
						   (0, 0, 1, 0, 0, 0, 2, 0),
						   (0, 0, 0, 1, 0, 0, 2, 0),
						   (0, 0, 1, 1, 1, 0, 2, 0),
						   (0, 1, 1, 1, 1, 1, 0, 0),
						   (0, 0, 1, 1, 1, 0, 0, 0),
						   (0, 0, 0, 1, 0, 0, 0, 0),)), [[4, 2], [9, 3]])