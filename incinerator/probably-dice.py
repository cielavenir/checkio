#import itertools
def probability(n, s, t):
	a=[0]*(s*(n+1)+1)
	for i in range(1,s+1):
		a[i+s]=1.0/s**n
	for e in range(n-1):
		for i in reversed(range(0,s*n+1)):
			a[i+s]=sum(a[i:i+s])
	#r=sum(1<=t-sum(a)<=s for a in itertools.product(list(range(1,s+1)),repeat=n-1))
	try:
		return a[t+s]
	except IndexError:
		return 0

if __name__ == '__main__':
	def almost_equal(checked, correct, significant_digits=4):
		precision = 0.1 ** significant_digits
		return correct - precision < checked < correct + precision
	assert(almost_equal(probability(2, 6, 3), 0.0556))
	assert(almost_equal(probability(2, 6, 4), 0.0833))
	assert(almost_equal(probability(2, 6, 7), 0.1667))
	assert(almost_equal(probability(2, 3, 5), 0.2222))
	assert(almost_equal(probability(2, 3, 7), 0.0000))
	assert(almost_equal(probability(3, 6, 7), 0.0694))
	assert(almost_equal(probability(10, 10, 50), 0.0375))