import math as m
def checkio(h,w):
	e=(1-(1.*min(h,w)/max(h,w))**2)**.5
	return[round(m.pi/2*e*w,2)for e in[w*h/3.]+([w+h*h*m.atanh(e)/e/w]if h<w else[w+h*m.asin(e)/e]if h>w else[2*w])]

if __name__ == '__main__':
	assert checkio(4, 2) == [8.38, 21.48], "Prolate spheroid"
	assert checkio(2, 2) == [4.19, 12.57], "Sphere"
	assert checkio(2, 4) == [16.76, 34.69], "Oblate spheroid"

import cmath as m
def checkio(h,w):
	e=m.sqrt(1-(1.*w/h)**2)
	return[round((m.pi/2*e*w).real,2)for e in[w*h/3.]+([2*w] if h==w else[w+h*m.asin(e)/e])]