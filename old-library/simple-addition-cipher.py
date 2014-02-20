s=' abcdefghijklmnopqrstuvwxyz'
h={}
for index,item in enumerate(s): h[item]=index

def checkio(data):
	old_encrypted, old_decrypted, new_encrypted = data
	key=[]
	for i in range(len(old_encrypted)):
		key.append((h[old_encrypted[i]]-h[old_decrypted[i]]+27)%27)
	l=1
	try:
		while True:
			i=0
			while i<l:
				if key[i]!=key[l+i]: break
				i+=1
			if i>=l: break
			l+=1
	except IndexError:
		l=len(old_encrypted)
	r=''
	for i in range(len(new_encrypted)):
		r+=s[(h[new_encrypted[i]]-key[i%l]+27)%27]
	return r

#These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
	assert checkio(
		[
			'lmljemxbwrhhfyd stlmhrxyvwhk',
			'this text contain the secret',
			'tsgryaaxckjqledcxhshreyuasckmysxhuwyl'
		]) == 'and this text also contain the secret', 'Secret'
	assert checkio(
		[
			'pjxxchnedonncdhhrqdgilq',
			'hello its first message',
			'pjxxchnedo jo bleyqg fsq'
		]) == 'hello its second message', "Hello"
	assert checkio(
		[
			'dxb dxb dxb dxb',
			'bla bla bla bla',
			'tqblbefxv'
		]) == 'real text', "Bla Bla Bla"
	assert checkio(
		[
			'dtqyefpxqtlh',
			'long message',
			'kmriy'
		]) == 'short', "Short"
	assert checkio(
		[
			'vjwclkjfijm',
			'keyofsecret',
			'lpcmuyxhuwyd'
		]) == 'akeyofsecret', "Almost"