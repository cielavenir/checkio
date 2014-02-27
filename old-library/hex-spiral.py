def convert(n):
	if n<1: return None
	if n==1: return [0,0,0]
	n-=2
	d=1
	s=6
	while s<=n:
		d+=1
		s+=d*6
	s-=d*6
	n-=s
	base=[-d+1,d,-1]
	for i in range(n):
		if i+1<d:
			base[0]+=1
			base[2]-=1
		elif i+1<d*2:
			base[0]+=1
			base[1]-=1
		elif i+1<d*3:
			base[1]-=1
			base[2]+=1
		elif i+1<d*4:
			base[0]-=1
			base[2]+=1
		elif i+1<d*5:
			base[0]-=1
			base[1]+=1
		else:
			base[1]+=1
			base[2]-=1
	return base

def checkio(data):
	a=convert(data[0])
	b=convert(data[1])
	#http://www.redblobgames.com/grids/hexagons/#distances
	return max(abs(a[0]-b[0]), abs(a[1]-b[1]), abs(a[2]-b[2]))

#These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
	assert checkio([2, 9]) == 1, "First"
	assert checkio([9, 2]) == 1, "Reverse First"
	assert checkio([6, 19]) == 2, "Second, short way"
	assert checkio([5, 11]) == 3, "Third"
	assert checkio([13, 15]) == 2, "Fourth, One row"
	assert checkio([11, 17]) == 4, "Fifth, One more test"