import itertools
golf=lambda s: min(sum(abs(complex(*x)-complex(*y)) for x,y in [(((0,0),)+e)[i:i+2] for i in range(len(e))]) for e in itertools.permutations(list(s)))

#def golf(s):
#	r=min(sum(abs(complex(*x)-complex(*y)) for x,y in [(((0,0),)+e)[i:i+2] for i in range(len(e))]) for e in itertools.permutations(list(s)))
#	print(r)
#	return r

if __name__ == '__main__':
	def almost_equal(checked, correct, significant_digits=2):
		precision = 0.1 ** significant_digits
		return correct - precision < checked < correct + precision
	assert almost_equal(golf({(1, 1), (1, 9),
                      (9, 9), (9, 1), (5, 5)}), 28.73), "First"
	assert almost_equal(golf({(1, 1), (1, 5), (1, 9),
			(5, 9), (9, 9), (9, 5),
			(9, 1), (5, 1), (5, 5)}), 33.47), "First"