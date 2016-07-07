#checkio=lambda x:round(__import__('numpy').linalg.det(x))

checkio=lambda l: 0 if len(l)<1 else l[0][0] if len(l)==1 else l[0][0]*l[1][1]-l[0][1]*l[1][0] if len(l)==2 else sum((-1)**t*l[0][t]*checkio([[l[u+1][m] for m in range(len(l)) if m!=t] for u in range(len(l)-1)]) for t in range(len(l)))

'''
def checkio(l):
	n=len(l)
	if n<1: return 0
	elif n==1: return l[0][0]
	elif n==2: return l[0][0]*l[1][1]-l[0][1]*l[1][0]
	else:
		i=1
		sum=0
		for t in range(n):
			d=[[l[u+1][m] for m in range(n) if m!=t] for u in range(n-1)]
			sum=sum+i*l[0][t]*checkio(d)
			i*=-1
		return sum
'''

if __name__ == '__main__':
	assert checkio([[4, 3], [6, 3]]) == -6, 'First example'
	assert checkio([[1, 3, 2],
					[1, 1, 4],
					[2, 2, 1]]) == 14, 'Second example'