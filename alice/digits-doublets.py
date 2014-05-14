def diff1(t,s):
	r=0
	for i in range(len(t)):
		if t[i]!=s[i]: r+=1
		if r>1: return False
	return True

def checkio(numbers):
	numbers=[str(e) for e in numbers]
	f=numbers.pop(0)
	l=numbers.pop()
	if f==l: return [int(f),int(l)]
	h={f:None}
	q=[(f,0)]
	while len(q)>0:
		x,y=q.pop(0)
		if diff1(x,l):
			q.append((l,y+1))
			h[l]=x
			break
		for e in numbers:
			if e not in h and diff1(x,e):
				q.append((e,y+1))
				h[e]=x
	if len(q)==0: return []
	a=[l]
	x=l
	while h[x]:
		a.append(h[x])
		x=h[x]
	return [int(e) for e in reversed(a)]

if __name__ == '__main__':
	assert checkio([123, 991, 323, 321, 329, 121, 921, 125, 999]) == [123, 121, 921, 991, 999], "First"
	assert checkio([111, 222, 333, 444, 555, 666, 121, 727, 127, 777]) == [111, 121, 127, 727, 777], "Second"
	assert checkio([456, 455, 454, 356, 656, 654]) == [456, 454, 654], "Third, [456, 656, 654] is correct too"