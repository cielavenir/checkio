_d=[(-1,-1),(-1,0),(-1,1),(0,-1),(0,1),(1,-1),(1,0),(1,1)]
def checkio(field):
	if field[0][0]==-1: return [False,0,0]
	for y in range(len(field)):
		for x in range(len(field[0])):
			if 1<=field[y][x]<=8:
				empty=0
				mine=0
				for d in _d:
					if y+d[0]<0 or len(field)<=y+d[0] or x+d[1]<0 or len(field[0])<=x+d[1]: continue
					if field[y+d[0]][x+d[1]]==-1: empty+=1
					if field[y+d[0]][x+d[1]]==9: mine+=1
				if empty>0 and mine==field[y][x]: #mark as safe
					for d in _d:
						if y+d[0]<0 or len(field)<=y+d[0] or x+d[1]<0 or len(field[0])<=x+d[1]: continue
						if field[y+d[0]][x+d[1]]==-1: return [False,y+d[0],x+d[1]]
				if empty+mine==field[y][x]: #mark as mine
					for d in _d:
						if y+d[0]<0 or len(field)<=y+d[0] or x+d[1]<0 or len(field[0])<=x+d[1]: continue
						if field[y+d[0]][x+d[1]]==-1: return [True,y+d[0],x+d[1]]
	assert False

#This part is using only for self-testing
if __name__ == '__main__':
	def check_is_win_referee(input_map):
		unopened = [1 for x in range(10) for y in range(10) if input_map[x][y] == -1]
		return not unopened
	def build_map(input_map, mine_map, row, col):
		opened = [(row, col)]
		while opened:
			i, j = opened.pop(0)
			neighs = [(i + x, j + y) for x, y in [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]
					  if 0 <= i + x < 10 and 0 <= j + y < 10]
			value = sum([mine_map[k][l] for k, l in neighs])
			input_map[i][j] = value
			if not value:
				for k, l in neighs:
					if input_map[k][l] == -1 and (k, l) not in opened:
						opened.append((k, l))
		return input_map
	def check_solution(func, mine_map):
		input_map = [[-1] * 10 for _ in range(10)]
		while True:
			is_mine, row, col = func([row[:] for row in input_map])  # using copy
			if input_map[row][col] != -1:
				print("You tried to uncover or mark already opened cell.")
				return False
			if is_mine and not mine_map[row][col]:
				print("You marked the wrong cell.")
				return False
			if not is_mine and mine_map[row][col]:
				print("You uncovered a mine. BANG!")
				return False
			if is_mine:
				input_map[row][col] = 9
			else:
				build_map(input_map, mine_map, row, col)
			if check_is_win_referee(input_map):
				return True
		return False
	assert check_solution(checkio, [
		[0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
		[0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
		[0, 0, 1, 0, 1, 0, 0, 1, 0, 0],
		[0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
		[0, 0, 1, 0, 1, 0, 0, 0, 0, 0],
		[0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
		[0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
		[0, 0, 1, 0, 1, 0, 0, 1, 0, 0],
		[0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
		[0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]), "Simple"
	assert check_solution(checkio, [
		[0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
		[0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
		[0, 1, 1, 0, 0, 0, 1, 1, 1, 0],
		[0, 1, 0, 0, 0, 0, 0, 0, 1, 0],
		[0, 1, 0, 0, 0, 0, 0, 0, 1, 0],
		[0, 1, 0, 0, 0, 0, 0, 0, 1, 0],
		[0, 1, 0, 0, 0, 0, 0, 0, 1, 0],
		[0, 1, 0, 0, 0, 0, 0, 0, 1, 0],
		[0, 1, 1, 1, 1, 1, 1, 1, 1, 0],
		[0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]), "Gate"
	assert check_solution(checkio, [
		[0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
		[0, 0, 0, 0, 0, 0, 0, 0, 1, 0],
		[0, 0, 1, 1, 0, 0, 1, 0, 0, 0],
		[0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
		[0, 0, 1, 0, 0, 0, 0, 1, 0, 0],
		[0, 0, 0, 0, 0, 1, 0, 0, 0, 0],
		[0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
		[0, 0, 0, 0, 1, 0, 0, 0, 1, 0],
		[0, 0, 1, 0, 0, 0, 1, 0, 0, 0],
		[0, 1, 0, 0, 0, 0, 0, 0, 0, 0]]), "Various"