from itertools import permutations

def dfs(z,a,b,d,s):
	if d==5: return s if b[1]==a[0] else 0
	return max([0]+[dfs(z,a,c,d+1,s+c[2]) for c in permutations(z[d]) if b[1]==c[0]])

def checkio(chips):
	r=0
	for z in permutations(chips[1:]):
		for a in permutations(chips[0]):
			r=max(r,dfs(z,a,a,0,a[2]))
	return r

#These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
	assert checkio(
		[[1, 4, 20], [3, 1, 5], [50, 2, 3],
		 [5, 2, 7], [7, 5, 20], [4, 7, 50]]) == 152, "First"
	assert checkio(
		[[1, 10, 2], [2, 20, 3], [3, 30, 4],
		 [4, 40, 5], [5, 50, 6], [6, 60, 1]]) == 210, "Second"
	assert checkio(
		[[1, 2, 3], [2, 1, 3], [4, 5, 6],
		 [6, 5, 4], [5, 1, 2], [6, 4, 3]]) == 21, "Third"
	assert checkio(
		[[5, 9, 5], [9, 6, 9], [6, 7, 6],
		 [7, 8, 7], [8, 1, 8], [1, 2, 1]]) == 0, "Fourth"