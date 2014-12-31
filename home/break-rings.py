from functools import reduce
from collections import defaultdict
def break_rings(_rings):
	rings=list(_rings)
	ring=sorted(reduce(set.union, rings))
	r=0
	while rings:
		d=defaultdict(int)
		for e in rings:
			for f in e: d[f]+=1
		try:
			k=next(k for k,v in d.items() if v==1)
			m=next(list(set(e)-set([k]))[0] for e in rings if k in e)
		except StopIteration: # no tip ring
			m=max(d.items(),key=lambda e:e[1])[0]
		for i in reversed(range(0,len(rings))):
			if m in rings[i]: del rings[i]
		r+=1
	return r

if __name__ == '__main__':
	assert break_rings(({1, 2}, {2, 3}, {3, 4}, {4, 5}, {5, 6}, {4, 6})) == 3, "example"
	assert break_rings(({1, 2}, {1, 3}, {1, 4}, {2, 3}, {2, 4}, {3, 4})) == 3, "All to all"
	assert break_rings(({5, 6}, {4, 5}, {3, 4}, {3, 5}, {3, 6})) == 2, "Chain"
	assert break_rings(({8, 9}, {1, 9}, {1, 2}, {2, 3}, {3, 4}, {4, 5}, {5, 6}, {6, 7}, {8, 7})) == 5, "Long chain"