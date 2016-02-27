def longest_palindromic(text):
	for i in range(len(text),0,-1):
		for j in range(len(text)-i+1):
			s=text[j:j+i]
			if s==s[::-1]: return s

if __name__ == '__main__':
	assert longest_palindromic("artrartrt") == "rtrartr", "The Longest"
	assert longest_palindromic("abacada") == "aba", "The First"
	assert longest_palindromic("aaaa") == "aaaa", "The A"