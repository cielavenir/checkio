def checkio(balance, withdrawal):
	for e in withdrawal:
		if e>0 and e%5==0 and balance>=e+1:
			balance-=e+1
	return balance

if __name__ == '__main__':
	assert checkio(120, [10, 20, 30]) == 57, 'First example'
	# With one Insufficient Funds, and then withdraw 10 $
	assert checkio(120, [200, 10]) == 109, 'Second example'
	#with one incorrect amount
	assert checkio(120, [3, 10]) == 109, 'Third example'
	assert checkio(120, [200, 119]) == 120, 'Fourth example'
	assert checkio(120, [120, 10, 122, 2, 10, 10, 30, 1]) == 56, "It's mixed all base tests"
	assert checkio(120, [-10]) == 120, 'Negative value'