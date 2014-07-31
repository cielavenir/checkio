from __future__ import division
chase=lambda a,b,c:a*c/(a-b)

if __name__=='__main__':
	def almost_equal(checked, correct, significant_digits):
		precision = 0.1 ** significant_digits
		return correct - precision < checked < correct + precision
	assert almost_equal(chase(6, 3, 2), 4, 8), "example"
	assert almost_equal(chase(10, 1, 10), 11.111111111, 8), "long number"
	assert almost_equal(chase(2, 1, 1), 2, 8)
	assert almost_equal(chase(15, 13, 56), 420, 8)