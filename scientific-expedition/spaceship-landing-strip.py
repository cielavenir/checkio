def checkio(data):
	y=len(data)
	x=len(data[0])
	m=[[0]*x for i in range(y)]
	for j in range(y):
		r=0
		for i in range(x):
			if data[j][i]=='G' or data[j][i]=='S': r+=1
			else: r=0
			m[j][i]=r
	r=0
	for i in range(x):
		for j in range(y):
			M=9999999
			for k in range(j,y):
				M=min(M,m[k][i])
				r=max(r,M*(k-j+1))
	return r

#These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
	assert checkio(['G']) == 1, 'One cell - one variant'
	assert checkio(['GS',
					'GS']) == 4, 'Four good cells'
	assert checkio(['GT',
					'GG']) == 2, 'Four cells, but with a tree'
	assert checkio(['GGTGG',
					'TGGGG',
					'GSSGT',
					'GGGGT',
					'GWGGG',
					'RGTRT',
					'RTGWT',
					'WTWGR']) == 9, 'Classic'