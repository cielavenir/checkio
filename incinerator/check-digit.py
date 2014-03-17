from functools import reduce
import re,operator

def checkio(data):
	t=re.sub(r'[^0-9A-Z]','',data[::-1])
	s=0
	for i,e in enumerate(t):
		if e.isupper(): e=ord(e)-48
		else: e=int(e)
		s += e if i%2==1 else reduce(operator.add, [int(f) for f in str(e*2)])
	return [str(10-((s-1)%10+1)),s]

#These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
	assert (checkio("799 273 9871") == ["3", 67]), "First Test"
	assert (checkio("139-MT") == ["8", 52]), "Second Test"
	assert (checkio("123") == ["0", 10]), "Test for zero"
	assert (checkio("999_999") == ["6", 54]), "Third Test"
	assert (checkio("+61 820 9231 55") == ["3", 37]), "Fourth Test"
	assert (checkio("VQ/WEWF/NY/8U") == ["9", 201]), "Fifth Test"
	print("OK, done!")