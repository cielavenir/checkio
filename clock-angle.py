def clock_angle(s):
	h,m=[int(e) for e in s.split(':')]
	h=(30*h+m/2.0)%360
	m*=6
	return min(360-abs(h-m),abs(h-m))

if __name__=='__main__':
	print(clock_angle('02:30'))
	print(clock_angle('13:42'))