import itertools
def checkio(data):
	result=sorted(list(set(''.join(data))))
	while True:
		for _e in data:
			for e,f in itertools.combinations(_e,2):
				idx1=result.index(e)
				idx2=result.index(f)
				if idx1>idx2:
					#result=result[0:idx2]+[result[idx1]]+result[idx2:idx1]+result[idx1+1:]
					result[idx1],result[idx2]=result[idx2],result[idx1]
					break
			else: continue
			break
		else: break
	return ''.join(result)

if __name__ == '__main__':
	assert checkio(["acb", "bd", "zwa"]) == "zwacbd", \
		"Just concatenate it"
	assert checkio(["klm", "kadl", "lsm"]) == "kadlsm", \
		"Paste in"
	assert checkio(["a", "b", "c"]) == "abc", \
		"Cant determine the order - use english alphabet"
	assert checkio(["aazzss"]) == "azs", \
		"Each symbol only once"
	assert checkio(["dfg", "frt", "tyg"]) == "dfrtyg", \
		"Concatenate and paste in"