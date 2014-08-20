from functools import reduce # reduce version must be submitted using Py2

def golf(c):
 z=set()
 for n in range(1,len(c)+1):z=z.union(map(sum,__import__('itertools').combinations(c,n)))
 return min(set(range(1,99))-z)

golf=lambda c:min(set(range(1,99))-reduce(lambda x,y:x.union(y),[set(map(sum,__import__('itertools').combinations(c,n)))for n in range(len(c))]))

def golf(c):
 l=len(c);z=set()
 for n in range(1<<l):z.add(sum(c[i]for i in range(l)if n&1<<i))
 return min(set(range(1,99))-z)

if __name__ == '__main__':
	assert golf([10, 2, 2, 1]) == 6
	assert golf([1, 1, 1, 1]) == 5
	assert golf([1, 2, 3, 4, 5]) == 16