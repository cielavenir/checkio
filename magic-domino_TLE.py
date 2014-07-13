#import itertools
def rec(m,dominos,x,y,sum1,sum2,size,number):
	if y==size:
		s=0
		for _i in range(size): s+=m[_i][_i]
		if s!=number: return None
		s=0
		for _i in range(size): s+=m[size-1-_i][_i]
		if s!=number: return None
		return m
	if x==size-1:
		m[y][x]=number-sum1
		m[y+1][x]=number-sum2
		for i in range(len(dominos)):
			if (dominos[i][0]==m[y][x] and dominos[i][1]==m[y+1][x]) or (dominos[i][0]==m[y+1][x] and dominos[i][1]==m[y][x]):
				return rec(m,dominos[:i]+dominos[i+1:],0,y+2,0,0,size,number)
		return None
	if sum1<number-((size-x)*6) or number<sum1 or sum2<number-((size-x)*6) or number<sum2: return None
	for i in range(len(dominos)):
		if y+2==size:
			s=0
			for _i in range(size-2): s+=m[_i][x]
			if s+dominos[i][0]+dominos[i][1]!=number: continue
		m[y][x]=dominos[i][0]
		m[y+1][x]=dominos[i][1]
		_m=rec(m,dominos[:i]+dominos[i+1:],x+1,y,sum1+m[y][x],sum2+m[y+1][x],size,number)
		if _m: return _m
		m[y][x]=dominos[i][1]
		m[y+1][x]=dominos[i][0]
		_m=rec(m,dominos[:i]+dominos[i+1:],x+1,y,sum1+m[y][x],sum2+m[y+1][x],size,number)
		if _m: return _m
	return None
def magic_domino(size,number):
	#dominos=[e for e in itertools.combinations_with_replacement(range(7),2)]
	dominos=[]
	for i in range(7):
		for j in range(i,7):
			dominos.append((i,j))
	ret=rec(
		[[0]*size for i in range(size)],
		dominos,
		0,0,0,0,size,number
	)
	if ret:
		for e in ret: print(e)
	return ret

def check_data(size, number, user_result):
	if not user_result: return 'Invalid'
	for i in range(size):
		for j in range(size):
			if user_result[i][j]<0 or 6<user_result[j][i]: return 'Out of range'
	for x in range(size):
		s=0
		for _i in range(size): s+=user_result[_i][x]
		if s!=number: return 'Vertical'
	for y in range(size):
		s=0
		for _i in range(size): s+=user_result[y][_i]
		if s!=number: return 'Horizontal'
	s=0
	for _i in range(size): s+=user_result[_i][_i]
	if s!=number: return 'Diagonal'
	s=0
	for _i in range(size): s+=user_result[size-1-_i][_i]
	if s!=number: return 'Diagonal'

def test(size,number):
	print([size,number])
	ret=check_data(size,number,magic_domino(size,number))
	if ret: print(ret)

###RPython stuff
def entry_point(argv):
	test(int(argv[1]), int(argv[2]))
	return 0

def target(*args):
	return entry_point, None

if __name__ == '__main__':
	from sys import argv
	test(int(argv[1]), int(argv[2]))
