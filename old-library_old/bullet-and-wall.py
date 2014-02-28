cross=lambda a,b: (a.conjugate()*b).imag
dot=lambda a,b: (a.conjugate()*b).real
def crosspoint(s0,s1,l0,l1):
	A = cross(l1-l0,s1-s0)
	B = cross(l1-l0,l1-s0)
	if abs(A)<1e-7:
		if abs(B)<1e-7:
			C=s0
		else:
			return False
	else:
		C = s0 + B/A*(s1-s0)
	return dot(s0-C,s1-C)<1e-7 and dot(C-l0,l1-l0)>-1e-7

checkio=lambda data: crosspoint(*[complex(*e) for e in data])

#These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
	assert checkio([[0, 0], [0, 2], [5, 1], [3, 1]]) == True, "1st example"
	assert checkio([[0, 0], [0, 2], [3, 1], [5, 1]]) == False, "2nd example"
	assert checkio([[0, 0], [2, 2], [6, 0], [3, 1]]) == True, "3rd example"
	assert checkio([[6, 0], [5, 5], [4, 0], [5, 6]]) == False, "4th example"
	assert checkio([[0, 0], [1, 1], [3, 3], [2, 2]]) == True, "5th example"
	assert checkio([[0, 0], [1, 1], [3, 2], [2, 1]]) == False, "6th example"