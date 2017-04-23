def is_stressful(s):
	s=s.upper()
	try:
		for c in 'HELP':
			idx=s.index(c)
			s=s[idx+1:]
		return True
	except ValueError:
		return False
