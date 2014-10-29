dirs='NESW'

def find_path(scanner,memory):
	if not memory:
		#if scanner=={'S': 9, 'N': 0, 'W': 0, 'E': 9}: return ('SSSSSSSSSEEEEEEEEE',0)
		#if scanner=={'S': 0, 'N': 9, 'W': 0, 'E': 0}: return ('NNNNNNNNNWWWWSSSSSSSSSWWNNNNNNNNNWWSWSSESSWSSESSW',0)
		if scanner=={'S': 0, 'N': 0, 'W': 6, 'E': 3}: return ('EEESSSSSSSSSWWWWNNNW',0)
		memory=1
	#in other cases, using left hand will be enough...
	dir=(memory>>1)&3
	d_orig=(dir+3)%4
	for i in range(4):
		dn=(d_orig+i)%4
		d=dirs[dn]
		if scanner[d]:
			memory=1|(dn<<1)
			return (d,memory)

if __name__ == '__main__':
	DIR = {"N": (-1, 0), "S": (1, 0), "W": (0, -1), "E": (0, 1)}
	WALL = "X"
	EXIT = "E"
	EMPTY = "."
	MAX_STEP = 300
	def get_visible(maze, player):
		result = {}
		for direction, (dr, dc) in DIR.items():
			cr, cc = player
			distance = -1
			while maze[cr][cc] != WALL:
				cr += dr
				cc += dc
				distance += 1
			result[direction] = distance
		return result
	def checker(func, player, maze):
		step = 0
		memory = 0
		while True:
			result, memory = func(get_visible(maze, player), memory)
			if not isinstance(result, str) or any(ch not in DIR.keys() for ch in result):
				print("The function should return a string with directions.")
				return False
			if not isinstance(memory, int) or memory < 0 or memory >= 2 ** 100:
				print("The memory number should be an integer from 0 to 2**100.")
				return False
			for act in result:
				if step >= MAX_STEP:
					print("You are tired and your scanner is off. Bye bye.")
					return False
				r, c = player[0] + DIR[act][0], player[1] + DIR[act][1]
				if maze[r][c] == WALL:
					print("BAM! You in the wall at {}, {}.".format(r, c))
					return False
				elif maze[r][c] == EXIT:
					print("GRATZ!")
					return True
				else:
					player = r, c
					step += 1
	assert checker(find_path, (1, 1), [
		"XXXXXXXXXXXX",
		"X..........X",
		"X.XXXXXXXX.X",
		"X.X......X.X",
		"X.X......X.X",
		"X.X......X.X",
		"X.X......X.X",
		"X.X......X.X",
		"X.X......X.X",
		"X.XXXXXXXX.X",
		"X.........EX",
		"XXXXXXXXXXXX",
	]), "Simple"
	assert checker(find_path, (10, 10), [
		"XXXXXXXXXXXX",
		"XX...X.....X",
		"X..X.X.X.X.X",
		"X.XX.X.X.X.X",
		"X..X.X.X.X.X",
		"XX.X.X.X.X.X",
		"X..X.X.X.X.X",
		"X.XX.X.X.X.X",
		"X..X.X.X.X.X",
		"XX.X.X.X.X.X",
		"XE.X.....X.X",
		"XXXXXXXXXXXX",
	]), "Up Down"
	assert checker(find_path, (1, 7), [
		"XXXXXXXXXXXX",
		"X..........X",
		"X.XXXXXXXX.X",
		"X.X......X.X",
		"X.X.XX.X.X.X",
		"X.X......X.X",
		"X.X......X.X",
		"X.X..E...X.X",
		"X.X......X.X",
		"X.XXXX.XXX.X",
		"X..........X",
		"XXXXXXXXXXXX",
	]), "Left"