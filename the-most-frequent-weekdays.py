def zeller(_y,m,d):
	m+=1
	if m<4: _y-=1;m+=12
	y=_y//100
	z=_y%100
	return (5*y+z+y//4+z//4+13*m//5+d-1)%7

def leap(y):
	if y%400==0: return True
	if y%100==0: return False
	return y%4==0

WDAY=['Monday','Tuesday','Wednesday','Thursday','Friday','Saturday','Sunday']
def most_frequent_days(y):
	d=zeller(y,1,1)
	r=[(d+6)%7]
	if leap(y): r.append(d)
	return [WDAY[d] for d in sorted(r)]

if __name__ == '__main__':
	assert most_frequent_days(2399) ==  ['Friday'], "1st example"
	assert most_frequent_days(1152) == ['Tuesday', 'Wednesday'], "2nd example"
	assert most_frequent_days(56) == ['Saturday', 'Sunday'], "3rd example"
	assert most_frequent_days(2909) == ['Tuesday'], "4th example"