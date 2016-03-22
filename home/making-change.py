def checkio(price, denominations):
	a=[0]+[None]*price
	for i in range(1,price+1):
		for e in denominations:
			if i>=e and a[i-e] is not None and (a[i] is None or a[i]>a[i-e]+1): a[i]=a[i-e]+1
	return a[price]

if __name__ == '__main__':
	assert checkio(8, [1, 3, 5]) == 2
	assert checkio(12, [1, 4, 5]) == 3
	print('Done')