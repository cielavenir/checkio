D=(
	(-1,0),
	(1,0),
	(0,-1),
	(0,1),
)
def finish_map(_m):
	m=list(map(list,_m))
	#mark coast
	for y in range(len(m)):
		for x in range(len(m[y])):
			if m[y][x]=='.' and any(0<=y+a<len(m) and 0<=x+b<len(m[0]) and m[y+a][x+b]=='X' for a in range(-1,2) for b in range(-1,2)):
				m[y][x]='S'
	#mark ghost
	for y in range(len(m)):
		for x in range(len(m[y])):
			if m[y][x]=='D':
				queue=[(x,y)]
				while queue:
					p,q=queue.pop(0)
					for a,b in D:
						if 0<=q+a<len(m) and 0<=p+b<len(m[0]) and m[q+a][p+b]=='.':
							queue.append((p+b,q+a))
							m[q+a][p+b]='D'
	#mark rest
	for y in range(len(m)):
		for x in range(len(m[y])):
			if m[y][x]=='.': m[y][x]='S'
	return tuple([''.join(e) for e in m])

if __name__ == '__main__':
	assert isinstance(finish_map(("D..", "...", "...")), (list, tuple)), "List or tuple"
	assert list(finish_map(("D..XX.....",
							"...X......",
							".......X..",
							".......X..",
							"...X...X..",
							"...XXXXX..",
							"X.........",
							"..X.......",
							"..........",
							"D...X....D"))) == ["DDSXXSDDDD",
												"DDSXSSSSSD",
												"DDSSSSSXSD",
												"DDSSSSSXSD",
												"DDSXSSSXSD",
												"SSSXXXXXSD",
												"XSSSSSSSSD",
												"SSXSDDDDDD",
												"DSSSSSDDDD",
												"DDDSXSDDDD"], "Example"
	assert list(finish_map(("........",
							"........",
							"X.X..X.X",
							"........",
							"...D....",
							"........",
							"X.X..X.X",
							"........",
							"........",))) == ["SSSSSSSS",
											   "SSSSSSSS",
											   "XSXSSXSX",
											   "SSSSSSSS",
											   "DDDDDDDD",
											   "SSSSSSSS",
											   "XSXSSXSX",
											   "SSSSSSSS",
											   "SSSSSSSS"], "Walls"