def z(x,y,grid,adjacents):
	pass
def dfs(num,grid,ndistricts,rtpl):
	pass

def unfair_districts(num,grid):
	#gridは[X,Y]を持つ2次元配列
	#1.2次元配列からnミノの集合を取り出す。このときnミノは(座標平面上で)連続で、全要素のXとYの合計がnumに等しい必要がある。
	#2.nミノ内でXの合計がYの合計より大きい場合勝ち、小さい場合負け、等しい場合引き分け
	#3.勝ちの数が負けの数より多ければ良い
	total=sum(sum(unit) for unit in chain(*grid))
	if total % num != 0: return None
	ndistricts=total//num
	rtpl=[['*']*len(grid[0]) for _ in range(len(grid))]
	for a,r in dfs(num,grid,ndistricts,rtpl):
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
