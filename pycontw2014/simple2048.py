#from itertools import groupby
def twoeleven_iterate(iterable,z):
	#squeezed=[e[0] for e in groupby(iterable, key)]
	squeezed=list(z(iterable))
	i=0
	while i<len(squeezed)-1:
		if squeezed[i]==squeezed[i+1]:
			squeezed=squeezed[:i]+[2*squeezed[i]]+squeezed[i+2:]
		i+=1
	return squeezed+[0]*(4-len(squeezed))

def move2048(a, b):
	if b=='up': x=list(map(list,zip(*[twoeleven_iterate([a[j][i] for j in range(4) if a[j][i]!=0],list) for i in range(4)])))
	if b=='down': x=list(map(list,zip(*[list(reversed(twoeleven_iterate([a[j][i] for j in range(4) if a[j][i]!=0],reversed))) for i in range(4)])))
	if b=='right': x=[list(reversed(twoeleven_iterate([a[i][j] for j in range(4) if a[i][j]!=0],reversed))) for i in range(4)]
	if b=='left': x=[twoeleven_iterate([a[i][j] for j in range(4) if a[i][j]!=0],list) for i in range(4)]
	for i in range(4):
		if any(x[i][j]==2048 for j in range(4)):
			return [['U','W','I','N']]*4
	for i in reversed(range(4)):
		for j in reversed(range(4)):
			if x[i][j]==0:
				x[i][j]=2
				return x
	return [['G','A','M','E'],['O','V','E','R']]*2

if __name__ == '__main__':
	assert move2048([[0,0,0,0],[0,0,0,0],[0,0,2,0],[0,2,0,0]], 'up') == [[0,2,2,0],[0,0,0,0],[0,0,0,0],[0,0,0,2]] 
	assert move2048([[0,0,0,0],[0,0,0,0],[0,0,0,0],[2,2,2,2]], 'left') == [[0,0,0,0],[0,0,0,0],[0,0,0,0],[4,4,0,2]]
	assert move2048([[0,0,0,0],[0,0,0,0],[0,0,0,0],[4,4,0,2]], 'right') == [[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,2,8,2]]
	print('Done')