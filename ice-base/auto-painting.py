import itertools

def checkio(capacity, number):
	d=min(capacity,number)
	number_str='0123456789'[:number]*2
	return ','.join(number_str[i:i+d] for i in range(0,number*2,d))

#These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
	print(checkio(2, 3))  # "01,12,02"
	print(checkio(6, 3))  # "012,012"
	print(checkio(3, 6))  # "012,012,345,345"
	print(checkio(1, 4))  # "0,0,1,1,2,2,3,3"
	print(checkio(2, 5))  # "01,01,23,42,34"