a=[1,2]
for i in range(2,1000):
	a.append(a[i-1]+a[i-2])
h={}
for e in a: h[e]=1
z=[10000]
for i in range(1,6000):
	z.append(z[i-1]+(-i if i in h else 1))

def checkio(opacity):
	for index,item in enumerate(z):
		if item==opacity: return index

#These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
	assert checkio(10000) == 0, "Newborn"
	assert checkio(9999) == 1, "1 year"
	assert checkio(9997) == 2, "2 years"
	assert checkio(9994) == 3, "3 years"
	assert checkio(9995) == 4, "4 years"
	assert checkio(9990) == 5, "5 years"