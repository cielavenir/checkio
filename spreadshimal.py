def checkio(r):
	flg=0
	xxx=''
	j=0
	while r>0:
		xxx+=chr(r%26+65-1-flg)
		flg=0
		if xxx[j]=='@':
			xxx=xxx[:j]+'Z'
			flg=1
		if xxx[j]=='?':
			xxx=xxx[:j]+'Y'
			flg=1
		j+=1
		r//=26
	if flg>0:
		j-=1
		xxx=xxx[:j]
	return xxx[::-1]

def checkio2(s):
	r=0
	for c in s:
		c=c.upper()
		r*=26
		r+=ord(c)-65+1
	return r

if __name__ == '__main__':
	assert checkio(1) == 'A'
	assert checkio(2) == 'B'
	assert checkio(26) == 'Z'
	assert checkio(27) == 'AA'
	assert checkio(675) == 'YY'
	print(checkio(456976))
	assert checkio(676) == 'YZ'
	print('Done')
