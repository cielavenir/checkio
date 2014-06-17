t=lambda s:s[0]+t(s[2+int('aeiouy'.find(s[0])>=0):])if s else''
translate=lambda s:' '.join(map(t,s.split()))

if __name__ == '__main__':
	assert translate("hieeelalaooo") == "hello", "Hi!"
	assert translate("hoooowe yyyooouuu duoooiiine") == "how you doin", "Joey?"
	assert translate("aaa bo cy da eee fe") == "a b c d e f", "Alphabet"
	assert translate("sooooso aaaaaaaaa") == "sos aaa", "Mayday, mayday"