import re
def checkio(expression):
	expression=re.sub(r'[^0-9-+\*/]','',expression)
	expression=re.sub(r'-','Z',expression)
	while True:
		m=re.match(r'(.*[+Z*/])(-?\d+)([+Z])(-?\d+)(.*)',expression)
		if not m:
			m=re.match(r'()(-?\d+)([+Z])(-?\d+)(.*)',expression)
			if not m: break
		if m.group(3)=='+':
			expression=m.group(1)+str(int(m.group(4))+int(m.group(2)))+m.group(5)
		else:
			expression=m.group(1)+str(int(m.group(4))-int(m.group(2)))+m.group(5)
	while True:
		m=re.match(r'(.*[+Z*/])(-?\d+)([*/])(-?\d+)(.*)',expression)
		if not m:
			m=re.match(r'()(-?\d+)([*/])(-?\d+)(.*)$',expression)
			if not m: break
		if not m: break
		if m.group(3)=='*':
			expression=m.group(1)+str(int(m.group(4))*int(m.group(2)))+m.group(5)
		else:
			d=0
			try:
				d=int(m.group(4))//int(m.group(2))
			except ZeroDivisionError:
				pass
			expression=m.group(1)+str(d)+m.group(5)
	return int(expression)

if __name__ == '__main__':
	assert checkio("2 + 2") == 4, "2+2=4"
	assert checkio("2 * 2") == 4, "2*2=4"
	assert checkio("2 + 2 * 2") == 8, "Yes, it is 8"
	assert checkio("1 - 2 - 3") == 0, "Right to left"
	assert checkio("3 - 2 - 1") == -4, "Again, right to left"
	assert checkio("4 / 8") == 2, "For divide, too"
	assert checkio("2 / 5") == 2, "Don't forget about floor result"
	assert checkio("0 / 10") == 0, "Divide by zero"
	assert checkio("1+1*1+1") == 4, "It is four"
	assert checkio("(3*2)+(4*2)") == 36, "Ignore brackets"
	assert checkio("asd4 + 86() )+( a56d :)") == 146, "Ignore All"
	assert checkio("4 + 8 / 6 * 3 - 33") == 15, "Right to left and operator priority"
	assert checkio("3 - 3 / 10") == 0, "Reduce and zero"
	assert checkio("((2 - 4) - (6 / 8)) + (4 * 6)") == 0, "Complex"
	assert checkio("4 / 2 * 2 + ((3 - 3) / 15)") == 3, "Complex 2"