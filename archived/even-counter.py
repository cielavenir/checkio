def checkio(number):
	if number==0: return 1
	r=0
	while number>0:
		if number%10%2==0: r+=1
		number//=10
	return r

if __name__ == '__main__':
	assert checkio(123456) == 3, '1st example'
	assert checkio(111111) == 0, '2nd example'
	assert checkio(24680) == 5, '3rd example'