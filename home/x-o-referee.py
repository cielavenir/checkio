b=lambda s,c: ((s[0]==c and s[1]==c and s[2]==c)or(s[3]==c and s[4]==c and s[5]==c)or(s[6]==c and s[7]==c and s[8]==c)or(s[0]==c and s[3]==c and s[6]==c)or(s[1]==c and s[4]==c and s[7]==c)or(s[2]==c and s[5]==c and s[8]==c)or(s[0]==c and s[4]==c and s[8]==c)or(s[2]==c and s[4]==c and s[6]==c))
solve=lambda game_result: 'D' if b(game_result,'X') and b(game_result,'O') else 'X' if b(game_result,'X') else 'O' if b(game_result,'O') else 'D'
checkio=lambda game_result: solve(''.join(game_result))

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