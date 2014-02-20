from functools import reduce
checkio=lambda data: reduce(lambda x,y:x+y,data)

if __name__ == '__main__':
	assert checkio([5, 5]) == 10, 'First'
	assert checkio([7, 1]) == 8, 'Second'
	print('All ok')