def checkio(data):
	ndata=[e if isinstance(e,int) else e.lower() for e in data]
	ret=[]
	for e in data:
		if ndata.count(e if isinstance(e,int) else e.lower())>1: ret.append(e)
	return ret

if __name__ == "__main__":
	assert isinstance(checkio([1]), list), "The result must be a list"
	assert checkio([1, 2, 3, 1, 3]) == [1, 3, 1, 3], "1st example"
	assert checkio([1, 2, 3, 4, 5]) == [], "2nd example"
	assert checkio([5, 5, 5, 5, 5]) == [5, 5, 5, 5, 5], "3rd example"
	assert checkio([10, 9, 10, 10, 9, 8]) == [10, 9, 10, 10, 9], "4th example"