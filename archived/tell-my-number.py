def checkio(a):
	if not a or len(a)==0: return None
	ret=0
	m=1
	for i in range(len(a)): m*=a[i][1]
	for i in range(len(a)):
		p=a[i][1]
		q=m/p
		s=0
		while s%p!=1: s+=q
		ret+=s*a[i][0]
	return ret%m

if __name__ == '__main__':
	assert (checkio([(2, 3), (3, 5), (2, 7)]) == 23), "First Test"
	assert (checkio([(1, 5), (4, 7)]) == 11), "Second Test"
	assert (checkio([(1, 3), (2, 5), (3, 7)]) == 52), "Third Test"
	assert (checkio([(1, 2), (1, 3), (1, 5)]) == 1), "Fourth Test"
	assert (checkio([(2, 4), (7, 9)]) == 34), "Fifth Test"
	print('All done!')