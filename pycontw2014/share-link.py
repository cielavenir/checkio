#coding:utf-8
checkio=lambda string:[e for e in string.split() if e.startswith('http://') or e.startswith('https://')]

if __name__ == '__main__':
	assert checkio(u"http://台灣.taipei/") == [u"http://台灣.taipei/"]
	print('Done')