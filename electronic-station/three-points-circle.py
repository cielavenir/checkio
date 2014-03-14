import math,re

def checkio(data):
	a=[[float(f) for f in e.split(',')] for e in data[1:-1].split('),(')]
	x1=a[0][0]
	y1=a[0][1]
	x2=a[1][0]
	y2=a[1][1]
	x3=a[2][0]
	y3=a[2][1]
	a1=2*x2-2*x1
	b1=2*y2-2*y1
	c1=x1*x1-x2*x2+y1*y1-y2*y2
	a2=2*x3-2*x1
	b2=2*y3-2*y1
	c2=x1*x1-x3*x3+y1*y1-y3*y3
	x=(b1*c2-b2*c1)/(a1*b2-a2*b1)
	y=(c1*a2-c2*a1)/(a1*b2-a2*b1)
	#s='(x-%s)^2+(y-%s)^2=%s^2'%(str(round(x,2)),str(round(y,2)),str(round(math.hypot(x1-x,y1-y),2)))
	#return re.sub(r'\.0([^0-9])',r'\1',s) # aww I forgot this escape in first solution!
	return '(x-%s)^2+(y-%s)^2=%s^2'%(str(round(x,2)).rstrip('.0'),str(round(y,2)).rstrip('.0'),str(round(math.hypot(x1-x,y1-y),2)).rstrip('.0'))

#These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
	assert checkio("(2,2),(6,2),(2,6)") == "(x-4)^2+(y-4)^2=2.83^2"
	assert checkio("(3,7),(6,9),(9,7)") == "(x-6)^2+(y-5.75)^2=3.25^2"