def checkio(number):
	i=number-1
	while True:
		i+=1
		s=str(i)
		if s!=s[::-1]: continue
		j=2
		while j*j<=i:
			if i%j==0: break
			j+=1
		if j*j>i: return i

#These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
	assert checkio(31) == 101, 'First example'
	assert checkio(130) == 131, 'Second example'
	assert checkio(131) == 131, 'Third example'