def bfs(data,s,g,dcur):
	back={s:None}
	backstr={}
	q=[s]
	while len(q)>0:
		x,y=q[0]
		if x==g[0] and y==g[1]: break
		q.pop(0)
		for dx,dy,d in [(0,-1,0),(1,0,1),(0,1,2),(-1,0,3)]:
			if 0<=x+dx<len(data[0]) and 0<=y+dy<len(data) and (data[y+dy][x+dx]=='.' or data[y+dy][x+dx]=='C') and (x+dx,y+dy) not in back:
				q.append((x+dx,y+dy))
				back[(x+dx,y+dy)]=(x,y)
				backstr[(x+dx,y+dy)]=d
	r=[]
	if len(q)==0:
		x,y=s
		for dx,dy,d in [(0,-1,0),(1,0,1),(0,1,2),(-1,0,3)]:
			if 0<=x+dx<len(data[0]) and 0<=y+dy<len(data) and data[y+dy][x+dx]=='.':
				r=[d]
				break
		else:
			raise Exception('dead end')
	else:
		while back[g]:
			r.append(backstr[g])
			g=back[g]
	ret=''
	for e in reversed(r):
		if dcur==e:
			ret+='F'
		elif (e-dcur+4)%4==1:
			ret+='R'
			dcur=(dcur+1)%4
		elif (dcur-e+4)%4==1:
			ret+='L'
			dcur=(dcur-1+4)%4
		else:
			raise Exception('tried backward') # should not happen.
	return ret

def move_snake(field_map):
	zero=None
	one=None
	cherry=None
	for y in range(len(field_map)):
		for x in range(len(field_map[0])):
			if field_map[y][x]=='0': zero=(x,y)
			if field_map[y][x]=='1': one=(x,y)
			if field_map[y][x]=='C': cherry=(x,y)
	if zero[1]-one[1]==1: dcur=2
	if one[0]-zero[0]==1: dcur=3
	if one[1]-zero[1]==1: dcur=0
	if zero[0]-one[0]==1: dcur=1
	return bfs(field_map,zero,cherry,dcur)

ACTION = ("L", "R", "F")
CHERRY = 'C'
TREE = 'T'
SNAKE_HEAD = '0'
SNAKE = {'0', '1', '2', '3', '4', '5', '6', '7', '8', '9'}
EMPTY = "."

SIZE = 10
DISTANCE = 5
INITIAL_STEPS = 200

TESTS = {
	"0. Basics": [
		".......T..",
		".T........",
		".....T....",
		"..T....T..",
		"..........",
		".0...T....",
		".1........",
		".2.T...T..",
		".3...T....",
		".4........"]
	,
	"1. Empty": [
		"..........",
		"..........",
		"..........",
		"..........",
		"..........",
		".0........",
		".1........",
		".2........",
		".3........",
		".4........"]
	,
	"2. Big L": [
		"..........",
		"..T.T.....",
		"..T.T.....",
		"..T.T.....",
		"..T.T.....",
		".0T.TTTTT.",
		".1T.......",
		".2TTTTTTT.",
		".3........",
		".4........"]
	,
	"3. Chaos": [
		"..T....T..",
		".......T..",
		"...TTT....",
		"..T....T..",
		"..T...T...",
		".0T..T....",
		".1........",
		".2.T..TT..",
		".3..TT....",
		".4........"]
	,
	"4. Chess Knight": [
		"...T...T..",
		".T...T....",
		"...T...T..",
		".T...T....",
		"...T...T..",
		"0T...T...T",
		"1..T...T..",
		"2T...T....",
		"3..T...T..",
		"4....T...T"]
	,
	"5. Wall": [
		"..........",
		"..........",
		"..........",
		"..........",
		"TTTT.TTTTT",
		"..........",
		"..........",
		"..........",
		"..........",
		".43210...."
	],
	"6. Pits": [
		"TTTTTTTTTT",
		"....T....T",
		"....T....T",
		"....T....T",
		"TTT.TTTT.T",
		"TT........",
		"TT........",
		"TTTT.TTTTT",
		"T.........",
		"T....01234"]
	,
	"7. Hard": [
		"......T...",
		"...T..T...",
		"...T.TT.T.",
		"..TT..T...",
		"TT......TT",
		"...TT.T...",
		".T....T..4",
		"...TTTTTT3",
		"..T....012",
		"..T.....TT"
	],
	"8. Evil": [
		"....T...TT",
		".TT...T...",
		"....T...T.",
		"TTTTTTTTT.",
		"T.........",
		"T.TTTTTTT.",
		"T..4.TT...",
		"TTT32T..T.",
		"TT.01T....",
		"TT...TTTTT"
	]
}

