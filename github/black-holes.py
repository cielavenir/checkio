import math,itertools

def intersect(a,b):
	d=math.hypot(a[0]-b[0],a[1]-b[1])
	r1=a[2]
	r2=b[2]
	if min(r1,r2)+d<=max(r1,r2): return True # inside
	if r1+r2<d: return False # outside
	area=( # http://okwave.jp/qa/q3471274.html
		r1*r1*math.acos((d*d+r1*r1-r2*r2)/(2*d*r1)) +
		r2*r2*math.acos((d*d+r2*r2-r1*r1)/(2*d*r2)) -
		math.sqrt(4*d*d*r1*r1-(d*d+r1*r1-r2*r2)**2)/2
	)
	return area/(min(r1,r2)**2*math.pi)>=0.55

def dominate(a,b):
	s1=math.pi*a[2]*a[2]
	s2=math.pi*b[2]*b[2]
	val=(s1-s2)/s1 if s1>s2 else (s2-s1)/s2
	return val>=0.2

def merge(a,b):
	if a[2]<b[2]: a,b=b,a
	return (a[0],a[1],math.hypot(a[2],b[2]))

def checkio(a):
	while True:
		try:
			d,i,j=min(
				(math.hypot(a[i][0]-a[j][0],a[i][1]-a[j][1]),i,j)
				for i,j in itertools.combinations(list(range(len(a))),2)
				if intersect(a[i],a[j]) and dominate(a[i],a[j])
			)
			a=a[:i]+[merge(a[i],a[j])]+a[i+1:j]+a[j+1:]
		except ValueError:
			break
	return [(e[0],e[1],round(e[2],2)) for e in a]

if __name__ == '__main__':
	assert checkio([(2, 4, 2), (3, 9, 3)]) == [(2, 4, 2), (3, 9, 3)]
	assert checkio([(0, 0, 2), (-1, 0, 2)]) == [(0, 0, 2), (-1, 0, 2)]
	assert checkio([(4, 3, 2), (2.5, 3.5, 1.4)]) == [(4, 3, 2.44)]
	assert checkio([(3, 3, 3), (2, 2, 1), (3, 5, 1.5)]) == [(3, 3, 3.5)]
	assert checkio([(2, 2, 3), (0, 4, 2), (4, 6, 2), (4.7, 3, 0.5)]) == [(2, 2, 3.04), (0, 4, 2), (4, 6, 2)]