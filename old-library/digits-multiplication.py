def checkio(number):
	r=1
	for e in str(number): r *= 1 if e=='0' else int(e)
	return r

if __name__ == '__main__':
	assert checkio(123405) == 120
	assert checkio(999) == 729
	assert checkio(1000) == 1
	assert checkio(1111) == 1