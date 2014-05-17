r=lambda c,p,i:p==0 if i<0 else r(c,p//2,i-1) if p%2==c[i].isalpha() else False
check_command=lambda p,c:r(c,p,len(c)-1)

if __name__ == '__main__':
	assert check_command(42, "12a0b3e4") == True, "42 is the answer"
	assert check_command(101, "ab23b4zz") == False, "one hundred plus one"
	assert check_command(0, "478103487120470129") == True, "Any number"
	assert check_command(127, "Checkio") == True, "Uppercase"
	assert check_command(7, "Hello") == False, "Only full match"
	assert check_command(5, "H2O") == True, "Water"
	assert check_command(42, "C2H5OH") == False, "Yep, this is not the Answer"