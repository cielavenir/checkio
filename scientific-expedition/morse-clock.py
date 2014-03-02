def checkio(data):
	x=('..','.-','-.','--')
	y=('...','..-','.-.','.--','-..','-.-','--.','---')
	z=('....','...-','..-.','..--','.-..','.-.-','.--.','.---','-...','-..-')
	a=[int(e) for e in data.split(':')]
	return x[a[0]//10]+' '+z[a[0]%10]+' : '+y[a[1]//10]+' '+z[a[1]%10]+' : '+y[a[2]//10]+' '+z[a[2]%10]

#These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
	assert checkio("10:37:49") == ".- .... : .-- .--- : -.. -..-", "First Test"
	assert checkio("21:34:56") == "-. ...- : .-- .-.. : -.- .--.", "Second Test"
	assert checkio("00:1:02") == ".. .... : ... ...- : ... ..-.", "Third Test"
	assert checkio("23:59:59") == "-. ..-- : -.- -..- : -.- -..-", "Fourth Test"