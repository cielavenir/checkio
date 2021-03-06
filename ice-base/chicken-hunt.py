#direction priority
DIRS2 = [
	("NW", (-1, -1)),
	("NE", (-1, 1)),
	("SE", (1, 1)),
	("SW", (1, -1)),
	("N", (-1, 0)),
	("S", (1, 0)),
	("E", (0, 1)),
	("W", (0, -1)),
	("", (0, 0)),
]

DIRS = dict(DIRS2)

def search(a,c):
	for y in range(len(a)):
		for x in range(len(a[y])):
			if a[y][x]==c:
				return (y,x)

def dist(yard,hobbit,goal,opponent,dir):
	depth={hobbit:0}
	queue=[hobbit]
	if hobbit==goal: return 0
	while queue:
		cur=queue[0]
		queue.pop(0)
		for k,v in DIRS.items():
			nxt=(cur[0]+v[0],cur[1]+v[1])
			if 0<=nxt[0]<len(yard) and 0<=nxt[1]<len(yard[0]) and yard[nxt[0]][nxt[1]]!='X' and yard[nxt[0]][nxt[1]]!=opponent:
				if nxt not in depth:
					queue.append(nxt)
					depth[nxt]=depth[cur]+1
					if nxt==goal: return depth[nxt]
	if dir=='': return 0
	return 99999

def hunt(yard):
	chicken=search(yard,'C')
	myself=search(yard,'I')
	companion=search(yard,'S')
	#filter dir
	myself_dirs=[s for s,e in DIRS2 if 0<=myself[0]+e[0]<len(yard) and 0<=myself[1]+e[1]<len(yard[0]) and yard[myself[0]+e[0]][myself[1]+e[1]]!='X' and yard[myself[0]+e[0]][myself[1]+e[1]]!='S']
	companion_dirs=[s for s,e in DIRS2 if 0<=companion[0]+e[0]<len(yard) and 0<=companion[1]+e[1]<len(yard[0]) and yard[companion[0]+e[0]][companion[1]+e[1]]!='X' and yard[companion[0]+e[0]][companion[1]+e[1]]!='S']
	myself_dirs=[e[1] for e in sorted(enumerate(myself_dirs),key=lambda ie:(dist(yard,(myself[0]+DIRS[ie[1]][0],myself[1]+DIRS[ie[1]][1]),chicken,'S',ie[1]),ie[0]))]
	companion_dir=min(enumerate(companion_dirs),key=lambda ie:(dist(yard,(companion[0]+DIRS[ie[1]][0],companion[1]+DIRS[ie[1]][1]),chicken,'I',ie[1]),ie[0]))[1]
	if myself==min(myself,companion) and (myself[0]+DIRS[myself_dirs[0]][0],myself[1]+DIRS[myself_dirs[0]][1])==(companion[0]+DIRS[companion_dir][0],companion[1]+DIRS[companion_dir][1]):
		return myself_dirs[1]
	return myself_dirs[0]

