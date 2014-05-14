from collections import defaultdict
import random
def checkio(__d, _n1, _n2):
	_t=100000
	_s=0
	_d=[(e.count('A'),e.count('D')) for e in __d]
	d=defaultdict(int)
	for e in _d: #1P
		for f in _d: #2P
			d[(max(0,f[0]-e[1]),max(0,e[0]-f[1]))]+=1
	del d[(0,0)]
	l=[]
	for k,v in d.items():
		for i in range(v): l.append(k)
	print(l)
	for i in range(_t):
		n1=_n1
		n2=_n2
		while n1>0 and n2>0:
			e=l[random.randint(0,len(l)-1)]
			n1-=e[0]
			n2-=e[1]
		if n1>0: _s+=1
	print(_s*1.0/_t)
	return _s*1.0/_t

if __name__ == '__main__':
	def almost_equal(checked, correct, significant_digits=4):
		precision = 0.1 ** significant_digits
		return correct - precision < checked < correct + precision
	assert(almost_equal(checkio(['A', 'D'], 3, 3), 0.0000)) # It's not immediately obvious, but each player will always lose the same number of units
	assert(almost_equal(checkio(['A', 'D'], 4, 3), 1.0000))
	assert(almost_equal(checkio(['AA', 'A', 'D', 'DD'], 3, 4), 0.0186))
	#assert(almost_equal(checkio(['AA', 'A', 'D', 'DD'], 4, 4), 0.4079))
	#assert(almost_equal(checkio(['AA', 'A', 'D', 'DD'], 5, 4), 0.9073))