from collections import Counter
def checkio(text,all_letters=False):
	t=[]
	for e in text.lower():
		if e.islower(): t.append(e)
	c=Counter(t)
	r=[e[0] for e in sorted(c.most_common(),key=lambda e:(-e[1],e[0]))]
	return ''.join(r) if all_letters else r[0]

if __name__ == '__main__':
	assert checkio("Hello World!") == "l", "Hello test"
	assert checkio("How do you do?") == "o", "O is most wanted"
	assert checkio("One") == "e", "All letter only once."
	assert checkio("Oops!") == "o", "Don't forget about lower case."
	assert checkio("AAaooo!!!!") == "a", "Only letters."