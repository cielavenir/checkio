def grid(m,I,J):
	f=True
	s=0
	for j in range(M):
		if m[I][j]: s+=m[I][j]
		else: f=False
	if f and s!=S: return False
	f=True
	s=0
	for i in range(M):
		if m[i][J]: s+=m[i][J]
		else: f=False
	if f and s!=S: return False
	return True

def dfs(m,h,n):
	if n==M*M:
		#check diagonal
		if sum(m[i][i] for i in range(M))!=S: return None
		if sum(m[i][M-i-1] for i in range(M))!=S: return None
		return m
	i=n//M
	j=n%M
	if m[i][j]: return dfs(m,h,n+1)
	for k in range(1,M*M+1):
		if k not in h:
			m[i][j]=k
			if grid(m,i,j):
				h[k]=1
				if dfs(m,h,n+1): return m
				del h[k]
	m[i][j]=0
	return None

def checkio(data):
	global M,S
	M=len(data)
	S=M*(M*M+1)//2
	h={}
	for y in range(len(data)):
		for x in range(len(data[0])):
			h[data[y][x]]=1
	return dfs(data,h,0)

#These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
	print(checkio([
		[2, 7, 6],
		[9, 5, 1],
		[4, 3, 0]
	]))
	#must return [[2, 7, 6], [9, 5, 1], [4, 3, 8]]
	print(checkio([
		[0, 0, 0],
		[0, 5, 0],
		[0, 0, 0]
	]))
	#can return [[2, 7, 6], [9, 5, 1], [4, 3, 8]] or
	# [[4, 9, 2], [3, 5, 7], [8, 1, 6]
	print(checkio([[1, 15, 14, 4],
				   [12, 0, 0, 9],
				   [8, 0, 0, 5],
				   [13, 3, 2, 16]]))
	# answer [[1, 15, 14, 4], [12, 6, 7, 9], [8, 10, 11, 5], [13, 3, 2, 16]]