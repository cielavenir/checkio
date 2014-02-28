def checkio(text):
	a=text.split()
	for i in range(len(a)):
		if a[i].isdigit():
			s=a[i][::-1]
			a[i]='.'.join(reversed([s[j:j+3][::-1] for j in range(0,len(s),3)]))
	return ' '.join(a)

#These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
	assert checkio('123456') == '123.456', "1st example"
	assert checkio('333') == '333', "2nd example"
	assert checkio('9999999') == '9.999.999', "3rd example"
	assert checkio('123456 567890') == '123.456 567.890', "4th example"
	assert checkio('price is 5799') == 'price is 5.799', "5th example"
	assert checkio('he was born in 1966th') == 'he was born in 1966th', "6th example"