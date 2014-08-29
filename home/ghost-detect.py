import re
check=lambda a:all(len(a.group(i))==len(a.group(i+2))for i in(1,3))
recognize=lambda n:check(re.search('(1+)(0+)(1+)(0+)(1+)',format(n,'b')))

if __name__ == '__main__':
	assert recognize(21) == True, "First example"
	assert recognize(1587) == True, "Second example"
	assert recognize(3687) == False, "Thid example"