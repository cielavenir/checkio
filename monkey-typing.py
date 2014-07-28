count_words=lambda str,words: sum(str.lower().find(e)>=0 for e in words)

if __name__=='__main__':
	assert count_words("How aresjfhdskfhskd you?", {"how", "are", "you", "hello"}) == 3
	assert count_words("Bananas, give me bananas!!!", {"banana", "bananas"}) == 2
	assert count_words("Lorem ipsum dolor sit amet, consectetuer adipiscing elit.",
		{"sum", "hamlet", "infinity", "anything"}) == 1