if isinstance(__builtins__,dict):
	min=__builtins__['min']
	max=__builtins__['max']
else:
	min=__builtins__.min
	max=__builtins__.max

if __name__ == '__main__':
	assert max(3, 2) == 3, "Simple case max"
	assert min(3, 2) == 2, "Simple case min"
	assert max([1, 2, 0, 3, 4]) == 4, "From a list"
	assert min("hello") == "e", "From string"
	assert max(2.2, 5.6, 5.9, key=int) == 5.6, "Two maximal items"
	assert min([[1, 2], [3, 4], [9, 0]], key=lambda x: x[1]) == [9, 0], "lambda key"