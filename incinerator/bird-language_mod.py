translate=lambda s:s and s[0]+translate(s[1+(s[0]>' ')+(s[0]in'aeiouy'):])

if __name__ == '__main__':
	assert translate("hieeelalaooo") == "hello", "Hi!"
	assert translate("hoooowe yyyooouuu duoooiiine") == "how you doin", "Joey?"
	assert translate("aaa bo cy da eee fe") == "a b c d e f", "Alphabet"
	assert translate("sooooso aaaaaaaaa") == "sos aaa", "Mayday, mayday"