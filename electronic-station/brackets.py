def checkio(expr):
	m={'(':')','{':'}','[':']'}
	stack=[]
	for e in expr:
		if e in ['(','{','[']: stack.append(m[e])
		elif e in [')','}',']']:
			if len(stack)==0 or stack.pop()!=e: return False
	return len(stack)==0

#These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
	assert checkio("((5+3)*2+1)") == True, "Simple"
	assert checkio("{[(3+1)+2]+}") == True, "Different types"
	assert checkio("(3+{1-1)}") == False, ") is alone inside {}"
	assert checkio("[1+1]+(2*2)-{3/3}") == True, "Different operators"
	assert checkio("(({[(((1)-2)+3)-3]/3}-3)") == False, "One is redundant"