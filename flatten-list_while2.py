def flat_list(a):
	while True:
		b=[]
		for e in a: b+=e if isinstance(e,list) else [e]
		if b==a: return b
		a=b