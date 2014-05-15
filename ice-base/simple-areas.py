'''
import math
def simple_areas(*args):
	if len(args)==1: return math.pi*(args[0]*.5)**2
	if len(args)==2: return args[0]*args[1]
	s=sum(args)*.5
	return math.sqrt(s*(s-args[0])*(s-args[1])*(s-args[2]))
'''

simple_areas=lambda *args:__import__('math').pi*(args[0]*.5)**2 if len(args)==1 else args[0]*args[1] if len(args)==2 else (sum(e**2 for e in args)**2-2*sum(e**4 for e in args))**.5/4

if __name__ == '__main__':
	def almost_equal(checked, correct, significant_digits=2):
		precision = 0.1 ** significant_digits
		return correct - precision < checked < correct + precision
	assert almost_equal(simple_areas(3), 7.07), "Circle"
	assert almost_equal(simple_areas(2, 2), 4), "Square"
	assert almost_equal(simple_areas(2, 3), 6), "Rectangle"
	assert almost_equal(simple_areas(3, 5, 4), 6), "Triangle"
	assert almost_equal(simple_areas(1.5, 2.5, 2), 1.5), "Small triangle"