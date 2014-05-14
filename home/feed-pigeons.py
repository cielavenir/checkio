import itertools
def checkio(number):
	pigeon=0
	for i in itertools.count(1):
		pigeon+=i
		if number<pigeon:
			return max(number,pigeon-i)
		number-=pigeon

if __name__ == '__main__':
	assert checkio(1) == 1, "1st example"
	assert checkio(2) == 1, "2nd example"
	assert checkio(5) == 3, "3rd example"
	assert checkio(10) == 6, "4th example"