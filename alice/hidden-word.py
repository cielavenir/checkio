import re

def checkio(text_, word):
	text=re.sub(' ','',text_.lower()).split("\n")
	l=len(word)
	Y=len(text)
	X=max(len(e) for e in text)
	for y in range(Y):
		for x in range(X):
			try:
				if all(text[y][x+k]==word[k] for k in range(len(word))): return [y+1,x+1,y+1,x+len(word)]
			except IndexError: pass
			try:
				if all(text[y+k][x]==word[k] for k in range(len(word))): return [y+1,x+1,y+len(word),x+1]
			except IndexError: pass
	return None

#These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
	assert checkio("""DREAMING of apples on a wall,
And dreaming often, dear,
I dreamed that, if I counted all,
-How many would appear?""", "ten") == [2, 14, 2, 16]
	assert checkio("""He took his vorpal sword in hand:
Long time the manxome foe he sought--
So rested he by the Tumtum tree,
And stood awhile in thought.
And as in uffish thought he stood,
The Jabberwock, with eyes of flame,
Came whiffling through the tulgey wood,
And burbled as it came!""", "noir") == [4, 16, 7, 16]