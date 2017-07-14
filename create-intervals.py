def create_intervals(data):
	data=sorted(list(data))
	r=[]
	st=n=data[0]
	for i in range(1,len(data)):
		if data[i]-n>1:
			r.append((st,n))
			st=data[i]
		n=data[i]
	r.append((st,n))
	return r