if __name__ == "__main__":
	from random import choice
	from re import sub
	from math import hypot
	def random_chicken(_, possible):
		return choice(possible)
	def distance_chicken(func):
		def run_chicken(yard, possible):
			enemies = [find_position(yard, str(i + 1)) for i in range(N)]
			best = "", find_position(yard, "C")
			best_dist = 0 if func == max else float("inf")
			for d, (x, y) in possible:
				min_dist = min(hypot(x - ex, y - ey) for ex, ey in enemies)
				if func(min_dist, best_dist) == min_dist:
					best = d, (x, y)
					best_dist = min_dist
				elif min_dist == best_dist:
					best = choice([(d, (x, y)), best])
				print(best, best_dist)
			return best
		return run_chicken
	CHICKEN_ALGORITHM = {
		"random": random_chicken,
		"run_away": distance_chicken(max),
		"hunter": distance_chicken(min)
	}
	ERROR_TYPE = "Your function must return a direction as a string."
	ERROR_FENCE = "A hobbit struck in the fence."
	ERROR_TREE = "A hobbit struck in an obstacle."
	ERROR_HOBBITS = "The Hobbits struck each other."
	ERROR_TIRED = "The Hobbits are tired."
	N = 2
	MAX_STEP = 100
	def find_position(yard, symb):
		for i, row in enumerate(yard):
			for j, ch in enumerate(row):
				if ch == symb:
					return i, j
		return None, None
	def find_free(yard, position):
		x, y = position
		result = []
		for k, (dx, dy) in DIRS.items():
			nx, ny = x + dx, y + dy
			if 0 <= nx < len(yard) and 0 <= ny < len(yard[0]) and yard[nx][ny] == ".":
				result.append((k, (nx, ny)))
		return result
	def prepare_yard(yard, numb):
		return tuple(sub("\d", "S", row.replace(str(numb), "I")) for row in yard)
	def checker(func, yard, chicken_algorithm="random"):
		for _ in range(MAX_STEP):
			individual_yards = [prepare_yard(yard, i + 1) for i in range(N)]
			results = [func(y) for y in individual_yards]
			if any(not isinstance(r, str) or r not in DIRS.keys() for r in results):
				print(ERROR_TYPE)
				return False
			chicken = find_position(yard, "C")
			possibles = find_free(yard, chicken)
			chicken_action, new_chicken = CHICKEN_ALGORITHM[chicken_algorithm](yard, possibles)
			positions = [find_position(yard, str(i + 1)) for i in range(N)]
			new_positions = []
			for i, (x, y) in enumerate(positions):
				nx, ny = x + DIRS[results[i]][0], y + DIRS[results[i]][1]
				if not (0 <= nx < len(yard) and 0 <= ny < len(yard[0])):
					print(ERROR_FENCE)
					return False
				if yard[nx][ny] == "X":
					print(ERROR_TREE)
					return False
				new_positions.append((nx, ny))
			if len(set(new_positions)) != len(new_positions):
				print(ERROR_HOBBITS)
				return False
			if any(new_chicken == pos for pos in new_positions):
				print("Gratz!")
				return True
			# update yard
			temp_yard = [[ch if ch in ".X" else "." for ch in row] for row in yard]
			for i, (x, y) in enumerate(new_positions):
				temp_yard[x][y] = str(i + 1)
			temp_yard[new_chicken[0]][new_chicken[1]] = "C"
			yard = tuple("".join(row) for row in temp_yard)
		print(ERROR_TIRED)
		return False
	assert checker(hunt, ("......",
						  ".1.XX.",
						  "...CX.",
						  ".XX.X.",
						  "...2..",
						  "......"), "random"), "Example 1"
	assert checker(hunt, ("......",
						  ".1.XX.",
						  "...CX.",
						  ".XX.X.",
						  "...2..",
						  "......"), "run_away"), "Example 1"
	assert checker(hunt, ("......",
						  ".1.XX.",
						  "...CX.",
						  ".XX.X.",
						  "...2..",
						  "......"), "hunter"), "Example 1"
	assert checker(hunt, ("1.........",
						  ".X.X.X.X.X",
						  ".X.X.X.X.X",
						  ".X.X.X.X.X",
						  ".X.X.X.X.X",
						  ".X.XCX.X.X",
						  ".X.X.X.X.X",
						  ".X.X.X.X.X",
						  ".X.X.X.X.X",
						  ".X.X.X.X.X",
						  ".........2"), "run_away"), "Tunnels"
	assert checker(hunt, ("1X.X.X.X2",
						  "X.X.X.X.X",
						  ".X.X.X.X.",
						  "X.X.X.X.X",
						  ".X.X.X.X.",
						  "X.X.X.X.X",
						  ".X.XCX.X.",
						  "X.X.X.X.X")), "ChessBoard"
	assert checker(hunt, ("...2...",
						  ".......",
						  ".......",
						  "...C...",
						  ".......",
						  ".......",
						  "...1...")), "Clear Random"