import heapq
INF=1<<30
D=((-1,0),(0,-1),(1,0),(0,1))

def shortestPath(g,s,dist,prev):
	n = len(g)
	dist[s] = 0
	Q=[]
	heapq.heappush(Q,(0,-2,s))
	while Q:
		e=heapq.heappop(Q)
		if prev[e[2]]!=-1: continue
		prev[e[2]]=e[1]
		for f in g[e[2]]:
			if dist[f[2]]>e[0]+f[0]:
				dist[f[2]]=e[0]+f[0]
				heapq.heappush(Q,(e[0]+f[0],f[1],f[2]))

M=[]
def shortestHamiltonCycle(n):
	N=1<<n
	best=[[0]*n for _ in range(N)]
	for S in range(N):
		for i in range(n): best[S][i]=INF
	best[0][0]=0
	for S in range(N):
		for j in range(n):
			if not S&(1<<j):
				for i in range(n):
					if best[S|(1<<j)][j] > best[S][i] + M[i][j]:
						best[S|(1<<j)][j] = best[S][i] + M[i][j]
	return -1 if best[N-1][0]==INF else best[N-1][0]

def inside(data,y,x):
	return 0<=y<len(data) and 0<=x<len(data[0])

def mountaintop(data,y,x):
	if not inside(data,y,x) or data[y][x]==0: return (0,y,x)
	r=(data[y][x],y,x)
	data[y][x]=0
	for dx,dy in D:
		q=mountaintop(data,y+dy,x+dx)
		if r[0]<q[0]: r=q
	return r

def climbing_route(data):
	global M
	data=[list(map(int,e)) for e in data]
	H=len(data)
	W=len(data[0])
	g=[[] for _ in range(H*W)]
	for i in range(H):
		for j in range(W):
			x=i*W+j
			if i<H-1:
				y=(i+1)*W+j
				f=data[i][j]-data[i+1][j]
				if abs(f)<=1: g[x].append((1,x,y));g[y].append((1,y,x))
			if j<W-1:
				y=i*W+j+1
				f=data[i][j]-data[i][j+1]
				if abs(f)<=1: g[x].append((1,x,y));g[y].append((1,y,x))
	#in this iteration "data" will be destroyed
	max_area=[0,H*W-1]
	for i in range(H):
		for j in range(W):
			x=i*W+j
			'''
			if all(not inside(data,i+dy,j+dx) or data[i][j]>data[i+dy][j+dx] for dx,dy in D):
				max_area.append(x)
			'''
			if data[i][j]>0:
				top=mountaintop(data,i,j)
				max_area.append(top[1]*W+top[2])
	N=len(max_area)
	M=[[0]*N for _ in range(N)]
	for i in range(N):
		dist=[INF]*len(g)
		prev=[-1]*len(g)
		shortestPath(g,max_area[i],dist,prev)
		for j in range(N): M[i][j]=dist[max_area[j]]
	M[0][1]=M[1][0]=0
	return shortestHamiltonCycle(N)

if __name__ == '__main__':
	assert climbing_route([
		'000',
		'210',
		'000']) == 6, 'basic'
	assert climbing_route([
		'00000',
		'05670',
		'04980',
		'03210',
		'00000']) == 26, 'spiral'
	assert climbing_route([
		'000000001',
		'222322222',
		'100000000']) == 26, 'bridge'
	assert climbing_route([
		'000000002110',
		'011100002310',
		'012100002220',
		'011100000000']) == 26, 'two top'
	assert climbing_route([
		'00000000120000',
		'00100001432100',
		'01211112211000',
		'00100000000000']) == 18, 'one top'
	assert climbing_route([
		'00000000000000000000000000',
		'00000000000111111100000000',
		'00000000000122222100000000',
		'00000000000123332100000000',
		'00000000000123432100000000',
		'00000000000123332100000000',
		'00000000000122222100000000',
		'00000000000111111100000000',
		'00000000000000000000000000',
		'00000111110000000000000000',
		'00000122210000000000000000',
		'00000123210000000000000000',
		'00000122210000000011223110',
		'00000111110000000000000000',
		'01110000000000000000000000',
		'01210000000000000000000000',
		'01110000000000000000000000',
		'00000000000000000000000000']) == 70, 'pyramids'
