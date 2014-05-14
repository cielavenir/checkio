import re
checkio=lambda line: re.sub(r'-+','-',line)

if __name__ == '__main__':
	assert checkio('I---like--python') == "I-like-python", 'Example'