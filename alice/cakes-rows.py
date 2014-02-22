from itertools import combinations
cross=lambda a,b: (a.conjugate()*b).imag
dot=lambda a,b: (a.conjugate()*b).real

def solve(points):
	h={}
	num=0
	for e in combinations(list(range(len(points))),3):
		if cross(points[e[1]]-points[e[0]],points[e[2]]-points[e[0]])==0:
			a=(e[0]<<16)|e[1]
			b=(e[0]<<16)|e[2]
			c=(e[1]<<16)|e[2]
			entry=None
			if a in h: entry=h[a]
			if b in h: entry=h[b]
			if c in h: entry=h[c]
			if entry==None:
				num+=1
				h[a]=h[b]=h[c]=num
			else:
				h[a]=h[b]=h[c]=entry
	return num

checkio=lambda data: solve([complex(*e) for e in data])

#These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
	assert checkio([[3, 3], [5, 5], [8, 8], [2, 8], [8, 2]]) == 2
	assert checkio(
		[[2, 2], [2, 5], [2, 8], [5, 2], [7, 2], [8, 2],
		 [9, 2], [4, 5], [4, 8], [7, 5], [5, 8], [9, 8]]) == 6