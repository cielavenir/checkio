def convert(numerator,denominator):
	if numerator==0: return '0.'
	if numerator%denominator==0: return str(numerator//denominator)+'.'
	head=str(numerator//denominator)+'.'
	numerator%=denominator
	tail=''
	while True:
		numerator*=10
		d=numerator//denominator
		tail+=str(d)
		numerator%=denominator
		if numerator==0: return head+tail
		tail_rev=tail[::-1]
		for i in range(1,len(tail_rev)//3+1):
			if all(tail_rev[j]==tail_rev[i+j] and tail_rev[i+j]==tail_rev[2*i+j] for j in range(i)):
				return head+tail_rev[i*3:][::-1]+'('+tail_rev[0:i][::-1]+')'

#old library repeating-decimal compatibility
checkio=lambda data:convert(*data)

if __name__ == '__main__':
	assert checkio([1, 3]) == "0.(3)", "1/3 Classic"
	assert checkio([5, 3]) == "1.(6)", "5/3 The same, but bigger"
	assert checkio([3, 8]) == "0.375", "3/8 without repeating part"
	assert checkio([7, 11]) == "0.(63)", "7/11 prime/prime"
	assert checkio([29, 12]) == "2.41(6)", "29/12 not and repeating part"
	assert checkio([11, 7]) == "1.(571428)", "11/7 six digits"