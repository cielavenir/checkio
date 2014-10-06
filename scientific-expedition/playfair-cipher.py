def each_slice(iterable,n):
	y=[]
	for e in iterable:
		y.append(e)
		if len(y)==n:
			yield y
			y=[]
	if y: yield y

def each_cons(iterable,n):
	siz=0
	y=[]
	for e in iterable:
		y.append(e)
		if len(y)>n: y.pop(0)
		if len(y)==n: yield y[:]

#def flatten(iterable):
#	for e in iterable:
#		for f in e: yield f
import itertools
flatten=lambda iterable:itertools.chain.from_iterable(iterable)
#flatten=lambda iterable:itertools.chain(*iterable)

def genmat(key):
	r=[]
	t=key+'abcdefghijklmnopqrstuvwxyz0123456789'
	for e in t:
		if e not in r: r.append(e)
	return list(each_slice(r,6))

def search(c,mat):
	for y in range(len(mat)):
		for x in range(len(mat[y])):
			if mat[y][x]==c: return (x,y)
	return None

def encode_stage2(a,mat,add): # add==1 => encode, add==-1 => decode
	r=[]
	for e in a:
		x0,y0=search(e[0],mat)
		x1,y1=search(e[1],mat)
		if x0==x1:
			r+=[mat[(y0+add)%len(mat)][x0]+mat[(y1+add)%len(mat)][x1]]
		elif y0==y1:
			r+=[mat[y0][(x0+add)%len(mat[y0])]+mat[y1][(x1+add)%len(mat[y1])]]
		else:
			r+=[mat[y0][x1]+mat[y1][x0]]
	return r

def encode_stage1(_str):
	str=''.join(e.lower() for e in _str if e.isalnum())
	r=[]
	i=0
	while i<len(str):
		if len(str[i:])==1:
			if str[i]=='z': r+=['zx']
			else: r+=[str[i]+'z']
			i+=1
		else:
			if str[i]==str[i+1]:
				if str[i]=='x': r+=['xz']
				else: r+=[str[i]+'x']
				i+=1
			else:
				r+=[str[i:i+2]]
				i+=2
	return r

def decode_stage1(a):
	'''
	#actually encoding is already not deterministic;
	#'ssa' and 'sxsa' are both encoded into ['sx','sa'].
	print(a)
	r=''
	for i,e in enumerate(a):
		if i<len(a)-1:
			if e[1]=='x' or e=='xz': r+=e[0]
			else: r+=e
		else:
			if e[1]=='z' or e=='zx': r+=e[0]
			else: r+=e
	print(r)
	'''
	return ''.join(a)

def encode(str,key):
	return ''.join(encode_stage2(encode_stage1(str),genmat(key),1))

def decode(str,key):
	return decode_stage1(encode_stage2(each_slice(str,2),genmat(key),-1))

if __name__=='__main__':
	assert encode("Fizz Buzz is x89 XX.", "checkio101") == 'do2y7mt22kry94y2y2', "Encode fizz buzz"
	assert decode("do2y7mt22kry94y2y2", "checkio101") == 'fizxzbuzzisx89xzxz', "Decode fizz buzz"
	assert encode("How are you?", "hello") == 'ea2imb1ht0', "Encode How are you"
	assert decode("ea2imb1ht0", "hello") == 'howareyouz', "Decode How are you"
	assert encode("My name is Alex!!!", "alexander") == 'i1dlkxjqlexn', "Encode Alex"
	assert decode("i1dlkxjqlexn", "alexander") == 'mynameisalex', "Decode Alex"
	assert encode("Who are you?", "human") == 'rnvftc1jd5', "Encode WHo"
	assert decode("rnvftc1jd5", "human") == 'whoareyouz', "Decode Who"
	assert encode("ATTACK AT DAWN", "general") == 'ewwektewhnua', "Encode attack"
	assert decode("ewwektewhnua", "general") == 'attackatdawn', "Decode attack"