eps=10e-15
def super_root(number):
	l=1.0
	h=10.0 # fixme
	while h-l>eps:
		m=(l+h)/2
		if m**m<number:
			l=m
		else:
			h=m
	return l

if __name__ == '__main__':
	def check_result(function, number):
		result = function(number)
		if not isinstance(result, (int, float)):
			print("The result should be a float or an integer.")
			return False
		p = result ** result
		if number - 0.001 < p < number + 0.001:
			return True
		return False
	assert check_result(super_root, 4), "Square"
	assert check_result(super_root, 9), "Cube"
	assert check_result(super_root, 81), "Eighty one"