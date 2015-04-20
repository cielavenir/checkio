from functools import reduce
def egcd(x,y):
	if y==0: return (x,1,0)
	g,a,b=egcd(y,x%y)
	return (g,b,a-x//y*b)

def perform(a1,m1,a2,m2):
	g,x,y=egcd(m1,m2)
	if (a2-a1)%g>0: raise ValueError
	l=m1//g*m2
	return ((a1+(a2-a1)//g*x*m1)%l,l)

def checkio(a):
	if not a: return None
	try:
		return reduce(lambda x,y:perform(*(x+y)),a)[0]
	except ValueError:
		return None

if __name__ == '__main__':
	assert (checkio([(2, 3), (3, 5), (2, 7)]) == 23), "First Test"
	assert (checkio([(1, 5), (4, 7)]) == 11), "Second Test"
	assert (checkio([(1, 3), (2, 5), (3, 7)]) == 52), "Third Test"
	assert (checkio([(1, 2), (1, 3), (1, 5)]) == 1), "Fourth Test"
	assert (checkio([(2, 4), (7, 9)]) == 34), "Fifth Test"
	assert (checkio([(1, 2), (1, 3), (3, 4)]) == 7), "Extra 1"
	assert (checkio([(1, 2), (0, 4)]) is None), "Extra 2"
	print('All done!')