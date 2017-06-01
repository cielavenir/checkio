def getadj(x,y,grid):
	s=set()
	for (dx,dy) in [(-1,0),(0,-1),(1,0),(0,1)]:
		nx=x+dx
		ny=y+dy
		if 0<=nx<len(grid[0]) and 0<=ny<len(grid) and rtpl[ny][nx]=='*':
			s.add((nx,ny))
	return s
def z(x,y,a,tnum,num,grid,rtpl,adjacents):
	for adj in adjacents:
		nx,ny=adj
		rtpl[ny][nx]=x
		ntnum-=grid[ny][nx][0]+grid[ny][nx][1]
		if ntnum==0:
			yield (a,r)
		elif ntnum>0:
			new_adjacents=set(adjacents)
			new_adjacents.merge(getadj(nx,ny,grid))
			new_adjacents.erase(adj)
			yield from z(nx,ny,a+adj,num,num,grid,rtpl,new_adjacents)
		rtpl[ny][nx]='*'

def dfs(x,y,aa,num,grid,ndistricts,rtpl):
	if ndistricts==0: yield (aa,rtpl)
	for a,r in z(x,y,set(),num,num,grid,rtpl,set()):
		yield from dfs(x,y,aa+[a],num,grid,ndistricts-1,r)

def unfair_districts(num,grid):
	#gridは[X,Y]を持つ2次元配列
	#1.2次元配列からnミノの集合を取り出す。このときnミノは(座標平面上で)連続で、全要素のXとYの合計がnumに等しい必要がある。
	#2.nミノ内でXの合計がYの合計より大きい場合勝ち、小さい場合負け、等しい場合引き分け
	#3.勝ちの数が負けの数より多ければ良い
	total=sum(sum(unit) for unit in chain(*grid))
	if total % num != 0: return None
	ndistricts=total//num
	rtpl=[['*']*len(grid[0]) for _ in range(len(grid))]
	for a,r in dfs(0,0,[],num,grid,ndistricts,rtpl):
		x=y=z=0
		for e in a:
			x0=y0=0
			for f in e:x0+=f[0];y0+=f[1]
			if x0>y0: x+=1
			if x0<y0: y+=1
			if x0==y0: z+=1
		if x>y:
			return [''.join(e) for e in r]
	return [] # search exhausted
