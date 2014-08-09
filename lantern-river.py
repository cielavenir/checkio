D=( #Right,Up,Left,Down
	(0,1),
	(-1,0),
	(0,-1),
	(1,0),
)

#solve mazes "whose walls are block" using right-hand method
class Maze:
	def __init__(self,x,y,gx,gy,d,v):
		self.x=x
		self.y=y
		self.gx=gx
		self.gy=gy
		self.d=d
		self.v=v
		self.v[self.y][self.x]='*'
		self.route=[]
		self.route.append((self.x,self.y))
	def ok(self):
		return self.gx==self.x and self.gy==self.y
	def same(self,other):
		return self.x==other.x and self.y==other.y
	def move(self):
		d_orig=(self.d+3)%4
		for i in range(4):
			self.d=(d_orig+i)%4
			if self.v[self.y+D[self.d][0]][self.x+D[self.d][1]]=='.': break
		self.y=self.y+D[self.d][0]
		self.x=self.x+D[self.d][1]
		self.v[self.y][self.x]='*'
		self.route.append((self.x,self.y))

def checkio(_state,time):
	rows=len(_state)
	cols=len(_state)
	state=[['X']*cols]+[list(e) for e in _state]+[['X']*cols]
	sidx=state[1].index('.')
	eidx=state[rows].index('.')
	mazes=[]
	n=0
	while state[1][sidx+n]=='.':
		maze=Maze(sidx+n,1,eidx+n,rows,3,state)
		while not maze.ok(): maze.move()
		mazes.append(maze)
		n+=1
	result=set()
	for i in range(n):
		x,y=mazes[i].route[time]
		print(x,y)
		for j in range(-1,2):
			for k in range(-1,2):
				if state[y+j][x+k]!='X':
					result.add((x+k,y+j))
	print(len(result))
	return len(result)

if __name__=='__main__':
	assert checkio((
		"X....XXX",
		"X....XXX",
		"X....XXX",
		"X....XXX",
		"X....XXX",
		"X......X",
		"X......X",
		"X......X",
		"X......X",
		"XXX....X"), 9)==17