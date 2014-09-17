CIPHER='ADFGVX'

def each_slice(a,n):
	s=0
	while s<len(a):
		yield a[s:s+n]
		s+=n

def genmat(key):
	return list(each_slice(key,6))

def genkey(s):
	s0=''
	i=0
	for e in s:
		if e not in s0: s0+=e
	a=sorted(s0)
	r=[a.index(e) for e in s0]
	return r

def search(c,mat):
	for y in range(len(mat)):
		for x in range(len(mat[y])):
			if mat[y][x]==c: return (x,y)
	return None

def encode(_str,key1,key2):
	str=''.join(e.lower() for e in _str if e.isalnum())
	mat=genmat(key1)
	deckey=genkey(key2)
	enckey=[0]*len(deckey)
	for i,e in enumerate(deckey): enckey[e]=i
	r=''
	for e in str:
		x,y=search(e,mat)
		r+=CIPHER[y]+CIPHER[x]
	a=['']*len(enckey)
	for i in range(len(r)):
		a[i%len(enckey)]+=r[i]
	return ''.join(a[enckey[i]] for i in range(len(enckey)))

def decode(_str,key1,key2):
	mat=genmat(key1)
	deckey=genkey(key2)
	col=[[] for i in range(len(deckey))]
	for i in range(len(_str)): col[deckey[i%len(deckey)]]+=[i]
	enc=[]
	for e in col:
		for f in e: enc.append(f)
	ret=''
	for e in each_slice([e[1] for e in sorted(zip(enc,_str))],2):
		ret+=mat[CIPHER.index(e[0])][CIPHER.index(e[1])]
	return ret

if __name__=='__main__':
	assert encode('I am going', 'dhxmu4p3j6aoibzv9w1n70qkfslyc8tr5e2g','weasel') == 'DXGAXAAXXVDDFGFX'
	assert decode('DXGAXAAXXVDDFGFX', 'dhxmu4p3j6aoibzv9w1n70qkfslyc8tr5e2g','weasel') == 'iamgoing'
	assert encode('attack at 12:00 am','na1c3h8tb2ome5wrpd4f6g7i9j0kjqsuvxyz','privacy') == 'DGDDDAGDDGAFADDFDADVDVFAADVX'
	assert decode('DGDDDAGDDGAFADDFDADVDVFAADVX','na1c3h8tb2ome5wrpd4f6g7i9j0kjqsuvxyz','privacy') == 'attackat1200am'
	assert encode('ditiszeergeheim','na1c3h8tb2ome5wrpd4f6g7i9j0kjqsuvxyz','piloten') == 'DFGGXXAAXGAFXGAFXXXGFFXFADDXGA'
	assert decode('DFGGXXAAXGAFXGAFXXXGFFXFADDXGA','na1c3h8tb2ome5wrpd4f6g7i9j0kjqsuvxyz','piloten') == 'ditiszeergeheim'