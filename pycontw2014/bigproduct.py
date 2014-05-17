def checkio(l, n):
	ret=0
	c=1
	m=l[0]
	for i in range(1,len(l)):
		#if l[i-1]<l[i]:
			c+=1
			m*=l[i]
			if c>n:
				c-=1
				m//=l[i-n]
			if c==n:
				ret=max(ret,m)
		#else:
		#	c=1
		#	m=l[i]
	return ret

if __name__ == '__main__':
	assert checkio([1,2,3,5,1,6,1], 2) == 15
	assert checkio([1,3,4,5,2,6,7,2], 3) == 84
	print('Done')