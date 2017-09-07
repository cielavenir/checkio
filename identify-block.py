# http://qiita.com/cielavenir/items/1bf073a963f6b1fedb31 ported from C++ into Python.

D=[[-1,0],[0,-1],[1,0],[0,1]]
def tetromino(island): #v is sorted by x, then y
	it=island[0]
	if [it[0]+1,it[1]] in island and [it[0],it[1]+1] in island and [it[0]+1,it[1]+1] in island:
		return 'O'
	if [it[0]+1,it[1]] in island and [it[0]+2,it[1]] in island and [it[0]+3,it[1]] in island:
		return 'I'
	if [it[0],it[1]+1] in island and [it[0],it[1]+2] in island and [it[0],it[1]+3] in island:
		return 'I'

	for it in island:
		d=[]
		for i in range(4):
			if [it[0]+D[i][0],it[1]+D[i][1]] in island: d.append(i)
		if len(d)==3: return 'T'
		if len(d)==2 and abs(d[0]-d[1])!=2:
			if d==[0,3]: d=[3,0]
			if [it[0]+D[ d[0] ][0]*2,it[1]+D[ d[0] ][1]*2] in island:
				return 'L'
			if [it[0]+D[ d[1] ][0]*2,it[1]+D[ d[1] ][1]*2] in island:
				return 'J'
			if [it[0]+D[ d[0] ][0]+D[ (d[0]-1)%4 ][0],it[1]+D[ d[0] ][1]+D[ (d[0]-1)%4 ][1]] in island:
				return 'Z'
			if [it[0]+D[ d[1] ][0]+D[ (d[1]+1)%4 ][0],it[1]+D[ d[1] ][1]+D[ (d[1]+1)%4 ][1]] in island:
				return 'S'
	return None

def identify_block(data):
	island=sorted([(e-1)%4,(e-1)//4] for e in data)
	'''
	q=[island[0]]
	depth={tuple(island[0]):0}
	while q:
		it=q.pop(0)
		for d in D:
			nxt=[it[0]+d[0],it[1]+d[1]]
			if tuple(nxt) not in depth and nxt in island:
				depth[tuple(nxt)]=depth[tuple(it)]+1
				q.append(nxt)
	if len(depth)!=4: return None
	'''
	return tetromino(island)
