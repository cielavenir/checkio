def golf(m):
 for z in range(len(m)):
  for y in range(len(m[z])):
   for x in range(len(m[z][y])):
    if any(x+a<len(m[z][y])and y+b<len(m[z])and z+c<len(m)and m[z][y][x]==m[z+c][y+b][x+a] for a,b,c in [[1,0,0],[0,1,0],[0,0,1]]):return False
 return True

golf=lambda m:1^any(x+a-len(m)&y+b-len(m)&z+c-len(m)and m[z][y][x]==m[z+c][y+b][x+a]for a,b,c in[[1,0,0],[0,1,0],[0,0,1]]for z in range(len(m))for y in range(len(m))for x in range(len(m)))

if __name__ == '__main__':
	assert golf([[["X", "Z"],
		["Z", "X"]],
		[["Z", "X"],
		["X", "Z"]]])
	assert not golf([[["X", "Z"],
		["Z", "X"]],
		[["X", "Z"],
		["Z", "X"]]])