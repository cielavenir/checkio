def between_markers(t,a,b):
	i=t.find(a)
	if i>=0: i=i+len(a)
	else: i=0
	j=t.find(b)
	if j<=0: j=len(t)
	return t[i:j]
