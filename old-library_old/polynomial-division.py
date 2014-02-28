import re

def add(a,b):
	m=max(len(a),len(b))
	return [(0 if len(a)<=i else a[i])+(0 if len(b)<=i else b[i]) for i in range(m)]

def sub(a,b):
	return add(a,[-1*e for e in b])

def mul(a,b):
	r=[]
	for i in range(len(b)):
		r=add(r,[0]*i+[b[i]*e for e in a])
	return r

def process(s):
	try:
		while True:
			bidx=s.index('(')
			count=1
			eidx=bidx+1
			while count>0:
				if s[eidx]=='(': count+=1
				if s[eidx]==')': count-=1
				eidx+=1
			s=s[:bidx]+process(s[bidx+1:eidx-1])+s[eidx:]
	except ValueError:
		pass
	while True:
		m=re.match(r'(.*?)([0-9,-]+)([*])([0-9,-]+)(.*)',s)
		if not m: break
		s=m.group(1)+','.join(str(f) for f in mul([int(e) for e in m.group(2).split(',')],[int(e) for e in m.group(4).split(',')]))+m.group(5)
	while True:
		m=re.match(r'(.*?)([0-9,-]+)([+Z])([0-9,-]+)(.*)',s)
		if not m: break
		if m.group(3)=='+':
			s=m.group(1)+','.join(str(f) for f in add([int(e) for e in m.group(2).split(',')],[int(e) for e in m.group(4).split(',')]))+m.group(5)
		else:
			s=m.group(1)+','.join(str(f) for f in sub([int(e) for e in m.group(2).split(',')],[int(e) for e in m.group(4).split(',')]))+m.group(5)
	return s

def format(a):
	r=[]
	for i,e in enumerate(a):
		if e==0: continue
		if i==0:
			if e>0: r.append('+'+str(e))
			else: r.append(str(e))
		else:
			if e==1: s='+'
			elif e==-1: e='-'
			elif e>0: s='+'+str(e)+'*'
			else: s=str(e)+'*'
			r.append(s+'*'.join(['x']*i))
	ret=''.join(reversed(r))
	return ret[1:] if len(ret)>0 and ret[0]=='+' else ret

def checkio(a):
	b=[]
	for s in a:
		s=re.sub(r'-','Z',s)
		s=re.sub(r'x','0,1',s)
		b.append([int(_) for _ in process(s).split(',')])
	c=[]
	while len(b[1])<=len(b[0]): #bah
		d=b[0][-1]//b[1][-1] #bah
		c.append(d)
		b[0]=sub(b[0],[0]*(len(b[0])-len(b[1]))+[e*d for e in b[1]])
		assert b[0][-1]==0
		b[0].pop()
	return [format(e) for e in [list(reversed(c)),b[0]]]

#These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
	assert checkio(['x*x*x-12*x*x-42', 'x-3']) == ['x*x-9*x-27', '-123'], "1st"
	assert checkio(['x*x-1', 'x+1']) == ['x-1', ''], "2nd"
	assert checkio(['x*x*x+6*x*x+12*x+8', 'x+2']) == ['x*x+4*x+4', ''], "3rd"
	assert checkio(['x*x*x*x*x+5*x+1', 'x*x']) == ['x*x*x', '5*x+1'], "4th"