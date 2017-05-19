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

def disconnected_users(a,v,s,l):
	uf=union_find()
	for x,y in a:
		uf.root(x)
		uf.root(y)
		if x not in l and y not in l:
			uf.unite(x,y)
	r=0
	for e in uf.parent:
		if uf.root(e)!=uf.root(s):
			r+=v[e]
	return r
