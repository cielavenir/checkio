def second_index(a,b):
	i=a.find(b)
	if i<0: return None
	a=a[i+1:]
	j=a.find(b)
	if j<0: return None
	return i+1+j
