WHITESPACE_STR = ' \t\n\r'

def parse_array(s, _w=WHITESPACE_STR, _sep=","):
	array = None
	stack = []
	accumulator = ""
	flag = False
	for ch in s:
		if ch in _w:
			continue
		if ch == "[":
			in_array = []
			if stack:
				stack[-1](in_array)
			else:
				array = in_array
			stack.append(in_array.append)
		elif ch == "]":
			if not stack:
				raise ValueError("Wrong string.")
			if accumulator:
				stack[-1](int(accumulator))
				accumulator = ""
				flag = True
			stack.pop()
		elif ch in _sep:
			if accumulator:
				stack[-1](int(accumulator))
				accumulator = ""
			elif flag:
				flag = False
			else:
				raise ValueError("Wrong string.")
		else:
			accumulator += ch
	if not array is None and not stack:
		return array
	else:
		raise ValueError("Wrong string")

if __name__ == "__main__":
	assert parse_array("[1, 2, 3]") == [1, 2, 3], "Simple"
	assert parse_array("[[1], 2, 3]") == [[1], 2, 3], "Nested"
	assert parse_array("[-3, [-2, 0], 10]") == [-3, [-2, 0], 10], "Negative integers"
	assert parse_array("[100]") == [100], "One number"
	assert parse_array("[2,	 3]") == [2, 3], "Whitespaces"
	assert parse_array("[[10, [11]], [[[1], 2], 3], 5]") == [[10, [11]], [[[1], 2], 3], 5], "Deep nested"
	assert parse_array("   [3, 4]   ") == [3, 4], "Skip whitespaces"
	try:
		parse_array("[asd]")
		assert False, "Only integers"
	except ValueError:
		pass
	try:
		parse_array("[2, 3]]")
		assert False, "Excess bracket"
	except ValueError:
		pass
	try:
		parse_array("[++2, 1]")
		assert False, "Two plus"
	except ValueError:
		pass
	try:
		parse_array("[10, 11, , 12]")
		assert False, "Two separators"
	except ValueError:
		pass
	try:
		parse_array(" 13 ")
		assert False, "Where is a list?"
	except ValueError:
		pass
	try:
		parse_array("[[2]")
		assert False, "Excess opened bracket"
	except ValueError:
		pass