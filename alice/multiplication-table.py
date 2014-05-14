def bitLen(n):
	l=0
	while n:
		n>>=1
		l+=1
	return l

def checkio(first, second):
	l=bitLen(first)
	n=(1<<bitLen(second))-1
	r=0
	for i in range(l):
		r+=second&(n if (first>>i)&1 else 0)
		r+=second|(n if (first>>i)&1 else 0)
		r+=second^(n if (first>>i)&1 else 0)
	return r

if __name__ == '__main__':
	assert checkio(4, 6) == 38
	assert checkio(2, 7) == 28
	assert checkio(7, 2) == 18