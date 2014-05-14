def checkio(first, second, goal):
	back={(0,0):None}
	back_perform={(0,0):None}
	q=[(0,0)]
	while len(q)>0:
		x=q[0]
		if x[0]==goal or x[1]==goal: break
		q.pop(0)
		a=[
			('01',(first,x[1])),
			('02',(x[0],second)),
			('10',(0,x[1])),
			('20',(x[0],0)),
			('12',(x[0]-min(x[0],second-x[1]),x[1]+min(x[0],second-x[1]))),
			('21',(x[0]+min(first-x[0],x[1]),x[1]-min(first-x[0],x[1]))),
		]
		for e in a:
			if e[1] not in back:
				back[e[1]]=x
				back_perform[e[1]]=e[0]
				q.append(e[1])
	if len(q)==0: return []
	r=[]
	while back[x]:
		r.append(back_perform[x])
		x=back[x]
	return list(reversed(r))

if __name__ == '__main__':
	print(checkio(5, 7, 6))	# ['02', '21', '10', '21', '02', '21', '10', '21', '02', '21']
	print(checkio(3, 4, 1))	# ["02", "21"]