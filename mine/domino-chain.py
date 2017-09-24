from collections import defaultdict

def dfs(h,c,q):
	if not q: return 1
	x=set()
	r=0
	for e in h[c]:
		if e==-1: continue
		if e in x: continue
		x.add(e)
		try:
			ie=h[e].index(c)
			h[e][ie]=-1
		except IndexError:
			continue
		ic=h[c].index(e)
		h[c][ic]=-1
		r+=dfs(h,e,q-1)
		h[c][ic]=e
		h[e][ie]=c
	return r

def domino_chain(tiles):
	h=defaultdict(list)
	x=tiles.split(', ')
	for e in x:
		a,b=map(int,e.split('-'))
		h[a].append(b)
		h[b].append(a)
	o=set()
	for s in h:
		if len(h[s])%1:o.add(s)
	r=0
	for s in o or h:
		r+=dfs(h,s,len(x))
	return r/2

if __name__ == '__main__':
	assert domino_chain("0-2, 0-5, 1-5, 1-3, 5-5") == 1
	assert domino_chain("1-5, 2-5, 3-5, 4-5, 3-4") == 2
	assert domino_chain("0-5, 1-5, 2-5, 3-5, 4-5, 3-4") == 0
	assert domino_chain("0-1, 0-2, 1-3, 1-2, 3-4, 2-4") == 6
	assert domino_chain("0-1, 0-2, 1-3, 1-2, 3-4, 2-4, 3-0, 0-4") == 0
	assert domino_chain("1-2, 2-2, 2-3, 3-3, 3-1") == 5
	assert domino_chain("1-4, 3-4, 0-4, 0-5, 4-5, 2-4, 2-5") == 0
	assert domino_chain("1-4, 1-5, 0-2, 1-6, 4-6, 4-5, 5-6") == 0
	assert domino_chain("1-2, 2-3, 2-4, 3-4, 2-5, 2-6, 5-6") == 8
	assert domino_chain("1-2, 2-3, 3-1, 4-5, 5-6, 6-4") == 0
	assert domino_chain("1-2, 1-4, 1-5, 1-6, 1-1, 2-5, 4-6") == 28
	print("Basic tests passed.")
