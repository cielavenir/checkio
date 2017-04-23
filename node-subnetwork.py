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

def subnetworks(a,l):
	uf=union_find()
	for x,y in a:
		if x not in l: uf.root(x)
		if y not in l: uf.root(y)
		if x not in l and y not in l:
			uf.unite(x,y)
	return uf.size()
