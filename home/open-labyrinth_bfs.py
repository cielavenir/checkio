def checkio(data):
	back={(1,1):None}
	backstr={}
	q=[(1,1)]
	g=(len(data[0])-2,len(data)-2)
	while len(q)>0:
		x,y=q[0]
		if x==g[0] and y==g[1]: break
		q.pop(0)
		for dx,dy,d in [(-1,0,'W'),(0,1,'S'),(1,0,'E'),(0,-1,'N')]:
			if data[y+dy][x+dx]==0 and (x+dx,y+dy) not in back:
				q.append((x+dx,y+dy))
				back[(x+dx,y+dy)]=(x,y)
				backstr[(x+dx,y+dy)]=d
	if len(q)==0: return None
	r=''
	while back[g]:
		r+=backstr[g]
		g=back[g]
	return r[::-1]

#This code using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
	print(checkio([
		[1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
		[1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
		[1, 0, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1],
		[1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1],
		[1, 0, 1, 0, 1, 1, 1, 1, 1, 1, 0, 1],
		[1, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 1],
		[1, 0, 0, 0, 1, 1, 0, 1, 1, 1, 0, 1],
		[1, 0, 1, 0, 0, 0, 0, 1, 0, 1, 1, 1],
		[1, 0, 1, 1, 0, 1, 0, 0, 0, 0, 0, 1],
		[1, 0, 1, 0, 0, 1, 1, 1, 1, 1, 0, 1],
		[1, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 1],
		[1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]]))
	print(checkio([
		[1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
		[1, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 1],
		[1, 0, 1, 0, 1, 0, 1, 0, 1, 1, 0, 1],
		[1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 0, 1],
		[1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 1],
		[1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 0, 1],
		[1, 0, 1, 0, 1, 0, 1, 0, 1, 1, 0, 1],
		[1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 0, 1],
		[1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 1],
		[1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 0, 1],
		[1, 0, 0, 0, 1, 0, 0, 0, 1, 1, 0, 1],
		[1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
	]))
	#be careful with infinity loop
	print(checkio([
		[1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
		[1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
		[1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
		[1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
		[1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
		[1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
		[1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
		[1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
		[1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
		[1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
		[1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
		[1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
	]))
	print(checkio([
		[1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
		[1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 1],
		[1, 0, 1, 0, 0, 0, 1, 0, 0, 0, 1, 1],
		[1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 1],
		[1, 0, 1, 0, 0, 0, 1, 0, 0, 0, 1, 1],
		[1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 1],
		[1, 0, 1, 0, 0, 0, 1, 0, 0, 0, 1, 1],
		[1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 1],
		[1, 0, 1, 0, 0, 0, 1, 0, 0, 0, 1, 1],
		[1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 1],
		[1, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 1],
		[1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
	]))
	print(checkio([
		[1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
		[1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1],
		[1, 0, 1, 1, 0, 1, 0, 1, 1, 1, 0, 1],
		[1, 0, 1, 1, 0, 1, 0, 1, 0, 1, 0, 1],
		[1, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 1],
		[1, 1, 1, 1, 1, 1, 0, 1, 0, 0, 0, 1],
		[1, 0, 0, 0, 0, 1, 1, 1, 0, 1, 1, 1],
		[1, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 1],
		[1, 0, 1, 1, 0, 1, 1, 1, 1, 1, 0, 1],
		[1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1],
		[1, 0, 1, 0, 1, 0, 1, 1, 0, 0, 0, 1],
		[1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
	]))