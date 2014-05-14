def checkio(words_set):
	words=list(words_set)
	for i in range(len(words)):
		for j in range(len(words)):
			if i!=j and words[i].endswith(words[j]): return True
	return False

if __name__ == '__main__':
	assert checkio({"hello", "lo", "he"}) == True, "helLO"
	assert checkio({"hello", "la", "hellow", "cow"}) == False, "hellow la cow"
	assert checkio({"walk", "duckwalk"}) == True, "duck to walk"
	assert checkio({"one"}) == False, "Only One"