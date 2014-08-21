import re
check=lambda a:len(a.group(1))==len(a.group(3))and len(a.group(3))==len(a.group(5))
recognize=lambda n:check(re.search('(1+)(0+)(1+)(0+)(1+)',format(n,'b')))

if __name__ == '__main__':
	assert recognize(21) == True, "First example"
	assert recognize(1587) == True, "Second example"
	assert recognize(3687) == False, "Thid example"