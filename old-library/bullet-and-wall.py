cross=lambda a,b: (a.conjugate()*b).imag
dot=lambda a,b: (a.conjugate()*b).real
def crosspoint(s0,s1,l0,l1):
	A = cross(l1-l0,s1-s0) # 
	B = cross(l1-l0,l1-s0)
	if abs(A)<1e-7:
		if abs(B)<1e-7:
			C=s0
		else:
			return -1
	else:
		C = s0 + B/A*(s1-s0)
	# now, C is the crosspoint of s0s1 and l0l1
	if dot(s0-C,s1-C)<1e-7 and dot(C-l0,l1-l0)>-1e-7: #C is on s0s1 and C is beyond l0
		ratio=2*abs(C-s0)/abs(s1-s0)
		if ratio>1: ratio=2-ratio
		#print(ratio)
		return round(100*ratio)
	else:
		return -1

shot=lambda *data: crosspoint(*[complex(*e) for e in data])
#old-library bullet-and-wall compatibility
checkio=lambda data: crosspoint(*[complex(*e) for e in data])>=0

if __name__ == '__main__':
	assert checkio([[0, 0], [0, 2], [5, 1], [3, 1]]) == True, "1st example"
	assert checkio([[0, 0], [0, 2], [3, 1], [5, 1]]) == False, "2nd example"
	assert checkio([[0, 0], [2, 2], [6, 0], [3, 1]]) == True, "3rd example"
	assert checkio([[6, 0], [5, 5], [4, 0], [5, 6]]) == False, "4th example"
	assert checkio([[0, 0], [1, 1], [3, 3], [2, 2]]) == True, "5th example"
	assert checkio([[0, 0], [1, 1], [3, 2], [2, 1]]) == False, "6th example"
	assert shot((2, 2), (5, 7), (11, 2), (8, 3)) == 100, "1st case"
	assert shot((2, 2), (5, 7), (11, 2), (7, 2)) == 0, "2nd case"
	assert shot((2, 2), (5, 7), (11, 2), (8, 4)) == 29, "3rd case"
	assert shot((2, 2), (5, 7), (11, 2), (9, 5)) == -1, "4th case"
	assert shot((2, 2), (5, 7), (11, 2), (10.5, 3)) == -1, "4th case again"
	assert shot((2, 2), (10, 2), (5, 10), (5, 5)) == 75
	assert shot((2, 10), (10, 2), (10, 10), (3, 9.9)) == 3