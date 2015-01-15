from collections import defaultdict
def rec(lst,hist,visit,cur,prev):
	visit.add(cur)
	ret=[]
	for e in lst[cur]:
		if e!=prev:
			try:
				idx=hist.index(e)
				if len(hist[idx:]+[e])>len(ret):
					ret=hist[idx:]+[e]
			except ValueError:
				hist.append(e)
				ret=max(ret,rec(lst,hist,visit,e,cur),key=len)
				hist.pop()
	return ret
			
def find_cycle(_lst):
	lst=defaultdict(list)
	for e in _lst:
		lst[e[0]].append(e[1])
		lst[e[1]].append(e[0])
	keys=list(lst)
	visit=set()
	ret=[]
	for e in keys:
		if e not in visit:
			ret=max(ret,rec(lst,[],visit,e,-1),key=len)
	return ret

if __name__ == '__main__':
	print find_cycle(((1, 2), (2, 3), (3, 4), (4, 5), (5, 7), (7, 6), (8, 5), (8, 4), (1, 5), (2, 4)))