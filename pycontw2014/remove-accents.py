#coding:utf-8
import unicodedata
checkio=lambda s:''.join(e for e in unicodedata.normalize('NFD',s) if ord(e)<128 or ord(e)>999)

if __name__ == '__main__':
	assert checkio(u"préfèrent") == u"preferent"
	assert checkio(u"loài trăn lớn") == u"loai tran lon"
	print('Done')