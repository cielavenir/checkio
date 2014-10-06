def golf(z):
	y=list(map(list,z))
	l=range(len(y))
	for k in l:
		for i in l:
			for j in l:
				if y[i][k]*y[k][j]:y[i][j]=min(y[i][j]or 1e9,y[i][k]+y[k][j])
	return y[0][len(y)-1]

if __name__=='__main__':
	assert golf(((0, 80, 58, 0), (80, 0, 71, 80), (58, 71, 0, 58), (0, 80, 58, 0))) == 116