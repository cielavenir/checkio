def convert(code):
	bin_code = bin(code)[2:].zfill(6)[::-1]
	return [[int(bin_code[j + i * 3]) for i in range(2)] for j in range(3)]

LETTERS_NUMBERS = list(map(convert,
	[1, 3, 9, 25, 17, 11, 27, 19, 10, 26, 5, 7, 13, 29, 21, 15, 31, 23, 14, 30, 37, 39, 62, 45, 61, 53]
))
CAPITAL_FORMAT = convert(32)
NUMBER_FORMAT = convert(60)
PUNCTUATION = {e[0]:convert(e[1]) for e in ((' ',0),(',',2),('-',18),('!',22),('_',36),('?',38),('.',50))}
WIDTH=10

def braille_page(s):
	b=[]
	for e in s:
		if e.islower():
			b.append(LETTERS_NUMBERS[ord(e)-ord('a')])
		elif e.isupper():
			b.append(CAPITAL_FORMAT)
			b.append(LETTERS_NUMBERS[ord(e)-ord('A')])
		elif e.isdigit():
			b.append(NUMBER_FORMAT)
			b.append(LETTERS_NUMBERS[9 if e=='0' else ord(e)-ord('1')])
		else:
			b.append(PUNCTUATION[e])
	width=min(WIDTH,len(b))*3-1
	m=[[0]*width for i in range( (len(b)+WIDTH-1)//WIDTH *4-1 )]
	for i,e in enumerate(b):
		for y0 in range(3):
			for x0 in range(2): m[i//WIDTH*4 + y0][i%WIDTH*3 + x0]=e[y0][x0]
	return m

if __name__ == '__main__':
	def checker(func, text, answer):
		result = func(text)
		return answer == tuple(tuple(row) for row in result)
	assert checker(braille_page, "hello 1st World!", (
		(1, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 1, 0, 0, 1),
		(1, 1, 0, 0, 1, 0, 1, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 1, 1),
		(0, 0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 1, 0, 0, 1, 0),
		(0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0),
		(0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0),
		(0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 1, 0, 1, 1, 0, 1, 0, 0, 0, 1, 0, 1, 1, 0, 0, 0, 0, 0, 0),
		(0, 0, 0, 0, 1, 0, 1, 1, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0))
	), "Example"
	assert checker(braille_page, "42", (
		(0, 1, 0, 1, 1, 0, 0, 1, 0, 1, 0),
		(0, 1, 0, 0, 1, 0, 0, 1, 0, 1, 0),
		(1, 1, 0, 0, 0, 0, 1, 1, 0, 0, 0))), "42"
	assert checker(braille_page, "CODE", (
		(0, 0, 0, 1, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 1, 0),
		(0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1),
		(0, 1, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0))
	), "CODE"