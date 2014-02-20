import re

def checkio(text):
	text=re.sub(r'[,\!\.\?]',' ',text.lower())
	r=0
	for e in text.split():
		if re.search(r'^([aeiouy][bcdfghjklmnpqrstvwxz])+$',e): r+=1
		if re.search(r'^([bcdfghjklmnpqrstvwxz][aeiouy])+$',e): r+=1
		if re.search(r'^([aeiouy][bcdfghjklmnpqrstvwxz])+[aeiouy]$',e): r+=1
		if re.search(r'^([bcdfghjklmnpqrstvwxz][aeiouy])+[bcdfghjklmnpqrstvwxz]$',e): r+=1
	return r

#These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
	assert checkio("My name is ...") == 3, "All words are striped"
	assert checkio("Hello world") == 0, "No one"
	assert checkio("A quantity of striped words.") == 1, "Only of"
	assert checkio("Dog,cat,mouse,bird.Human.") == 3, "Dog, cat and human"