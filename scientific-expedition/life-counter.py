D=[[-1,-1],[-1,0],[-1,1],[0,-1],[0,1],[1,-1],[1,0],[1,1]]
def life_counter(_data,cnt):
	data=set()
	for y in range(len(_data)):
		for x in range(len(_data[y])):
			if _data[y][x]: data.add((y,x))
	for i in range(cnt):
		nxt=set()
		for y0,x0 in data:
			for dy0,dx0 in D:
				y,x=y0+dy0,x0+dx0
				l=sum((y+dy,x+dx) in data for dy,dx in D)
				if l==3 or (l==2 and (y,x) in data): nxt.add((y,x))
		data=nxt
	return len(data)

if __name__=='__main__':
	assert life_counter(((0, 1, 0, 0, 0, 0, 0), (0, 0, 1, 0, 0, 0, 0), (1, 1, 1, 0, 0, 0, 0),
                       (0, 0, 0, 0, 0, 1, 1), (0, 0, 0, 0, 0, 1, 1), (0, 0, 0, 0, 0, 0, 0),
                       (1, 1, 1, 0, 0, 0, 0)), 4)==15