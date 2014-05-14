import math
angle=lambda a,b,c: round( 180*math.acos((a*a+b*b-c*c)/2.0/a/b)/math.pi )
solve=lambda x: [0,0,0] if x[0]+x[1]<=x[2] else sorted([angle(*x[i:]+x[:i]) for i in range(3)])
checkio=lambda a,b,c: solve([a,b,c])

if __name__ == '__main__':
	assert checkio(4, 4, 4) == [60, 60, 60], "All sides are equal"
	assert checkio(3, 4, 5) == [37, 53, 90], "Egyptian triangle"
	assert checkio(2, 2, 5) == [0, 0, 0], "It's can not be a triangle"