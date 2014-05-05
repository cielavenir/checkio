from itertools import permutations
def checkio(crossword, words):
	for e in permutations(words):
		if e[3][0]!=e[0][0] or e[3][2]!=e[1][0] or e[3][4]!=e[2][0] or e[4][0]!=e[0][2] or e[4][2]!=e[1][2] or e[4][4]!=e[2][2] or e[5][0]!=e[0][4] or e[5][2]!=e[1][4] or e[5][4]!=e[2][4]: continue
		a=[[' ']*5 for i in range(5)]
		a[0][0]=e[0][0]
		a[0][1]=e[0][1]
		a[0][2]=e[0][2]
		a[0][3]=e[0][3]
		a[0][4]=e[0][4]
		a[1][0]=e[3][1]
		a[1][2]=e[4][1]
		a[1][4]=e[5][1]
		a[2][0]=e[1][0]
		a[2][1]=e[1][1]
		a[2][2]=e[1][2]
		a[2][3]=e[1][3]
		a[2][4]=e[1][4]
		a[3][0]=e[3][3]
		a[3][2]=e[4][3]
		a[3][4]=e[5][3]
		a[4][0]=e[2][0]
		a[4][1]=e[2][1]
		a[4][2]=e[2][2]
		a[4][3]=e[2][3]
		a[4][4]=e[2][4]
		h={}
		for y in range(5):
			for x in range(5):
				if y not in [1,3] and x not in [1,3]:
					if crossword[y][x] not in h:
						h[crossword[y][x]]=a[y][x]
					elif h[crossword[y][x]]!=a[y][x]:
						break
			else: continue
			break
		else: return a
	return None

if __name__ == '__main__':
	assert checkio(
		[
			[21, 6, 25, 25, 17],
			[14, 0, 6, 0, 2],
			[1, 11, 16, 1, 17],
			[11, 0, 16, 0, 5],
			[26, 3, 14, 20, 6]
		],
		['hello', 'habit', 'lemma', 'ozone', 'bimbo', 'trace']) == [['h', 'e', 'l', 'l', 'o'],
																	['a', ' ', 'e', ' ', 'z'],
																	['b', 'i', 'm', 'b', 'o'],
																	['i', ' ', 'm', ' ', 'n'],
																	['t', 'r', 'a', 'c', 'e']]