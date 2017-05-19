from collections import defaultdict
class union_find:
	def __init__(self):
		self.parent={}
	def root(self,a):
		if a not in self.parent: self.parent[a]=a
		if self.parent[a]!=a: self.parent[a]=self.root(self.parent[a])
		return self.parent[a]
	def unite(self,a,b):
		x=self.root(a)
		y=self.root(b)
		self.parent[x]=y
	def size(self):
		return len(set(self.root(e) for e in self.parent))

def most_crucial(a,_v):
	retv=[float('inf'),float('inf')]
	ret=[]
	for v in _v:
		uf=union_find()
		for x,y in a:
			uf.root(x)
			uf.root(y)
			if x!=v and y!=v:
				uf.unite(x,y)
		r=defaultdict(int)
		for w in _v:
			r[uf.root(w)]+=_v[w]
		xretv=sum(e**2 for e in r.values())
		if retv[0]>xretv or (retv[0]==xretv and _v[v]>retv[1]):
			retv=[xretv,_v[v]]
			ret=[]
		if retv[0]==xretv and _v[v]==retv[1]:
			ret.append(v)
	return ret

