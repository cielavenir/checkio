def is_stressful2(s,x):
	try:
		for c in x:
			idx=s.index(c)
			s=s[idx+1:]
		return True
	except ValueError:
		return False

def is_stressful(s):
	t=s.upper()
	if s==t: return True
	if s.endswith('!!!'): return True
	return any(is_stressful2(t,x) for x in ['HELP','ASAP','URGENT'])
