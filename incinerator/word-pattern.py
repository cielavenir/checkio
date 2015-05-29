attr={
	2:['isdigit','isalpha'],
	3:['isdigit','islower','isupper'],
	4:['isdigit','islower','isupper','isspace'],
}
def ck(p,ite,n):
	try:
		cur=next(ite)
		return ck(p//n,ite,n) if any(p%n==i and getattr(cur,attr[n][i])() for i in range(n)) else False
	except StopIteration:
		return p==0

def check_command(pattern,command,n=2): return ck(pattern,reversed(command),n)

if __name__ == '__main__':
	assert check_command(42, "12a0b3e4") == True, "42 is the answer"
	assert check_command(101, "ab23b4zz") == False, "one hundred plus one"
	assert check_command(0, "478103487120470129") == True, "Any number"
	assert check_command(127, "Checkio") == True, "Uppercase"
	assert check_command(7, "Hello") == False, "Only full match"
	assert check_command(5, "H2O") == True, "Water"
	assert check_command(42, "C2H5OH") == False, "Yep, this is not the Answer"