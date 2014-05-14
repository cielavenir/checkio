D={'N':(0,-1),'E':(1,0),'W':(-1,0),'S':(0,1)}

def bfs(data,s,g):
	back={s:None}
	backstr={}
	q=[s]
	while len(q)>0:
		x,y=q[0]
		if x==g[0] and y==g[1]: break
		q.pop(0)
		for dx,dy,d in [(-1,0,'W'),(0,1,'S'),(1,0,'E'),(0,-1,'N')]:
			if 0<=x+dx*2<len(data[0]) and 0<=y+dy*2<len(data) and data[y+dy][x+dx]!=1 and data[y+dy*2][x+dx*2]!=1 and (x+dx*2,y+dy*2) not in back:
				q.append((x+dx*2,y+dy*2))
				back[(x+dx*2,y+dy*2)]=(x,y)
				backstr[(x+dx*2,y+dy*2)]=d
	if len(q)==0: return None
	r=''
	while back[g]:
		r+=backstr[g]
		g=back[g]
	return r[::-1]

def checkio(_house, stephan, ghost):
	if stephan==1: return 'N' #escaped successfully.
	_house=[_house[i:i+4] for i in range(0,16,4)]
	house=[[0]*7 for i in range(7)]
	for y in range(len(_house)):
		for x in range(len(_house[0])):
			for dx,dy in [D[e] for e in iter(_house[y][x])]:
				house[y*2+dy][x*2+dx]=1
	gx=(ghost-1)%4*2
	gy=(ghost-1)//4*2
	sx=(stephan-1)%4*2
	sy=(stephan-1)//4*2
	for dx,dy in [D[e] for e in iter('NEWS')]:
		if 0<=gx+dx*2<len(house) and 0<=gy+dy*2<len(house): house[gy+dy*2][gx+dx*2]=1
	move=bfs(house,(sx,sy),(0,0))
	if move!=None: return move[0]
	for dx,dy in [D[e] for e in iter('NEWS')]:
		if 0<=gx+dx*2<len(house) and 0<=gy+dy*2<len(house): house[gy+dy*2][gx+dx*2]=0
	move=bfs(house,(sx,sy),(0,0))
	return move[0]

if __name__ == '__main__':
	from random import choice
	DIRS = {"N": -4, "S": 4, "E": 1, "W": -1}
	def check_solution(func, house):
		stephan = 16
		ghost = 1
		for step in range(30):
			direction = func(house[:], stephan, ghost)
			if direction in house[stephan - 1]:
				print('Stefan ran into a closed door. It was hurt.')
				return False
			if stephan == 1 and direction == "N":
				print('Stefan has escaped.')
				return True
			stephan += DIRS[direction]
			if ((direction == "W" and stephan % 4 == 0) or (direction == "E" and stephan % 4 == 1) or
					(stephan < 1) or (stephan > 16)):
				print('Stefan has gone out into the darkness.')
				return False
			sx, sy = (stephan - 1) % 4, (stephan - 1) // 4
			ghost_dirs = [ch for ch in "NWES" if ch not in house[ghost - 1]]
			if ghost % 4 == 1 and "W" in ghost_dirs:
				ghost_dirs.remove("W")
			if not ghost % 4 and "E" in ghost_dirs:
				ghost_dirs.remove("E")
			if ghost <= 4 and "N" in ghost_dirs:
				ghost_dirs.remove("N")
			if ghost > 12 and "S" in ghost_dirs:
				ghost_dirs.remove("S")
			ghost_dir, ghost_dist = "", 1000
			for d in ghost_dirs:
				new_ghost = ghost + DIRS[d]
				gx, gy = (new_ghost - 1) % 4, (new_ghost - 1) // 4
				dist = (gx - sx) ** 2 + (gy - sy) ** 2
				if ghost_dist > dist:
					ghost_dir, ghost_dist = d, dist
				elif ghost_dist == dist:
					ghost_dir += d
			ghost_move = choice(ghost_dir)
			ghost += DIRS[ghost_move]
			if ghost == stephan:
				print('The ghost caught Stephan.')
				return False
		print("Too many moves.")
		return False
	assert check_solution(checkio,
						  ["", "S", "S", "",
						   "E", "NW", "NS", "",
						   "E", "WS", "NS", "",
						   "", "N", "N", ""]), "1st example"
	assert check_solution(checkio,
						  ["", "", "", "",
						   "E", "ESW", "ESW", "W",
						   "E", "ENW", "ENW", "W",
						   "", "", "", ""]), "2nd example"