M=3
def grid(m,I,J):
	z=[0]*(M*M+1)
	for j in range(M*M):
		if m[I][j]: z[m[I][j]]+=1
		if z[m[I][j]]>1: return False
	z=[0]*(M*M+1)
	for i in range(M*M):
		if m[i][J]: z[m[i][J]]+=1
		if z[m[i][J]]>1: return False
	i=I//M+J//M*M
	z=[0]*(M*M+1)
	for j in range(M*M):
		x=i%M*M+j//M
		y=i//M*M+j%M
		if m[x][y]: z[m[x][y]]+=1
		if z[m[x][y]]>1: return False
	return True

def dfs(m,n):
	if n==M*M*M*M: return m
	i=n//(M*M)
	j=n%(M*M)
	if m[i][j]: return dfs(m,n+1)
	for k in range(1,M*M+1):
		m[i][j]=k
		if grid(m,i,j) and dfs(m,n+1): return m
	m[i][j]=0
	return None

checkio=lambda m: dfs(m,0)

#These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
	assert checkio([[0, 7, 1, 6, 8, 4, 0, 0, 0],
					[0, 4, 9, 7, 0, 0, 0, 0, 0],
					[5, 0, 0, 0, 0, 0, 0, 0, 0],
					[0, 8, 0, 0, 0, 0, 5, 0, 4],
					[0, 0, 0, 3, 0, 7, 0, 0, 0],
					[2, 0, 3, 0, 0, 0, 0, 9, 0],
					[0, 0, 0, 0, 0, 0, 0, 0, 9],
					[0, 0, 0, 0, 0, 3, 7, 2, 0],
					[0, 0, 0, 4, 9, 8, 6, 1, 0]]) == [[3, 7, 1, 6, 8, 4, 9, 5, 2],
													  [8, 4, 9, 7, 2, 5, 3, 6, 1],
													  [5, 6, 2, 9, 3, 1, 4, 7, 8],
													  [6, 8, 7, 2, 1, 9, 5, 3, 4],
													  [9, 1, 4, 3, 5, 7, 2, 8, 6],
													  [2, 5, 3, 8, 4, 6, 1, 9, 7],
													  [1, 3, 6, 5, 7, 2, 8, 4, 9],
													  [4, 9, 8, 1, 6, 3, 7, 2, 5],
													  [7, 2, 5, 4, 9, 8, 6, 1, 3]], "first"
	assert checkio([[5, 0, 0, 7, 1, 9, 0, 0, 4],
					[0, 0, 1, 0, 3, 0, 5, 0, 0],
					[0, 0, 0, 0, 0, 0, 0, 0, 0],
					[0, 8, 5, 9, 7, 2, 6, 4, 0],
					[0, 0, 0, 6, 0, 1, 0, 0, 0],
					[0, 2, 6, 3, 8, 5, 9, 1, 0],
					[0, 0, 0, 0, 0, 0, 0, 0, 0],
					[0, 0, 3, 0, 5, 0, 2, 0, 0],
					[8, 0, 0, 4, 9, 7, 0, 0, 6]]) == [[5, 6, 8, 7, 1, 9, 3, 2, 4],
													  [9, 7, 1, 2, 3, 4, 5, 6, 8],
													  [2, 3, 4, 5, 6, 8, 7, 9, 1],
													  [1, 8, 5, 9, 7, 2, 6, 4, 3],
													  [3, 9, 7, 6, 4, 1, 8, 5, 2],
													  [4, 2, 6, 3, 8, 5, 9, 1, 7],
													  [6, 1, 9, 8, 2, 3, 4, 7, 5],
													  [7, 4, 3, 1, 5, 6, 2, 8, 9],
													  [8, 5, 2, 4, 9, 7, 1, 3, 6]], "second"