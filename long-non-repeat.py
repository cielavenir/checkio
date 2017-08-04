from collections import defaultdict
def non_repeat(s):
	head=tail=r=0
	t=''
	d=defaultdict(int)
	for c in s:
		tail+=1
		d[c]+=1
		while d[c]>1:
			d[s[head]]-=1
			head+=1
		if r<tail-head:
			r=tail-head
			t=s[head:tail]
	return t
