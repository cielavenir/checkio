X=3
Y=3
i=0
m={}
prev={}
v=[]
for i in range(1,X*Y): v.append(str(i))
v.append('0')
m[''.join(v)]=[8,0]
prev[''.join(v)]=[''.join(v),None]
q=[v]
while len(q)>0:
	v=q.pop(0)
	coor=m[''.join(v)][0]
	x=coor%X
	y=coor//X
	depth=m[''.join(v)][1]
	nextstr=''.join(v)
	if 0<x:
		v[coor],v[coor-1]=v[coor-1],v[coor]
		if ''.join(v) not in m:
			m[''.join(v)]=[coor-1,depth+1]
			q.append(v[:])
			prev[''.join(v)]=[nextstr,'R']
		v[coor],v[coor-1]=v[coor-1],v[coor]
	if x<X-1:
		v[coor],v[coor+1]=v[coor+1],v[coor]
		if ''.join(v) not in m:
			m[''.join(v)]=[coor+1,depth+1]
			q.append(v[:])
			prev[''.join(v)]=[nextstr,'L']
		v[coor],v[coor+1]=v[coor+1],v[coor]
	if 0<y:
		v[coor],v[coor-X]=v[coor-X],v[coor]
		if ''.join(v) not in m:
			m[''.join(v)]=[coor-X,depth+1]
			q.append(v[:])
			prev[''.join(v)]=[nextstr,'D']
		v[coor],v[coor-X]=v[coor-X],v[coor]
	if y<Y-1:
		v[coor],v[coor+X]=v[coor+X],v[coor]
		if ''.join(v) not in m:
			m[''.join(v)]=[coor+X,depth+1]
			q.append(v[:])
			prev[''.join(v)]=[nextstr,'U']
		v[coor],v[coor+X]=v[coor+X],v[coor]

def checkio(data):
	s=''.join(''.join(str(f) for f in e) for e in data)
	r=''
	while prev[s][1]:
		r+=prev[s][1]
		s=prev[s][0]
	return r

if __name__ == '__main__':
	print(checkio([[1, 2, 3],
				   [4, 6, 8],
				   [7, 5, 0]]))