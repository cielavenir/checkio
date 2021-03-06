def checkio(x):
	m={'(':')','{':'}','[':']'}
	s=[]
	for e in x:
		if e in'({[':s+=[m[e]]
		if e in')}]'and(not s or s.pop()!=e):return False
	return not s

if False:
	import sys
	if sys.version_info[0]>=3: raw_input=input
	n=int(raw_input())
	for _ in range(n):
		print(['NO','YES'][checkio(raw_input().strip())])
else:
	assert checkio("((5+3)*2+1)") == True, "Simple"
	assert checkio("{[(3+1)+2]+}") == True, "Different types"
	assert checkio("(3+{1-1)}") == False, ") is alone inside {}"
	assert checkio("[1+1]+(2*2)-{3/3}") == True, "Different operators"
	assert checkio("(({[(((1)-2)+3)-3]/3}-3)") == False, "One is redundant"