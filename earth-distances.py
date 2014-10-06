#coding:utf-8
#Unicode translate is supported only by Py3
import math

def process(arg):
	a=arg.translate(str.maketrans(u'°′″,',u'    ')).split()
	north=float(a[0])+float(a[1])/60+float(a[2])/3600
	if a[3]=='S': north=-north
	east=float(a[4])+float(a[5])/60+float(a[6])/3600
	if a[7]=='W': east=-east	
	return (east*math.pi/180,north*math.pi/180)

def distance(*args):
	coor1,coor2=[process(e) for e in args]
	return 6371*math.acos( (math.sin(coor1[1])*math.sin(coor2[1])+math.cos(coor1[1])*math.cos(coor2[1])*math.cos(coor1[0]-coor2[0])) )

if __name__ == '__main__':
	def almost_equal(checked, correct, significant_digits=1):
		precision = 0.1 ** significant_digits
		return correct - precision < checked < correct + precision
	assert almost_equal(
		distance(u"51°28′48″N 0°0′0″E", u"46°12′0″N, 6°9′0″E"), 739.2), "From Greenwich to Geneva"
	assert almost_equal(
		distance(u"90°0′0″N 0°0′0″E", u"90°0′0″S, 0°0′0″W"), 20015.1), "From South to North"
	assert almost_equal(
		distance(u"33°51′31″S, 151°12′51″E", u"40°46′22″N 73°59′3″W"), 15990.2), "Opera Night"