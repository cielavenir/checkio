def checkio(radius):
	r=int(radius)+1
	h={}
	for i in range(r):
		for j in range(r):
			if i**2+j**2<radius**2: h[i<<16|j]=1
	x=y=0
	for i in range(r):
		for j in range(r):
			if i<<16|j in h:
				if (i+1)<<16|j in h and i<<16|(j+1) in h and (i+1)<<16|(j+1) in h: x+=1
				else: y+=1
	return [x*4, y*4]

#These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
	assert checkio(2) == [4, 12], "N=2"
	assert checkio(3) == [16, 20], "N=3"
	assert checkio(2.1) == [4, 20], "N=2.1"
	assert checkio(2.5) == [12, 20], "N=2.5"