import math
ETHERNET = (0.1,1,10,40,100)

def routing(ring,dept,dest):
	idx1=ring.index(dept)
	idx2=ring.index(dest)
	return min([[idx1,idx2],[idx2,idx1]],key=lambda e:(e[1]-e[0])%len(ring))
	
def checkio(ring,*flows):
	ring=[ord(c)-65 for c in ring]
	cost=[0]*len(ring)
	for e in flows:
		route=routing(ring,*[ord(c)-65 for c in e[0]])
		i=route[0]
		while i!=route[1]:
			cost[i]+=e[1]
			i=(i+1)%len(ring)
	result=[0]*len(ETHERNET)
	for c in cost:
		if c==0: continue
		for i,e in enumerate(ETHERNET):
			if e>=c:
				result[i]+=1
				break
		else:
			result[-1]+=math.ceil(float(c)/ETHERNET[-1])
	return list(reversed(result))

if __name__ == '__main__':
	assert checkio("AEFCBG", ("AC", 5), ("EC", 10), ("AB", 60)) == [2, 2, 1, 0, 0]
	assert checkio("ABCDEFGH", ("AD", 4)) == [0, 0, 3, 0, 0]
	assert checkio("ABCDEFGH", ("AD", 4), ("EA", 41)) == [4, 0, 3, 0, 0]