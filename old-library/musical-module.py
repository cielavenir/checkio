gcd=lambda a,b: a if b==0 else gcd(b,a%b)
checkio=lambda data: gcd(data[0],data[1])

if __name__ == '__main__':
	assert checkio((12, 8)) == 4, "First example"
	assert checkio((14, 21)) == 7, "Second example"
	assert checkio((13, 11)) == 1, "Third example"