#!/usr/bin/python
B=999999937
P=1000000007

from collections import defaultdict
import bisect

class KeyRange(object):
	def __init__(self, lo, hi, key):
		self.lo = lo
		self.hi = hi
		self.key = key
	def __len__(self):
		return self.hi-self.lo
	def __getitem__(self, k):
		return self.key(k)

def gen_hash(s,hash):
	c=0
	for i in range(len(s)):
		c=(c*B+s[i])%P
		hash[i]=c

class Checker:
	def __init__(self,v):
		self.v=v
		self.i=None
	def chk(self,k):
		r=defaultdict(list)
		Bk=pow(B,k,P)
		for i in range(k-1,len(self.v)):
			hsh=(self.v[i]-(self.v[i-k] if i>=k else 0)*Bk%P)%P
			r[hsh].append(i)
		for v in r.values():
			if v[-1]-v[0]>=k:
				self.i=v[0]
				return 0
		return 1

def double_substring(s):
	if not s:return 0
	s=[ord(e) for e in s]
	ls=len(s)
	v=[0]*ls
	gen_hash(s,v)
	check=Checker(v)
	n=bisect.bisect_left(KeyRange(0,ls,check.chk),1)-1
	return n
