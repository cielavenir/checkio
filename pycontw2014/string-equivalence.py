#coding:utf-8
import unicodedata
checkio=lambda a,b:unicodedata.normalize('NFC',a)==unicodedata.normalize('NFC',b)

if __name__ == '__main__':
	assert checkio(u"\u212B", u"\u00C5") == True
	assert checkio(u"\u212B", u"A") == False
	print('Done')