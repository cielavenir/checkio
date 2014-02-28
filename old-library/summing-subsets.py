import itertools
def checkio(data):
	r=0
	for i in range(1,data+1):
		a=list(range(1,i+1))
		for j in range(1,i+1):
			r+=sum(sum(e) for e in itertools.combinations(a,j))
	return r

#These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
	assert checkio(1) == 1, "First"
	assert checkio(2) == 7, "Second"
	assert checkio(3) == 31, "Third"
	assert checkio(4) == 111, "Fourth"