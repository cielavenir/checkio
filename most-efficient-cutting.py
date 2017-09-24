import itertools
L=6000

def solve(data):
	r=cur=0
	for e in data:
		if cur+e>L:
			r+=L-cur
			cur=e
		else:
			cur+=e
	if cur:
		r+=L-cur
	return r

def most_efficient_cutting(data):
	return min(solve(e) for e in itertools.permutations(data))
