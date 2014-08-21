import re
def tryint(s):
	try:
		return int(s)
	except ValueError:
		return s

def natsort_key(s):
	return [ tryint(c) for c in re.split(r"((?:(?:(?<=[ ,])|^)-)?[0-9]+)", s) ]

def checkio(a):
	return sorted(a, key=natsort_key)

if __name__ == '__main__':
	assert checkio(["01","10","100","20","3"]) == ['01', '3', '10', '20', '100']
	assert checkio(["1.0a","10.0a","2.0b","2.0a","0.1"]) == ['0.1', '1.0a', '2.0a', '2.0b', '10.0a']
	print('Done')