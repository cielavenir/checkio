cross=lambda a1, b1, a2, b2: a1*b2-a2*b1
def checkio(a):
	n=len(a)
	s=0
	t=0
	for i in range(n-1):
		x=cross(a[i][0],a[i][1],a[i+1][0],a[i+1][1])
		if x>0: s+=abs(x)/2.0
		else: t+=abs(x)/2.0
	x=cross(a[n-1][0],a[n-1][1],a[0][0],a[0][1])
	if x>0: s+=abs(x)/2.0
	else: t+=abs(x)/2.0
	return abs(s-t)

if __name__ == '__main__':
	assert checkio([[1, 1], [9, 9], [9, 1]]) == 32, "The half of the square"
	assert checkio([[4, 10], [7, 1], [1, 4]]) == 22.5, "Triangle"
	assert checkio([[1, 2], [3, 8], [9, 8], [7, 1]]) == 40, "Quadrilateral"
	assert checkio([[3, 3], [2, 7], [5, 9], [8, 7], [7, 3]]) == 26, "Pentagon"
	assert checkio([[7, 2], [3, 2], [1, 5],
					[3, 9], [7, 9], [9, 6]]) == 42, "Hexagon"
	assert checkio([[4, 1], [3, 4], [3, 7], [4, 8],
					[7, 9], [9, 6], [7, 1]]) == 35.5, "Heptagon"