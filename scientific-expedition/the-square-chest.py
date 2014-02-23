def checkio(lines_list):
	h={}
	for p,q in lines_list: h[(min(p,q)-1,max(p,q)-1)]=1
	r=0
	for k in range(1,4):
		for x in range(3-k+1):
			for y in range(3-k+1):
				if all(((y+i)*4+x,(y+i+1)*4+x) in h and (y*4+x+i,y*4+x+i+1) in h and ((y+i)*4+x+k,(y+i+1)*4+x+k) in h and ((y+k)*4+x+i,(y+k)*4+x+i+1) in h for i in range(k)):
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