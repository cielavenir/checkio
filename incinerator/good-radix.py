def checkio(s):
	r=0
	try:
		for i in range(36,1,-1):
			if int(s,i)%(i-1)==0: r=i
	except ValueError:
		pass
	return r

if __name__ == '__main__':
	assert checkio("18") == 10, "Simple decimal"
	assert checkio("1010101011") == 2, "Any number is divisible by 1"
	assert checkio("222") == 3, "3rd test"
	assert checkio("A23B") == 14, "It's not a hex"
	print('Local tests done')