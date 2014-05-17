import itertools
def checkio(string):
	a=string.split()
	s=a[0]+'+'+a[1]+'=='+a[2]
	head=a[0][0]+a[1][0]+a[2][0]
	a=list(set(''.join(a)))
	for e in itertools.permutations(range(0,10),len(a)):
		d=dict(zip(a,map(str,e)))
		if any(d[e]=='0' for e in head): continue
		expr=''.join(d.get(f,f) for f in s)
		if eval(expr): return True
	return False

if __name__ == '__main__':
	assert checkio("SEND MORE MONEY")==True
	assert checkio("GET LESS JOBS")==True
	print('Done')