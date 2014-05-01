import random
def checkio(n, s, t, b):
	_t=200000
	_s=0
	for _i in range(_t):
		turn=0
		cur=0
		while cur!=t:
			cur=(cur+sum(random.randint(1,s) for z in range(n)))%len(b)
			cur=(cur+b[cur]+len(b))%len(b)
			turn+=1
		_s+=turn
	print(_s*1.0/_t)
	return _s*1.0/_t

if __name__ == '__main__':
	#These are only used for self-checking and are not necessary for auto-testing
	def almost_equal(checked, correct, significant_digits=1):
		precision = 0.1 ** significant_digits
		return correct - precision < checked < correct + precision
	assert(almost_equal(checkio(1, 4, 3, [0, 0, 0, 0]), 4.0))
	assert(almost_equal(checkio(1, 4, 1, [0, 0, 0, 0]), 4.0))
	assert(almost_equal(checkio(1, 4, 3, [0, 2, 1, 0]), 1.3))
	assert(almost_equal(checkio(1, 4, 3, [0, -1, -2, 0]), 4.0))
	assert(almost_equal(checkio(1, 6, 1, [0] * 10), 8.6))
	assert(almost_equal(checkio(2, 6, 1, [0] * 10), 10.2))