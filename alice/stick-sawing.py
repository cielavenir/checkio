def checkio(number):
	start=1
	while start*(start+1)//2<=number:
		s=0
		n=start
		while s<number:
			s+=n*(n+1)//2
			n+=1
		if s==number:
			return [e*(e+1)//2 for e in range(start,n)]
		start+=1
	return []

if __name__ == '__main__':
	assert checkio(64) == [15, 21, 28], "1st example"
	assert checkio(371) == [36, 45, 55, 66, 78, 91], "1st example"
	assert checkio(225) == [105, 120], "1st example"
	assert checkio(882) == [], "1st example"