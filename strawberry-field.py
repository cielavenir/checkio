import math
def strawberryfield(a,b,c,d):
	#a*a+d*d-2*a*d*cosx == b*b+c*c+2*b*c*cosx
	return round(math.acos((a*a+d*d-b*b-c*c)/(2.0*a*d+2*b*c))*180/math.pi,1)
