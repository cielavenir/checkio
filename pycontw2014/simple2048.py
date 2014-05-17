#from itertools import groupby
def twoeleven_iterate(iterable,z):
	#squeezed=[e[0] for e in groupby(iterable, key)]
	squeezed=iterable
	i=0
	while i<len(squeezed)-1:
		if squeezed[i]==squeezed[i+1]:
			squeezed=squeezed[:i]+[2*squeezed[i]]+squeezed[i+2:]
		i+=1
	return list(z(squeezed))+[0]*(4-len(squeezed))

def checkio(a, b):
	if b=='up': x=list(map(list,zip(*[twoeleven_iterate([a[j][i] for j in range(4) if a[j][i]!=0],list) for i in range(4)])))
	if b=='down': x=list(map(list,zip(*[list(reversed(twoeleven_iterate([a[j][i] for j in range(4) if a[j][i]!=0],reversed))) for i in range(4)])))
	if b=='right': x=[list(reversed(twoeleven_iterate([a[i][j] for j in range(4) if a[i][j]!=0],reversed))) for i in range(4)]
	if b=='left': x=[twoeleven_iterate([a[i][j] for j in range(4) if a[i][j]!=0],list) for i in range(4)]
	if a==x: return x
	for i in reversed(range(4)):
		for j in reversed(range(4)):
			if x[i][j]==0:
				x[i][j]=2
				return x
	return x

if __name__ == '__main__':
	assert checkio([[0,0,0,0],[0,0,0,0],[0,0,2,0],[0,2,0,0]], 'up') == [[0,2,2,0],[0,0,0,0],[0,0,0,0],[0,0,0,2]] 
	assert checkio([[0,0,0,0],[0,0,0,0],[0,0,0,0],[2,2,2,2]], 'left') == [[0,0,0,0],[0,0,0,0],[0,0,0,0],[4,4,0,2]]
	assert checkio([[0,0,0,0],[0,0,0,0],[0,0,0,0],[4,4,0,2]], 'right') == [[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,2,8,2]]
	print('Done')