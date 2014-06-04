golf=lambda s:min(sum(abs((i and e[i-1])-e[i])for i in range(5))for e in __import__('itertools').permutations(map(complex,*zip(*s))))
#golf=lambda s:min(abs(e[0])+sum(abs(e[i]-e[i+1])for i in range(4))for e in __import__('itertools').permutations(map(complex,*zip(*s))))
#golf=lambda s:min(abs(e[0])+sum(abs(e[i]-e[i+1])for i in range(4))for e in __import__('itertools').permutations([complex(*e)for e in s]))
#golf=lambda s:min(sum(abs(complex(*(e[i-1]if i else(0,0)))-complex(*e[i]))for i in range(5))for e in __import__('itertools').permutations(s))
#golf=lambda s:min(sum(abs(complex(*x)-complex(*y))for x,y in[(((0,0),)+e)[i:i+2]for i in range(5)])for e in __import__('itertools').permutations(s))
#golf=lambda s:min(sum(abs(complex(*x)-complex(*y))for x,y in[(((0,0),)+e)[i:i+2]for i in range(5)])for e in __import__('itertools').permutations(s))
#golf=lambda s:min(sum(abs(complex(*x)-complex(*y)) for x,y in [(((0,0),)+e)[i:i+2] for i in range(len(e))]) for e in __import__('itertools').permutations(list(s)))

if __name__ == '__main__':
	def almost_equal(checked, correct, significant_digits=2):
		precision = 0.1 ** significant_digits
		return correct - precision < checked < correct + precision
	assert almost_equal(golf({(1, 1), (1, 9), (9, 9), (9, 1), (5, 5)}), 28.73)
	assert almost_equal(golf({(2, 2), (2, 8), (8, 8), (8, 2), (5, 5)}), 23.31)
	assert almost_equal(golf({(2, 2), (4, 4), (6, 6), (8, 8), (9, 9)}), 12.73)