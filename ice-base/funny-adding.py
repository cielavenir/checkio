from functools import reduce
import operator
checkio=lambda data: reduce(operator.add,data)

if __name__ == '__main__':
	assert checkio([5, 5]) == 10, 'First'
	assert checkio([7, 1]) == 8, 'Second'
	print('All ok')