def checkio(x):
	m={'(':')','{':'}','[':']'}
	s=[]
	for e in x:
		if e in'({[':s+=[m[e]]
		if e in')}]'and(not s or s.pop()!=e):return False
	return not s

if __name__ == '__main__':
	assert checkio("((5+3)*2+1)") == True, "Simple"
	assert checkio("{[(3+1)+2]+}") == True, "Different types"
	assert checkio("(3+{1-1)}") == False, ") is alone inside {}"
	assert checkio("[1+1]+(2*2)-{3/3}") == True, "Different operators"
	assert checkio("(({[(((1)-2)+3)-3]/3}-3)") == False, "One is redundant"