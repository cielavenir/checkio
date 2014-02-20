#Accoding to https://github.com/Bryukh-Checkio-Tasks/checkio-task-loading-cargo/blob/master/verification/tests.py ,
#max(len(data)) is 10. Thus O(2^n) is applicable.

def checkio(data):
	if len(data)==0: return 0
	if len(data)==1: return data[0]
	ret=sum(data)
	for i in range(1,1<<(len(data)-1)):
		l=0
		r=0
		for j,e in enumerate(data):
			if i&(1<<j): l+=e
			else: r+=e
		ret=min(ret,abs(l-r))
	return ret

#These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
	assert checkio([10, 10]) == 0, "1st example"
	assert checkio([10]) == 10, "2nd example"
	assert checkio([5, 8, 13, 27, 14]) == 3, "3rd example"
	assert checkio([5, 5, 6, 5]) == 1, "4th example"
	assert checkio([12, 30, 30, 32, 42, 49]) == 9, "5th example"
	assert checkio([1, 1, 1, 3]) == 0, "6th example"
