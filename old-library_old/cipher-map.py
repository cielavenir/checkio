def recall_password(grille, template):
	r=''
	for i in range(len(grille)):
		for j in range(len(grille)):
			if grille[i][j]=='X': r+=template[i][j]
	for i in range(len(grille)):
		for j in range(len(grille)):
			if grille[len(grille)-1-j][i]=='X': r+=template[i][j]
	for i in range(len(grille)):
		for j in range(len(grille)):
			if grille[len(grille)-1-i][len(grille)-1-j]=='X': r+=template[i][j]
	for i in range(len(grille)):
		for j in range(len(grille)):
			if grille[j][len(grille)-1-i]=='X': r+=template[i][j]
	return r

#old library cipher-map compatibility
checkio=lambda data:recall_password(data[0],data[1])

if __name__ == '__main__':
	assert checkio([
		['X...',
		 '..X.',
		 'X..X',
		 '....'],
		['itdf',
		 'gdce',
		 'aton',
		 'qrdi']]) == 'icantforgetiddqd', 'First example'
	assert checkio([
		['....',
		 'X..X',
		 '.X..',
		 '...X'],
		['xhwc',
		 'rsqx',
		 'xqzz',
		 'fyzr']]) == 'rxqrwsfzxqxzhczy', 'Second example'