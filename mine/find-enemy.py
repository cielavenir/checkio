import math
def convert(s):
	ax=ord(s[0])-65
	a=[float(ax)*math.sqrt(3)/2,-float(s[1:])+1]
	if ax%2: a[1]-=0.5
	return a
def dist(s,t):
	ax=ord(s[0])-65
	ay=int(s[1:])-ax//2
	bx=ord(t[0])-65
	by=int(t[1:])-bx//2
	dx=bx-ax
	dy=by-ay
	return abs(dx+dy) if dx*dy>0 else max(abs(dx),abs(dy))

T=['N','NW','SW','S','SE','NE']
def find_enemy(a_,d,b_):
	eps=1e-9
	a=convert(a_)
	b=convert(b_)
	b[0]-=a[0]
	b[1]-=a[1]
	arg=math.atan2(b[1],b[0])-math.pi*T.index(d)/3
	if arg<-math.pi: arg+=math.pi
	if arg<-math.pi: arg+=math.pi
	if (math.pi*1/6)+eps<arg<-eps+math.pi*5/6:
		d='F'
	elif math.pi*-5/6+eps<arg<-eps+math.pi*-1/6:
		d='B'
	elif abs(arg)<=math.pi*1/2:
		# math.pi*-1/6<=arg<=math.pi*1/6:
		d='R'
	else:
		d='L'
	return [d,dist(a_,b_)]

if __name__ == '__main__':
	assert find_enemy('G5', 'N', 'G4') == ['F', 1], "N-1"
	assert find_enemy('G5', 'N', 'I4') == ['R', 2], "NE-2"
	assert find_enemy('G5', 'N', 'J6') == ['R', 3], "SE-3"
	assert find_enemy('G5', 'N', 'G9') == ['B', 4], "S-4"
	assert find_enemy('G5', 'N', 'B7') == ['L', 5], "SW-5"
	assert find_enemy('G5', 'N', 'A2') == ['L', 6], "NW-6"
	assert find_enemy('G3', 'NE', 'C5') == ['B', 4], "[watch your six!]"
	assert find_enemy('H3', 'SW', 'E2') == ['R', 3], "right"
	assert find_enemy('A4', 'S', 'M4') == ['L', 12], "true left"
	print("You are good to go!")
