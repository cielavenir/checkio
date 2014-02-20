def checkio(words):
	x=0
	for e in words.lower().split():
		if e.islower():
			x+=1
			if x==3: return True
		else:
			x=0
	return False

#These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
	assert checkio("Hello World hello") == True, "Hello"
	assert checkio("He is 123 man") == False, "123 man"
	assert checkio("1 2 3 4") == False, "Digits"
	assert checkio("bla bla bla bla") == True, "Bla Bla"
	assert checkio("Hi") == False, "Hi"