import itertools

def check(data,result):
	for _e in data:
		for e,f in itertools.combinations(_e,2):
			idx1=result.index(e)
			idx2=result.index(f)
			if idx1>idx2:
				return (idx1,idx2)
	return None

def checkio(data):
	result=sorted(list(set(''.join(data))))
	a=check(data,result)
	while a:
		#result=result[0:a[1]]+[result[a[0]]]+result[a[1]:a[0]]+result[a[0]+1:]
		result[a[0]],result[a[1]]=result[a[1]],result[a[0]]
		a=check(data,result)
	while True:
		for i in range(len(result)-1):
			for j in range(i+1,len(result)):
				if result[i]>result[j]:
					result2=result[0:i]+[result[j]]+result[i:j]+result[j+1:]
					if not check(data,result2):
						result=result2
						break
			else: continue
			break
		else: break
	return ''.join(result)

#These "asserts" using only for self-checking and not necessary for auto-testing
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
	assert checkio(["abg","hef","bf"]) == "abghef"