def bfs(data,s,g,dcur):
	D='URDL'
	back={s:None}
	backstr={}
	q=[s]
	while len(q)>0:
		x,y=q[0]
		if x==g[0] and y==g[1]: break
		q.pop(0)
		for dx,dy,d in [(0,-1,0),(1,0,1),(0,1,2),(-1,0,3)]:
			if 0<=x+dx<len(data[0]) and 0<=y+dy<len(data) and (data[y+dy][x+dx]=='.' or data[y+dy][x+dx]=='C') and (x+dx,y+dy) not in back:
				q.append((x+dx,y+dy))
				back[(x+dx,y+dy)]=(x,y)
				backstr[(x+dx,y+dy)]=d
	if len(q)==0: return None
	r=[]
	while back[g]:
		r.append(backstr[g])
		g=back[g]
	ret=''
	for e in reversed(r):
		if dcur==e:
			ret+='F'
		elif (e-dcur+4)%4==1:
			ret+='R'
			dcur=(dcur+1)%4
		elif (dcur-e+4)%4==1:
			ret+='L'
			dcur=(dcur-1+4)%4
		else:
			return None
	return ret

def checkio(field_map):
	zero=None
	one=None
	cherry=None
	for y in range(len(field_map)):
		for x in range(len(field_map[0])):
			if field_map[y][x]=='0': zero=(x,y)
			if field_map[y][x]=='1': one=(x,y)
			if field_map[y][x]=='C': cherry=(x,y)
	if zero[1]-one[1]==1: dcur=2
	if one[0]-zero[0]==1: dcur=3
	if one[1]-zero[1]==1: dcur=0
	if zero[0]-one[0]==1: dcur=1
	return bfs(field_map,zero,cherry,dcur)

#These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
	print(checkio([
		".T.....T..",
		".C........",
		".....T....",
		"..T....T..",
		"..........",
		".0...T....",
		".1........",
		".2.T...T..",
		".3...T....",
		".4........"
	]))