class UnionFind:
	def __init__(self):
		self.parent={}
	def root(self,x):
		if x not in self.parent: self.parent[x]=x
		return x if self.parent[x]==x else self.root(self.parent[x])
	def unite(self,x,y):
		x=self.root(x)
		y=self.root(y)
		if x==y: return False
		self.parent[x]=y
		return True

def check_connection(_conn,a,b):
	conn=[e.split('-') for e in _conn]
	uf=UnionFind()
	for e in conn: uf.unite(e[0],e[1])
	return not uf.unite(a,b)

if __name__ == '__main__':
	assert check_connection(
	("dr101-mr99", "mr99-out00", "dr101-out00", "scout1-scout2",
	 "scout3-scout1", "scout1-scout4", "scout4-sscout", "sscout-super"),
	"scout2", "scout3") == True
	assert check_connection(
	("dr101-mr99", "mr99-out00", "dr101-out00", "scout1-scout2",
	 "scout3-scout1", "scout1-scout4", "scout4-sscout", "sscout-super"),
	"dr101", "sscout") == False