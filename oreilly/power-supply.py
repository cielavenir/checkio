from collections import defaultdict
from scipy.sparse import *

def power_supply(a,p):
	i=-1
	m={}
	q={}
	b=[]
	c=[]
	for e in a:
		if e[0] not in m:i+=1;m[e[0]]=i;q[i]=e[0]
		if e[1] not in m:i+=1;m[e[1]]=i;q[i]=e[1]
		b.append((m[e[0]],m[e[1]]))
		c.append(1)
	r=[1]*len(m)
	mat=csr_matrix((c,zip(*b)),[len(m)]*2)
	for k,v in p.items():
		for i,e in enumerate(csgraph.dijkstra(mat,0,m[k])):
			if e<=v:r[i]=0
	return [q[i] for i,e in enumerate(r) if e]

if __name__ == '__main__':
	assert power_supply([['p1', 'c1'], ['c1', 'c2']], {'p1': 1}) == ['c2'], 'one blackout'
	assert power_supply([['c0', 'c1'], ['c1', 'p1'], ['c1', 'c3'], ['p1', 'c4']], {'p1': 1}) == ['c0', 'c3'], 'two blackout'
	assert power_supply([['p1', 'c1'], ['c1', 'c2'], ['c2', 'c3']], {'p1': 3}) == [], 'no blackout'
	assert power_supply([['c0', 'p1'], ['p1', 'c2']], {'p1': 0}) == ['c0', 'c2'], 'weak power-plant'
	assert power_supply([['p0', 'c1'], ['p0', 'c2'], ['c2', 'c3'], ['c3', 'p4'], ['p4', 'c5']], {'p0': 1, 'p4': 1}) == [], 'cooperation'
	assert power_supply([['c0', 'p1'], ['p1', 'c2'], ['c2', 'c3'], ['c2', 'c4'], ['c4', 'c5'],
						 ['c5', 'c6'], ['c5', 'p7']],
						{'p1': 1, 'p7': 1}) == ['c3', 'c4', 'c6'], 'complex cities 1'
	assert power_supply([['p0', 'c1'], ['p0', 'c2'], ['p0', 'c3'],
						 ['p0', 'c4'], ['c4', 'c9'], ['c4', 'c10'],
					   ['c10', 'c11'], ['c11', 'p12'], ['c2', 'c5'],
					   ['c2', 'c6'], ['c5', 'c7'], ['c5', 'p8']],
					  {'p0': 1, 'p12': 4, 'p8': 1}) == ['c6', 'c7'], 'complex cities 2'
	print("Looks like you know everything. It is time for 'Check'!")
