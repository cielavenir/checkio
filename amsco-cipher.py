def decode_amsco(data,_col):
	col=[]
	while _col:
		col=[_col%10]+col
		_col//=10
	mat=[[] for i in range(len(col))]
	r=c=0
	#split data
	ncol=len(col)
	nrow=len(data)//(ncol*3)*2
	i=0
	while i<len(data):
		l=1 if r%2==c%2 else 2
		for _l in range(l):
			if i<len(data): mat[c].append(i)
			i+=1
		c+=1
		if c==ncol:
			c=0
			r+=1
	encode=[]
	for e in sorted(zip(col,mat)):
		for f in e[1]: encode.append(f)
	return ''.join(e[1] for e in sorted(zip(encode,data)))

if __name__=='__main__':
	assert decode_amsco("oruoreemdstmioitlpslam", 4123) == "loremipsumdolorsitamet", "Lorem Ipsum"
	assert decode_amsco('kicheco', 23415) == "checkio", "Checkio"
	assert decode_amsco('hrewhoorrowyilmmmoaouletow', 123) == "howareyouwillhometommorrow", "How are you"