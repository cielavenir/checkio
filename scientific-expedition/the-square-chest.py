def checkio(lines_list):
	M=4
	if any(any(e>16 for e in _) for _ in lines_list): M=5
	h={}
	for p,q in lines_list: h[(min(p,q)-1,max(p,q)-1)]=1
	r=0
	for k in range(1,M):
		for x in range((M-1)-k+1):
			for y in range((M-1)-k+1):
				if all(((y+i)*M+x,(y+i+1)*M+x) in h and (y*M+x+i,y*M+x+i+1) in h and ((y+i)*M+x+k,(y+i+1)*M+x+k) in h and ((y+k)*M+x+i,(y+k)*M+x+i+1) in h for i in range(k)):
					r+=1
	return r

if __name__ == '__main__':
	assert (checkio([[1, 2], [3, 4], [1, 5], [2, 6], [4, 8], [5, 6], [6, 7],
					 [7, 8], [6, 10], [7, 11], [8, 12], [10, 11],
					 [10, 14], [12, 16], [14, 15], [15, 16]]) == 3), "First, from description"
	assert (checkio([[1, 2], [2, 3], [3, 4], [1, 5], [4, 8],
					 [6, 7], [5, 9], [6, 10], [7, 11], [8, 12],
					 [9, 13], [10, 11], [12, 16], [13, 14], [14, 15], [15, 16]]) == 2), "Second, from description"
	assert (checkio([[1, 2], [1, 5], [2, 6], [5, 6]]) == 1), "Third, one small square"
	assert (checkio([[1, 2], [1, 5], [2, 6], [5, 9], [6, 10], [9, 10]]) == 0), "Fourth, it's not square"
	assert (checkio([[16, 15], [16, 12], [15, 11], [11, 10],
					 [10, 14], [14, 13], [13, 9]]) == 0), "Fifth, snake"