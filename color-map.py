from collections import defaultdict

def links(_a,_b):
	for a in _a:
		for b in _b:
			minx=min(a[0],b[0])
			maxx=max(a[0],b[0])
			miny=min(a[1],b[1])
			maxy=max(a[1],b[1])
			#manhattan==1
			if (maxx-minx)+(maxy-miny)==1: return True
	return False

def dfs(linkage,result,d,n):
	if d==n:
		yield result
	else:
		for i in range(1,5):
			if all(result[e]!=i for e in linkage[d] if e<d):
				for e in dfs(linkage,result+[i],d+1,n): yield e

def checkio(m):
	n=0
	a=defaultdict(set) # a[country] => set of (x,y)
	for y in range(len(m)):
		for x in range(len(m[y])):
			n=max(n,m[y][x]+1)
			a[m[y][x]].add((x,y))
	linkage=defaultdict(list)
	for i in range(n):
		for j in range(i+1,n):
			if links(a[i],a[j]):
				linkage[i].append(j)
				linkage[j].append(i)
	return next(e for e in dfs(linkage,[1],1,n))