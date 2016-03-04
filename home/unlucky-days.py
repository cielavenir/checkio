def zeller(_y,m,d):
	m+=1
	if m<4: _y-=1;m+=12
	y=_y//100
	z=_y%100
	return (5*y+z+y//4+z//4+13*m//5+d-1)%7

checkio=lambda y: sum(zeller(y,m,13)==5 for m in range(1,13))

if __name__ == '__main__':
	assert checkio(2015) == 3, "First - 2015"
	assert checkio(1986) == 1, "Second - 1986"