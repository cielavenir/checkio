import re
checkio=lambda line: re.sub(r'-+','-',line)

#These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
	assert checkio('I---like--python') == "I-like-python", 'Example'