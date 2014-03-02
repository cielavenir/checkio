import itertools

def bfs(data,s,g):
	back={s:None}
	backstr={}
	q=[s]
	while len(q)>0:
		x,y=q[0]
		if x==g[0] and y==g[1]: break
		q.pop(0)
		for dx,dy,d in [(-1,0,'L'),(0,1,'D'),(1,0,'R'),(0,-1,'U')]:
			if 0<=x+dx<len(data[0]) and 0<=y+dy<len(data) and data[y+dy][x+dx]!='W' and (x+dx,y+dy) not in back:
				q.append((x+dx,y+dy))
				back[(x+dx,y+dy)]=(x,y)
				backstr[(x+dx,y+dy)]=d
	if len(q)==0: return None
	r=''
	while back[g]:
		r+=backstr[g]
		g=back[g]
	return r[::-1]

def checkio(field_map):
	box=[]
	for y in range(len(field_map)):
		for x in range(len(field_map[0])):
			if field_map[y][x]=='S': start=(x,y)
			if field_map[y][x]=='E': goal=(x,y)
			if field_map[y][x]=='B': box.append((x,y))
	n=bfs(field_map,start,goal)
	m=min(((bfs(field_map,start,a),bfs(field_map,a,b),bfs(field_map,b,goal)) for a,b in itertools.permutations(box,2)),key=lambda e: len(e[0])*2+1+len(e[1])+1+len(e[2])*2)
	return 'B'.join(m) if len(m[0])*2+1+len(m[1])+1+len(m[2])*2<len(n)*2 else n

if __name__ == '__main__':
	#This part is using only for self-checking and not necessary for auto-testing
	ACTIONS = {
		"L": (0, -1),
		"R": (0, 1),
		"U": (-1, 0),
		"D": (1, 0),
		"B": (0, 0)
	}
	def check_solution(func, max_time, field):
		max_row, max_col = len(field), len(field[0])
		s_row, s_col = 0, 0
		total_time = 0
		hold_box = True
		route = func(field[:])
		for step in route:
			if step not in ACTIONS:
				print("Unknown action {0}".format(step))
				return False
			if step == "B":
				if hold_box:
					if field[s_row][s_col] == "B":
						hold_box = False
						total_time += 1
						continue
					else:
						print("Stephan broke the cargo")
						return False
				else:
					if field[s_row][s_col] == "B":
						hold_box = True
					total_time += 1
					continue
			n_row, n_col = s_row + ACTIONS[step][0], s_col + ACTIONS[step][1],
			total_time += 2 if hold_box else 1
			if 0 > n_row or n_row >= max_row or 0 > n_col or n_row >= max_col:
				print("We've lost Stephan.")
				return False
			if field[n_row][n_col] == "W":
				print("Stephan fell in water.")
				return False
			s_row, s_col = n_row, n_col
			if field[s_row][s_col] == "E" and hold_box:
				if total_time <= max_time:
					return True
				else:
					print("You can deliver the cargo faster.")
					return False
		print("The cargo is not delivered")
		return False
	assert check_solution(checkio, 12, ["S...", "....", "B.WB", "..WE"]), "1st Example"
	assert check_solution(checkio, 11, ["S...", "....", "B..B", "..WE"]), "2nd example"