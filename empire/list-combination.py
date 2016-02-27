from functools import reduce
import operator
def list_combination(*data):return reduce(operator.add,(list(e) for e in zip(*data)))

if __name__ == '__main__':
	assert list_combination([1, 2, 3], [4, 5, 6]) == [1, 4, 2, 5, 3, 6], "First"
	assert list_combination([1, 1, 1, 1], [2, 2, 2, 2]) == [1, 2, 1, 2, 1, 2, 1, 2], "Second"
	print("All set? Click \"Check\" to review your code and earn rewards!")