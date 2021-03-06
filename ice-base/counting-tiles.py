z=lambda i,j,r:i**2+j**2<r**2
def checkio(R):
	r=int(R)+1
	x=y=0
	for i in range(r):
		for j in range(r):
			if z(i,j,R):
				y+=1
				x+=z(i+1,j+1,R)
	return[x*4,(y-x)*4]

f=lambda R,r,k:sum((i+k)**2+(j+k)**2<R**2 for i in range(r) for j in range(r))
def golf(R):
	r=int(R)+1
	return [4*f(R,r,1),4*(f(R,r,0)-f(R,r,1))]

if __name__ == '__main__':
	assert checkio(2) == [4, 12], "N=2"
	assert checkio(3) == [16, 20], "N=3"
	assert checkio(2.1) == [4, 20], "N=2.1"
	assert checkio(2.5) == [12, 20], "N=2.5"