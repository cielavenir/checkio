'''
def checkio(array):
	if not len(array): return 0
	m=array[-1]
	r=0
	for i,e in enumerate(array):
		if i%2==0: r+=e
	return r*m
'''
checkio=lambda a: 0 if len(a)==0 else sum(a[0::2])*a[-1]

#These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
	assert checkio([0, 1, 2, 3, 4, 5]) == 30, "(0+2+4)*5=30"
	assert checkio([1, 3, 5]) == 30, "(1+5)*5=30"
	assert checkio([6]) == 36, "(6)*6=36"
	assert checkio([]) == 0, "Empty"