SHIP = "S"
TORNADO = "O"
ICEBERG = "X"
EMPTY = "."

HUNT_DISTANCE = 2

DIRS = {
	"N": (-1, 0),
	"S": (1, 0),
	"W": (0, -1),
	"E": (0, 1),
	".": (0, 0),
}

def manhattan(a,b):
	return abs(a[0]-b[0])+abs(a[1]-b[1])

def move_ship(data, fuel):
	tornados=[]
	S=(0,0)
	for y in range(len(data)):
		for x in range(len(data[0])):
			if data[y][x]=='S': S=(x,y)
			if data[y][x]=='O': tornados.append((x,y))
	back={S:None}
	backstr={}
	q=[S]
	g=(len(data[0])-1,len(data)-1)
	#first try
	x,y=q[0]
	q.pop(0)
	for d,(dy,dx) in DIRS.items():
		if 0<=x+dx<len(data[0]) and 0<=y+dy<len(data) and data[y+dy][x+dx]=='.' and all(manhattan((x+dx,y+dy),e)>1 for e in tornados):
			q.append((x+dx,y+dy))
			back[(x+dx,y+dy)]=(x,y)
			backstr[(x+dx,y+dy)]=d
	while len(q)>0:
		x,y=q[0]
		if x==g[0] and y==g[1]: break
		q.pop(0)
		for d,(dy,dx) in DIRS.items():
			if 0<=x+dx<len(data[0]) and 0<=y+dy<len(data) and data[y+dy][x+dx]=='.' and (x+dx,y+dy) not in back:
				q.append((x+dx,y+dy))
				back[(x+dx,y+dy)]=(x,y)
				backstr[(x+dx,y+dy)]=d
	if len(q)==0: return '.'
	r=''
	while back[g]:
		r+=backstr[g]
		g=back[g]
	return r[::-1][0]

if __name__ == '__main__':
	import random
	def prepare_map(grid, ship, tornadoes):
		grid = list(list(row) for row in grid)
		grid[ship[0]][ship[1]] = SHIP
		for t in tornadoes:
			grid[t[0]][t[1]] = TORNADO
		return tuple("".join(row) for row in grid)
	def check_solution(func, sea, fuel, tornadoes):
		ship = (0, 0)
		for step in range(fuel):
			user_result = func(prepare_map(sea, ship, tornadoes), fuel - step)
			if not isinstance(user_result, str) and user_result not in DIRS.keys():
				print("You should return a string with an action.")
				return False
			sx, sy = ship
			sea_width = len(sea[0])
			sea_height = len(sea)
			new_sx, new_sy = sx + DIRS[user_result][0], sy + DIRS[user_result][1]
			ship = new_sx, new_sy
			if (new_sx, new_sy) in tornadoes:
				print("Dont move in a tornado! SOS")
				return False
			if sea[new_sx][new_sy] == ICEBERG:
				print("ICEBERG! Turn to ... SOS")
				return False
			if new_sx < 0 or new_sx >= len(sea) or new_sy < 0 or new_sy >= len(sea[0]):
				print("Captain, we lost.")
				return False
			if (new_sx, new_sy) == (sea_height - 1, sea_width - 1):
				print("WIN!")
				return True
			# Aaaaand tornado move
			for i in range(len(tornadoes)):
				tx, ty = tornadoes[i]
				possible = []
				for direction, (dx, dy) in DIRS.items():
					x, y = tx + dx, ty + dy
					if 0 <= x < sea_height and 0 <= y < sea_width and sea[x][y] != ICEBERG and (x, y) not in tornadoes:
						possible.append((direction, (x, y)))
				distance = abs(sx - tx) + abs(sy - ty)
				if distance <= HUNT_DISTANCE:
					best = float("inf"), (tx, ty), "."
					for d, (x, y) in possible:
						possible_distance = abs(sx - x) + abs(sy - y)
						if possible_distance < best[0]:
							best = possible_distance, (x, y), d
						elif possible_distance == best[0]:
							best = random.choice([(possible_distance, (x, y), d), best])
					tornadoes[i] = best[1]
				else:
					rand = random.choice(possible)
					tornadoes[i] = rand[1]
			if ship in tornadoes:
				print("Tornado caught us, Cap.")
				return False
		print("We don't have fuel.")
		return False
	assert check_solution(move_ship, (
		".....",
		".XXX.",
		"...X.",
		".XXX.",
		".....",), 100, [(2, 2)]), "First"
	assert check_solution(move_ship, (
		".......",
		".X.....",
		".XXXX.X",
		".X.....",
		".X.X...",
		".X.X...",
		".X.X...",
		"...X...",), 100, [(0, 6)]), "First"
	assert check_solution(move_ship, (
		".........",
		".X.X.X.X.",
		".........",
		".X.X.X.X.",
		".........",
		".X.X.X.X.",
		".........",
		".X.X.X.X.",
		".........",), 100, [(6, 2), (4, 4), (2, 6)]), "First"