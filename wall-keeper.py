#coding:utf-8
#speedy O(HW)
#cf: http://yukicoder.me/submissions/156186

import functools
#if sys.version_info[0]<3:
if 'maketrans' not in str.__dict__:
	range=xrange

def popcnt(n):
	r=0
	while n>0:
		r+=n%2
		n//=2
	return r

def prepare(x,y):
	a=[[0,0] for _ in range(x*y)]

	#create problem
	for i in range(x):
		for j in range(y):
			a[i+j*x][0]=1<<(i+j*x)
			a[i+j*x][1]= 0 +\
				(1<<(i+j*x)) |\
				(1<<(i-1+j*x) if i>0   else 0) |\
				(1<<(i+1+j*x) if i<x-1 else 0) |\
				(1<<(i+(j-1)*x) if j>0   else 0) |\
				(1<<(i+(j+1)*x) if j<y-1 else 0) |\
				0

	#solve
	badbits=0
	for i in range(x*y):
		if (a[i][1]&(1<<i))==0:
			for j in range(i+1,x*y):
				if (a[j][1]&(1<<i))!=0:
					a[i],a[j]=a[j],a[i]
					break
			else:
				badbits|=1<<i
				continue
		for j in range(x*y):
			if i==j: continue
			if (a[j][1]&(1<<i))!=0:
				a[j][0]^=a[i][0]
				a[j][1]^=a[i][1]

	k=x*y-popcnt(badbits)

	#t: the set of quiet pattern
	tmsk=0
	t=[]
	a_ok=[]
	for i in range(x*y):
		if ((badbits>>i)&1):
			t.append(a[i][0])
		else:
			a_ok.append((i,a[i][0]))
			tmsk|=1<<i

	tlst=[0]*(1<<(x*y-k))
	for l in range(1<<(x*y-k)):
		r=0
		for j in range(x*y-k):
			if (l&(1<<j)):
				r^=t[j]
		tlst[l]=r
	return (a_ok,tlst,t)

H=5
W=5
def solve(a_ok,tlst,t,a):
	input_=0
	for i in a: input_|=1<<(i-1)
	if any(popcnt(e&input_)%2 for e in t):
		return None

	r=0
	r0=1<<29
	c0=0
	for j in a_ok:
		if (input_&(1<<j[0])):
			c0^=j[1]
	#try every quiet-pattern
	for l in range(len(tlst)):
		r1=c0
		r1^=tlst[l]
		if r0>popcnt(r1):
			r0=popcnt(r1)
			r=r1
		r0=min(r0,popcnt(r1))
	q='%*s'%(H*W,bin(r)[2:])
	return [i+1 for i,e in enumerate(reversed(q)) if e=='1']

#precalc answer grid
wall_keeper=functools.partial(solve,*prepare(W,H))
