from functools import reduce
verify_anagrams=lambda *args:reduce(lambda x,y:x==y,(sorted(''.join(e.split()).lower()) for e in args))

if __name__ == '__main__':
	assert isinstance(verify_anagrams("a", 'z'), bool), "Boolean!"
	assert verify_anagrams("Programming", "Gram Ring Mop") == True, "Gram of code"
	assert verify_anagrams("Hello", "Ole Ho") == False, "Hello! Ole Ho!"
	assert verify_anagrams("Kyoto", "Tokyo") == True, "The global warming crisis of 3002"