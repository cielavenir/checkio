import re
def first_word(txt):
	txt=re.sub(r'[^\w\s\']','',txt)
	return txt.split()[0]
