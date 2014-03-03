def bfs(data,s):
	depth={s:data[s[1]][s[0]]}
	q=[s]
	while len(q)>0:
		x,y=q[0]
		dep=depth[q[0]]
		q.pop(0)
		for dx,dy in [(-1,0),(0,1),(1,0),(0,-1)]:
			if 0<=x+dx<len(data[0]) and 0<=y+dy<len(data) and ((x+dx,y+dy) not in depth or data[y+dy][x+dx]+dep<depth[(x+dx,y+dy)]):
				q.append((x+dx,y+dy))
				depth[(x+dx,y+dy)]=data[y+dy][x+dx]+dep
	return min(depth[(x,len(data)-1)] for x in range(len(data[0])))

def checkio(field_map):
	return min(bfs(field_map,(x,0)) for x in range(len(field_map[0])))

#These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
	assert checkio([[1, 1, 1, 1, 0, 1, 1],
					[1, 1, 1, 1, 0, 0, 1],
					[1, 1, 1, 1, 1, 0, 1],
					[1, 1, 0, 1, 1, 0, 1],
					[1, 1, 0, 1, 1, 1, 1],
					[1, 0, 0, 1, 1, 1, 1],
					[1, 0, 1, 1, 1, 1, 1]]) == 2, "1st example"
	assert checkio([[0, 0, 0, 0, 0, 0, 0],
					[1, 1, 1, 1, 1, 1, 1],
					[1, 1, 1, 1, 1, 1, 1],
					[1, 1, 1, 1, 1, 1, 1],
					[1, 1, 0, 1, 0, 1, 1],
					[1, 0, 0, 0, 0, 0, 1],
					[0, 0, 0, 0, 0, 0, 0]]) == 3, "2nd example"
	assert checkio([[1, 1, 1, 1, 1, 0, 1, 1],
					[1, 0, 1, 1, 1, 0, 1, 1],
					[1, 0, 1, 0, 1, 0, 1, 0],
					[1, 0, 1, 1, 1, 0, 1, 1],
					[0, 0, 1, 1, 0, 0, 0, 0],
					[1, 0, 1, 1, 1, 1, 1, 1],
					[1, 0, 1, 1, 1, 1, 1, 1],
					[1, 1, 1, 0, 1, 1, 1, 1]]) == 2, "3rd example"