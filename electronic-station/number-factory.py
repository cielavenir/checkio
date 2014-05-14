def checkio(data):
	if data<1: return 0
	if data==1: return 1
	r=[]
	for i in range(9,1,-1):
		while data%i==0:
			r.append(str(i))
			data//=i
	if data>1: return 0
	return int(''.join(reversed(r)))

if __name__ == '__main__':
	assert checkio(20) == 45, "1st example"
	assert checkio(21) == 37, "2nd example"
	assert checkio(17) == 0, "3rd example"
	assert checkio(33) == 0, "4th example"
	assert checkio(5) == 5, "5th example"