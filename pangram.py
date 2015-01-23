import string;check_pangram=lambda t:string.ascii_uppercase in str().join(sorted(list(set(t.upper()))))

#creative title=one liner without quotes

if __name__ == '__main__':
	assert check_pangram("The quick brown fox jumps over the lazy dog."), "brown fox"
	assert not check_pangram("ABCDEF"), "ABC"
	assert check_pangram("Bored? Craving a pub quiz fix? Why, just come to the Royal Oak!"), "Bored?"