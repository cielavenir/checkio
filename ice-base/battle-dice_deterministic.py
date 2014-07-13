from collections import defaultdict
#from fractions import Fraction
def make_dict(d, _n1, _n2):
	#probability of 1 die
	die=defaultdict(int)
	for e in d: die[(e.count('A'),e.count('D'))]+=1.0/len(d)
	#probability of n dice
	dice=[{},die]
	for n in range(2,max(_n1,_n2)+1):
		p=defaultdict(int)
		for k1,v1 in dice[n-1].items():
			for k2,v2 in die.items():
				p[(k1[0]+k2[0],k1[1]+k2[1])]+=v1*v2
		dice.append(p)
	#make dict
	dict = {}
	for n1 in range(_n1+1):
		for n2 in range(_n2+1):
			p = defaultdict(int)
			for k1,v1 in dice[n1].items():
				for k2,v2 in dice[n2].items():
					m1 = max(n1 - max(k2[0]-k1[1],0), 0)
					m2 = max(n2 - max(k1[0]-k2[1],0), 0)
					p[(m1,m2)]+=v1*v2
			dict[(n1,n2)]=p
	return dict

def battle_probability(d, n1, n2):
	dict=make_dict(d, n1, n2)
	ret=0
	p=defaultdict(int,{(n1,n2):1})
	for i in range(99):
		pnxt=defaultdict(int)
		for _k,_v in p.items():
			if _k[0]!=0 and _k[1]!=0:
				for k,v in dict[_k].items():
					if k[0]!=0 and k[1]==0: ret+=_v*v
					pnxt[k]+=_v*v
		p=pnxt
	return ret

if __name__ == '__main__':
	def almost_equal(checked, correct, significant_digits=4):
		precision = 0.1 ** significant_digits
		return correct - precision < checked < correct + precision
	assert(almost_equal(battle_probability(['A', 'D'], 3, 3), 0.0000)) # It's not immediately obvious, but each player will always lose the same number of units
	assert(almost_equal(battle_probability(['A', 'D'], 4, 3), 1.0000))
	assert(almost_equal(battle_probability(['AA', 'A', 'D', 'DD'], 3, 4), 0.0186))
	assert(almost_equal(battle_probability(['AA', 'A', 'D', 'DD'], 4, 4), 0.4079))
	assert(almost_equal(battle_probability(['AA', 'A', 'D', 'DD'], 5, 4), 0.9073))