check_line=lambda s:not('XX' in ''.join(s) or 'ZZ' in ''.join(s))

if __name__ == '__main__':
	assert check_line(["X", "Z", "X"]) == True
	assert check_line(["X", "Z", "X", "X"]) == False
	assert check_line(["X", "Z"]) == True
	assert check_line(["Z", "X"]) == True
	assert check_line(["Z", "X", "Z", "X", "Z", "Z", "X"]) == False