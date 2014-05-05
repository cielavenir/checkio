import math
def simple_areas(*args):
	if len(args)==1: return math.pi*(args[0]*.5)**2
	if len(args)==2: return args[0]*args[1]
	s=sum(args)*.5
	return math.sqrt(s*(s-args[0])*(s-args[1])*(s-args[2]))

if __name__ == '__main__':
	#These "asserts" using only for self-checking and not necessary for auto-testing
	assert simple_areas(3) == 7.07, "Circle"
	assert simple_areas(2, 2) == 4, "Square"
	assert simple_areas(2, 3) == 6, "Rectangle"
	assert simple_areas(3, 5, 4) == 6, "Triangle"
	assert simple_areas(1.5, 2.5, 2) == 1.5, "Small triangle"