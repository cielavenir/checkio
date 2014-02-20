import math

def checkio(height, width):
	height/=2.0
	width/=2.0
	e=math.sqrt(1-(min(height,width)/max(height,width))**2)
	if height<width:
		return [4.0/3*math.pi*width*width*height,2*math.pi*(width*width+height*height*math.atanh(e)/e)]
	elif height>width:
		return [4.0/3*math.pi*width*width*height,2*math.pi*(width*width+width*height*math.asin(e)/e)]
	else:
		return [4.0/3*math.pi*width*width*height,4*math.pi*width*width]

#These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
	assert checkio(4, 2) == [8.38, 21.48], "Prolate spheroid"
	assert checkio(2, 2) == [4.19, 12.57], "Sphere"
	assert checkio(2, 4) == [16.76, 34.69], "Oblate spheroid"