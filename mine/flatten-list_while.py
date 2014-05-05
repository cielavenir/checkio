def flat_list(a):
	while True:
		b=[]
		for e in a:
			try:
				b+=e
			except TypeError:
				b.append(e)
		if b==a: return b
		a=b