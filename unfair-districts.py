from itertools import chain

def getadj(x,y,grid,rtpl):
	s=set()
	for (dx,dy) in [(-1,0),(0,-1),(1,0),(0,1)]:
		nx=x+dx
		ny=y+dy
		if 0<=nx<len(grid[0]) and 0<=ny<len(grid) and rtpl[ny][nx]=='*':
			s.add((nx,ny))
	return s

def z(x,y,color,a,tnum,num,grid,rtpl,adjacents):
	for adj in adjacents:
		nx,ny=adj
		rtpl[ny][nx]=color
		ntnum=tnum-grid[ny][nx][0]-grid[ny][nx][1]
		a.add(adj)
		if ntnum==0:
			yield (a,rtpl)
		elif ntnum>0:
			new_adjacents=set(adjacents)
			new_adjacents.update(getadj(nx,ny,grid,rtpl))
			new_adjacents.remove(adj)
			yield from z(nx,ny,color,a,ntnum,num,grid,rtpl,new_adjacents)
		a.remove(adj)
		rtpl[ny][nx]='*'

def dfs(x,y,aa,num,grid,ndistricts,rtpl):
	#if ndistricts==0: yield (aa,rtpl)
	for a,r in z(x,y,ndistricts,set(),num,num,grid,rtpl,set([(x,y)])):
		if ndistricts==1: yield (aa+[a],rtpl)
		for xy in range(len(grid)*len(grid[0])):
			y=xy//len(grid[0])
			x=xy%len(grid[0])
			if rtpl[y][x]=='*':
				yield from dfs(x,y,aa+[a],num,grid,ndistricts-1,r)
				break

def unfair_districts(num,grid):
	#grid: 2 dimensional array whose element is [X,Y]
	#1. get sets of n-mino from 2D array.
	#   n-mino has to be adjacent and all sum (of X and Y) has to be the same as num.
	#2. in n-mino, if the sum of X is larger than Y sum, it is a win. smaller=lose, equal=draw
	#3. the number of win should be more than lose.
	total=sum(sum(unit) for unit in chain(*grid))
	if total % num != 0: return None
	ndistricts=total//num
	rtpl=[['*']*len(grid[0]) for _ in range(len(grid))]
	for a,r in dfs(0,0,[],num,grid,ndistricts,rtpl):
		x=y=z=0
		for e in a:
			x0=y0=0
			for f in e:
				x0+=grid[f[1]][f[0]][0]
				y0+=grid[f[1]][f[0]][1]
			if x0>y0: x+=1
			if x0<y0: y+=1
			if x0==y0: z+=1
		if x>y:
			return [''.join(chr(f+64) for f in e) for e in r]
	return [] # search exhausted
