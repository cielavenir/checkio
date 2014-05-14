cross=lambda a,b: (a.conjugate()*b).imag
dot=lambda a,b: (a.conjugate()*b).real

def ccw(a,b,c):
	b-=a
	c-=a
	if cross(b,c)>0:  return +1 # counter clockwise
	if cross(b,c)<0:  return -1 # clockwise
	if dot(b,c)<0:    return +2 # c--a--b on line
	if abs(b)<abs(c): return -2 # a--b--c on line
	return 0

def intersectSS(s0,s1,t0,t1):
	return ccw(s0,s1,t0)*ccw(s0,s1,t1)<=0 and ccw(t0,t1,s0)*ccw(t0,t1,s1)<=0

def bfs(graph,s,g):
	back={s:None}
	depth={s:0}
	q=[s]
	while len(q)>0:
		x=q[0]
		if x==g: break
		q.pop(0)
		for e in graph[x]:
			if e not in depth or depth[x]+abs(e-x)<depth[e]:
				q.append(e)
				back[e]=x
				depth[e]=depth[x]+abs(e-x)
	if len(q)==0: return None
	ret=depth[g]/3
	while back[g]:
		#print(g)
		g=back[g]
	#print(ret)
	return ret

z=0.5 #lol
def checkio(_map):
	if _map[0][0]=='A': return 0
	bats=[]
	walls=[]
	for y in range(len(_map)):
		for x in range(len(_map[0])):
			if _map[y][x] in ['A','B']:
				if _map[y][x]=='A': alpha=complex(x*3+1,y*3+1)
				bats.append(complex(x*3+1,y*3+1))
			if _map[y][x]=='W':
				walls.append((complex(x*3-z,y*3-z),complex(x*3+2+z,y*3+2+z)))
				walls.append((complex(x*3+2+z,y*3-z),complex(x*3-z,y*3+2+z)))
	graph={}
	for i in range(len(bats)):
		for j in range(i+1,len(bats)):
			if not any(intersectSS(bats[i],bats[j],*e) for e in walls):
				if bats[i] not in graph: graph[bats[i]]=[]
				graph[bats[i]].append(bats[j])
				if bats[j] not in graph: graph[bats[j]]=[]
				graph[bats[j]].append(bats[i])
	return bfs(graph,complex(1,1),alpha)

if __name__ == '__main__':
	'''
	assert checkio([
		"B--",
		"---",
		"--A"]) == 2.83, "1st example"
	'''
	assert checkio([
		"B-B",
		"BW-",
		"-BA"]) == 4, "2nd example"
	assert checkio([
		"BWB--B",
		"-W-WW-",
		"B-BWAB"]) == 12, "3rd example"
	assert checkio([
		"B---B-",
		"-WWW-B",
		"-WA--B",
		"-W-B--",
		"-WWW-B",
		"B-BWB-"]) == 9.24, "4th example"