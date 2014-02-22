def checkio(a,b):
	r=0
	for i in range(32):
		if (a>>i)&1 != (b>>i)&1: r+=1
	return r

#These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
	assert checkio(117, 17) == 3, "First example"
	assert checkio(1, 2) == 2, "Second example"
	assert checkio(16, 15) == 5, "Third example"