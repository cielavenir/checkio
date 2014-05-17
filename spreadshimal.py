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
		j+=1
		r//=26
	if flg>0:
		j-=1
		xxx=xxx[:j]
	return ''.join(reversed(xxx))

if __name__ == '__main__':
	assert checkio(1) == 'A'
	assert checkio(2) == 'B'
	assert checkio(26) == 'Z'
	assert checkio(27) == 'AA'
	print('Done')