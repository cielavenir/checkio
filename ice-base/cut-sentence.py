def cut_sentence(s,n):
	if len(s)<=n: return s
	while len(s)>n:
		try:
			idx=s.rindex(' ')
		except ValueError:
			idx=0
		s=s[:idx]
	return s+'...'
