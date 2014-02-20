from functools import reduce

def checkio(data):
	for i in range(999999):
		n=reduce(lambda x,y: x*y,[int(e) for e in str(i)])
		if n==data: return i
	return 0

#These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
	assert checkio(20) == 45, "1st example"
	assert checkio(21) == 37, "2nd example"
	assert checkio(17) == 0, "3rd example"
	assert checkio(33) == 0, "4th example"
	assert checkio(5) == 5, "5th example"