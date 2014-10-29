cross=lambda a,b: (a.conjugate()*b).imag
dot=lambda a,b: (a.conjugate()*b).real

def solve(poly, p):
	f=False
	for i in range(len(poly)):
		a=poly[i]-p
		b=poly[(i+1)%len(poly)]-p
		if a.imag>b.imag: a,b=b,a
		if a.imag<=0 and 0<b.imag and cross(a,b)<0: f=not f
		if cross(a,b)==0 and dot(a,b)<=0: return True
	return f

is_inside=lambda data: solve([complex(*e) for e in data[0]],complex(*data[1]))
#old library target-hit compatibility
checkio=is_inside

if __name__ == '__main__':
	assert checkio([[[1, 1], [1, 3], [3, 3], [3, 1]], [2, 2]]) == True, "First"
	assert checkio([[[1, 1], [1, 3], [3, 3], [3, 1]], [4, 2]]) == False, "Second"
	assert checkio([[[1, 1], [4, 1], [2, 3]], [3, 2]]) == True, "Third"
	assert checkio([[[1, 1], [4, 1], [1, 3]], [3, 3]]) == False, "Fourth"
	assert checkio([[[2, 1], [4, 1], [5, 3], [3, 4], [1, 3]], [4, 3]]) == True, "Fifth"
	assert checkio([[[2, 1], [4, 1], [3, 2], [3, 4], [1, 3]], [4, 3]]) == False, "Sixth"
	assert checkio([[[1, 1], [3, 2], [5, 1], [4, 3], [5, 5], [3, 4], [1, 5], [2, 3]], [3, 3]]) == True, "Seventh"
	assert checkio([[[1, 1], [1, 5], [5, 5], [5, 4], [2, 4], [2, 2], [5, 2], [5, 1]], [4, 3]]) == False, "Eighth"