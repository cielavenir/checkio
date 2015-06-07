def f(n):
	if n==1:return[0,0]
	n-=2
	d=s=0
	while s<=n:
		d+=1
		s+=d*8
	n-=(s-d*8)
	print(n,d)
	r=[-d,-d+1]
	#for i in range(1,n+1):r[i//(d*2)%2^1]+=(-1)**(i//(d*4))
	for i in range(1,n+1):
		if i<d*2:r[1]+=1
		elif i<d*4:r[0]+=1
		elif i<d*6:r[1]-=1
		else:r[0]-=1
	return r
def find_distance(p,q):
	a=f(p)
	b=f(q)
	return abs(a[0]-b[0])+abs(a[1]-b[1])

#old library destination-in-spiral compatibility
checkio=lambda data:find_distance(*data)

if __name__ == '__main__':
	assert checkio([1, 9]) == 2, "First"
	assert checkio([9, 1]) == 2, "Reverse First"
	assert checkio([10, 25]) == 1, "Neighbours"
	assert checkio([5, 9]) == 4, "Diagonal"
	assert checkio([26, 31]) == 5, "One row"
	assert checkio([50, 16]) == 10, "One more test"