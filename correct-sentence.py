def correct_sentence(txt):
	txt=txt[0].upper()+txt[1:].lower()
	if txt[-1]!='.': txt+='.'
	return txt
