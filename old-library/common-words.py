def checkio(first, second):
	a=first.split(',')
	b=second.split(',')
	r=[]
	for e in a:
		if any(e==f for f in b): r.append(e)
	return ','.join(sorted(r))

if __name__ == '__main__':
	assert checkio("hello,world", "hello,earth") == "hello", "Hello"
	assert checkio("one,two,three", "four,five,six") == "", "Too different"
	assert checkio("one,two,three", "four,five,one,two,six,three") == "one,three,two", "1 2 3"