if __name__ == '__main__':
	# This part is using only for self-checking and not necessary for auto-testing
	def find_snake(field_map):
		snake = {}
		for i, row in enumerate(field_map):
			for j, ch in enumerate(row):
				if ch in SNAKE:
					snake[ch] = (i, j)
		return snake

	def find_new_head(snake, action):
		head = snake[SNAKE_HEAD]
		snake_dir = (head[0] - snake["1"][0], head[1] - snake["1"][1])
		if action == 'F':
			return head[0] + snake_dir[0], head[1] + snake_dir[1]
		elif action == 'L':
			return head[0] - snake_dir[1], head[1] + snake_dir[0]
		elif action == 'R':
			return head[0] + snake_dir[1], head[1] - snake_dir[0]
		else:
			raise ValueError("The action must be only L,R or F")

	def pack_map(list_map):
		return [''.join(row) for row in list_map]

	def create_cherry(field, head):
		from random import choice

		distance = DISTANCE
		possible = []
		while not possible:
			possible = [(i, j) for i in range(SIZE) for j in range(SIZE)
						if field[i][j] == "." and (abs(i - head[0]) + abs(j - head[1])) == distance]
			distance = (distance + 1) % SIZE
		return choice(possible)

	def check_solution(func, field_map):
		temp_map = [list(row) for row in field_map]
		head = find_snake(field_map)[SNAKE_HEAD]
		crow, ccol = create_cherry(field_map, head)
		temp_map[crow][ccol] = CHERRY
		field_map = pack_map(temp_map)
		step_count = INITIAL_STEPS
		while True:
			route = func(field_map[:])
			res_route = ""
			for ch in route:
				if step_count < 0:
					print("Too many steps."),
					return False
				if ch not in ACTION:
					print("The route must contain only F,L,R symbols")
					return False
				res_route += ch
				snake = find_snake(temp_map)
				tail = snake[max(snake.keys())]
				temp_map[tail[0]][tail[1]] = EMPTY
				new_head = find_new_head(snake, ch)
				for s_key in sorted(snake.keys())[:-1]:
					s = snake[s_key]
					temp_map[s[0]][s[1]] = str(int(temp_map[s[0]][s[1]]) + 1)
				if (new_head[0] < 0 or new_head[0] >= len(temp_map) or
							new_head[1] < 0 or new_head[1] >= len(temp_map[0])):
					print("The snake crawl outside")
					return False
				elif temp_map[new_head[0]][new_head[1]] == 'T':
					print("The snake struck at the tree")
					return False
				elif temp_map[new_head[0]][new_head[1]] in SNAKE:
					print("The snake bit itself")
					return False
				if temp_map[new_head[0]][new_head[1]] == 'C':
					temp_map[new_head[0]][new_head[1]] = SNAKE_HEAD
					if max(snake.keys()) == '9':
						print("Score: {}".format(step_count))
						return True
					else:
						temp_map[tail[0]][tail[1]] = str(int(max(snake.keys())) + 1)
						cherry = create_cherry(temp_map, new_head)
						temp_map[cherry[0]][cherry[1]] = CHERRY
						step_count -= 1
				else:
					temp_map[new_head[0]][new_head[1]] = SNAKE_HEAD
				step_count -= 1
				field_map = pack_map(temp_map)
	for k in sorted(TESTS.keys()):
		assert check_solution(move_snake,TESTS[k])