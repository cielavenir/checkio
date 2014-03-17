from functools import reduce
import operator
#fact=lambda n: 1 if n==0 else n*fact(n-1)
checkio=lambda data: sum(reduce(operator.mul,range(1,int(e)+1),1) for e in iter(str(data)))
	
if __name__ == '__main__':
	assert checkio(100) == 3, 'First'
	assert checkio(222) == 6, 'Second'
	assert checkio(1234) == 33, 'Third'
	print('All ok')