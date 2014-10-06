def golf(z):
	y=[list(e)for e in z]
	l=len(y)
	for k in range(l):
		for i in range(l):
			for j in range(l):
				if i!=j and y[i][k] and y[j][k] and (y[i][j]==0 or y[i][j]>y[i][k]+y[k][j]):
					y[i][j]=y[i][k]+y[k][j]
	return y[0][l-1]

if __name__=='__main__':
	assert golf(((0, 80, 58, 0), (80, 0, 71, 80), (58, 71, 0, 58), (0, 80, 58, 0))) == 116