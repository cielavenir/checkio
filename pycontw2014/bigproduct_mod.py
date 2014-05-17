def checkio(l, n):
	m=1
	for i in range(n): m*=l[i]
	ret=0
	for i in range(n,len(l)):
		m*=l[i]
		m//=l[i-n]
		ret=max(ret,m)
	return ret

if __name__ == '__main__':
	assert checkio([1,2,3,5,1,6,1], 2) == 15
	assert checkio([1,3,4,5,2,6,7,2], 3) == 84
	print('Done')