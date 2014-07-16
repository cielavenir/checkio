#except itertools.combinations(), this source is RPython compliant.

import itertools
import time#,os
try:
	import rpython.rlib.rrandom
	RPYTHON=True
except ImportError:
	RPYTHON=False
	import random

#Searched using several random seeds, really.
dict6={
	13: [
		[1, 0, 2, 0, 4, 6],
		[3, 0, 2, 5, 3, 0],
		[3, 4, 1, 1, 1, 3],
		[3, 4, 1, 5, 0, 0],
		[2, 1, 6, 2, 2, 0],
		[1, 4, 1, 0, 3, 4]
	],
	14: [
		[3, 2, 3, 4, 2, 0],
		[6, 6, 2, 0, 0, 0],
		[1, 1, 0, 6, 0, 6],
		[2, 0, 3, 0, 5, 4],
		[1, 4, 4, 2, 2, 1],
		[1, 1, 2, 2, 5, 3]
	],
	15: [
		[0, 1, 4, 5, 2, 3],
		[5, 3, 6, 1, 0, 0],
		[2, 6, 0, 5, 2, 0],
		[4, 2, 4, 2, 3, 0],
		[2, 1, 1, 1, 4, 6],
		[2, 2, 0, 1, 4, 6]
	],
	16: [
		[1, 1, 0, 3, 6, 5],
		[6, 2, 2, 6, 0, 0],
		[1, 5, 6, 0, 0, 4],
		[0, 4, 6, 3, 0, 3],
		[4, 1, 1, 2, 4, 4],
		[4, 3, 1, 2, 6, 0]
	],
	17: [
		[3, 3, 0, 2, 6, 3],
		[5, 4, 4, 0, 1, 3],
		[0, 2, 3, 6, 4, 2],
		[0, 4, 0, 6, 4, 3],
		[3, 1, 5, 1, 1, 6],
		[6, 3, 5, 2, 1, 0]
	],
	18: [
		[0, 3, 4, 5, 6, 0],
		[3, 5, 5, 0, 5, 0],
		[3, 4, 1, 1, 3, 6],
		[4, 0, 4, 6, 2, 2],
		[4, 4, 2, 0, 2, 6],
		[4, 2, 2, 6, 0, 4]
	],
	19: [
		[6, 3, 5, 1, 0, 4],
		[6, 4, 6, 2, 1, 0],
		[2, 1, 2, 5, 6, 3],
		[3, 3, 4, 2, 4, 3],
		[1, 4, 2, 4, 2, 6],
		[1, 4, 0, 5, 6, 3]
	],
	20: [
		[1, 1, 1, 5, 6, 6],
		[2, 6, 4, 2, 2, 4],
		[3, 4, 6, 1, 1, 5],
		[4, 5, 6, 1, 3, 1],
		[5, 0, 3, 6, 4, 2],
		[5, 4, 0, 5, 4, 2]
	],
	21: [
		[3, 1, 4, 5, 4, 4],
		[5, 3, 6, 5, 0, 2],
		[0, 4, 5, 5, 5, 2],
		[1, 4, 0, 4, 6, 6],
		[6, 6, 1, 1, 3, 4],
		[6, 3, 5, 1, 3, 3]
	],
	22: [
		[3, 1, 5, 2, 5, 6],
		[5, 3, 5, 4, 4, 1],
		[1, 6, 4, 6, 2, 3],
		[2, 6, 1, 4, 6, 3],
		[6, 0, 4, 1, 5, 6],
		[5, 6, 3, 5, 0, 3]
	],
	23: [
		[1, 3, 4, 4, 6, 5],
		[6, 6, 6, 5, 0, 0],
		[2, 2, 3, 4, 6, 6],
		[2, 5, 5, 4, 5, 2],
		[6, 3, 2, 3, 4, 5],
		[6, 4, 3, 3, 2, 5]
	]
}

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
	if size==6: return dict6[number]
	#dominos=[e for e in itertools.combinations_with_replacement(range(7),2)]
	dominos=[]
	for i in range(7):
		for j in range(i,7):
			dominos.append((i,j))
	#Fisher-Yates
	seed=int(time.time()) #^(os.getpid()<<16)
	rnd=rpython.rlib.rrandom.Random(seed) if RPYTHON else random.Random(seed)
	i=len(dominos)-1
	while i>0:
		idx=int(rnd.random()*(i+1))
		dominos[i],dominos[idx]=dominos[idx],dominos[i]
		i-=1
	#cnt=0
	for dom in itertools.combinations(dominos,size*size//2):
		#cnt+=1
		#if cnt%10000==0: print(cnt)
		if sum(sum(e) for e in dom)==size*number:
			#print(cnt)
			#print('Found')
			#print(dom)
			ret=rec(
				[[0]*size for i in range(size)],
				dom,
				0,0,0,0,size,number
			)
			if ret:
				#for e in ret: print(e)
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
	#print([size,number])
	ret=check_data(size,number,magic_domino(size,number))
	if ret: print(ret)

###RPython stuff
def entry_point(argv):
	test(int(argv[1]), int(argv[2]))
	return 0

def target(*args):
	return entry_point

if __name__ == '__main__':
	#from sys import argv
	#test(int(argv[1]), int(argv[2]))