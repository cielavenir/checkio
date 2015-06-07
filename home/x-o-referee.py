b=lambda s,c: ((s[0]==c and s[1]==c and s[2]==c)or(s[3]==c and s[4]==c and s[5]==c)or(s[6]==c and s[7]==c and s[8]==c)or(s[0]==c and s[3]==c and s[6]==c)or(s[1]==c and s[4]==c and s[7]==c)or(s[2]==c and s[5]==c and s[8]==c)or(s[0]==c and s[4]==c and s[8]==c)or(s[2]==c and s[4]==c and s[6]==c))
solve=lambda game_result: b(game_result,'X')*2|b(game_result,'O')

def checkio(game_result):
	r=0
	for y in range(len(game_result)-2):
		for x in range(len(game_result[y])-2):
			r|=solve(''.join(e[x:x+3] for e in game_result[y:y+3]))
	return 'DOXD'[r]

if __name__ == '__main__':
	assert checkio([
		"X.O",
		"XX.",
		"XOO"]) == "X", "Xs wins"
	assert checkio([
		"OO.",
		"XOX",
		"XOX"]) == "O", "Os wins"
	assert checkio([
		"OOX",
		"XXO",
		"OXX"]) == "D", "Draw"