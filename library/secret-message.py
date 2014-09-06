find_message=lambda text: ''.join(e for e in text if e.isupper())

if __name__ == '__main__':
	assert find_message("How are you? Eh, ok. Low or Lower? Ohhh.") == "HELLO", "hello"
	assert find_message("hello world!") == "", "Nothing"
	assert find_message("HELLO WORLD!!!") == "HELLOWORLD", "Capitals"