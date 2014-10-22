def clock_angle(s):
	h,m=[int(e) for e in s.split(':')]
	h=(30*h+m/2.0)%360
	m*=6
	return min(360-abs(h-m),abs(h-m))

if __name__=='__main__':
	assert clock_angle("02:30") == 105, "02:30"
	assert clock_angle("13:42") == 159, "13:42"
	assert clock_angle("01:42") == 159, "01:42"
	assert clock_angle("01:43") == 153.5, "01:43"
	assert clock_angle("00:00") == 0, "Zero"
	assert clock_angle("12:01") == 5.5, "Little later"
	assert clock_angle("18:00") == 180, "Opposite"