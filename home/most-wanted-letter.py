from collections import Counter
def checkio(text):
	t=[]
	for e in text.lower():
		if e.islower(): t.append(e)
	c=Counter(t)
	r=[]
	max=c.most_common()[0][1]
	for e in c.most_common():
		if e[1]<max: break
		r.append(e[0])
	return sorted(r)[0]

if __name__ == '__main__':
	assert checkio("Hello World!") == "l", "Hello test"
	assert checkio("How do you do?") == "o", "O is most wanted"
	assert checkio("One") == "e", "All letter only once."
	assert checkio("Oops!") == "o", "Don't forget about lower case."
	assert checkio("AAaooo!!!!") == "a", "Only letters."