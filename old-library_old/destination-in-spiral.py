def convert(n):
	if n<1: return None
	if n==1: return [0,0]
	n-=2
	d=1
	s=8
	while s<=n:
		d+=1
		s+=d*8
	s-=d*8
	n-=s
	base=[-d,-d+1]
	for i in range(n):
		if i+1<d*2:
			base[1]+=1
		elif i+1<d*4:
			base[0]+=1
		elif i+1<d*6:
			base[1]-=1
		else:
			base[0]-=1
	return base

def find_distance(first,second):
	a=convert(first)
	b=convert(second)
	return abs(a[0]-b[0])+abs(a[1]-b[1])

#old library destination-in-spiral compatibility
checkio=lambda data:find_distance(data[0],data[1])

if __name__ == '__main__':
	assert checkio([1, 9]) == 2, "First"
	assert checkio([9, 1]) == 2, "Reverse First"
	assert checkio([10, 25]) == 1, "Neighbours"
	assert checkio([5, 9]) == 4, "Diagonal"
	assert checkio([26, 31]) == 5, "One row"
	assert checkio([50, 16]) == 10, "One more test"