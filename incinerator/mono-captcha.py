font = [
	"0110001001110111010101110011011101110011",
	"0101011000010001010101000100000101010101",
	"0101001000110010011101100111001001110111",
	"0101001001000001000100010101010001010001",
	"0011001001110111000101100011010001110110",
]
font_matrix=[[font[y][x*4+1:x*4+4] for x in range(len(font[y])//4)] for y in range(len(font))]
font_tr=[list(e) for e in zip(*font_matrix)]
font_joined=[''.join(e) for e in font_tr]

diff=lambda t,s: sum(t[i]!=s[i] for i in range(len(t)))

def checkio(image):
	matrix=[[image[y][x*4+1:x*4+4] for x in range(len(image[y])//4)] for y in range(len(image))]
	tr=[list(e) for e in zip(*matrix)]
	joined=[''.join(''.join(str(g) for g in f) for f in e) for e in tr]
	r=''
	for e in joined:
		for i,f in enumerate(font_joined):
			if diff(e,f)<2:
				r+=str(i)
				break
	return int(r)

#These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
	assert checkio([[0, 1, 1, 1, 0, 0, 1, 1, 0, 1, 0, 1, 0],
					[0, 0, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0],
					[0, 0, 1, 0, 0, 1, 1, 1, 0, 1, 1, 1, 0],
					[0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 1, 0],
					[0, 1, 1, 1, 0, 1, 1, 0, 0, 0, 0, 1, 0]]) == 394, "394 clear"
	assert checkio([[0, 1, 1, 1, 0, 0, 1, 1, 0, 1, 1, 1, 0],
					[0, 0, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0],
					[0, 0, 1, 0, 0, 1, 1, 1, 0, 1, 1, 1, 0],
					[0, 1, 0, 1, 0, 1, 0, 1, 0, 0, 0, 1, 0],
					[0, 1, 1, 1, 0, 1, 1, 0, 0, 0, 0, 1, 0]]) == 394, "again 394 but with noise"