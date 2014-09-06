#I'm going to show what's happening in 4th case.
def mind_switcher(_journal):
	journal=[tuple(e) for e in _journal]
	helper=('nikola','sophia')
	lst=set()
	for e in journal:
		for f in e: lst.add(f)
	lst=list(lst)
	modified=lst[:]
	for e in journal:
		idx0=modified.index(e[0])
		idx1=modified.index(e[1])
		modified[idx0],modified[idx1]=modified[idx1],modified[idx0]
	lst,modified=modified,lst # there might be a small misunderstanding...
	#print(lst)
	#['lister', 'driller', 'digger', 'drawer', 'hater', 'planer', 'scout', 'melter', 'hammer']
	#print(modified)
	#['driller', 'lister', 'melter', 'digger', 'drawer', 'scout', 'planer', 'hammer', 'hater']
	lst2=[]
	modified2=[]
	while lst:
		_lst=[lst[0]]
		_modified=[modified[0]]
		lst=lst[1:]
		modified=modified[1:]
		cur=_modified[0]
		while cur!=_lst[0]:
			idx=lst.index(cur)
			_lst.append(lst[idx])
			lst=lst[:idx]+lst[idx+1:]
			_modified.append(modified[idx])
			cur=modified[idx]
			modified=modified[:idx]+modified[idx+1:]
		if len(_lst)>1:
			lst2.append(_lst)
			modified2.append(_modified)
	#print(lst2)
	#[['lister', 'driller'], ['digger', 'melter', 'hammer', 'hater', 'drawer'], ['planer', 'scout']]
	#print(modified2)
	#[['driller', 'lister'], ['melter', 'hammer', 'hater', 'drawer', 'digger'], ['scout', 'planer']]
	ret=[]
	for i in range(len(lst2)):
		ret.append({helper[0],lst2[i][0]})
		for j in range(1,len(lst2[i])):
			ret.append({helper[1],lst2[i][j]})
		ret.append({helper[0],lst2[i][1]})
		ret.append({helper[1],lst2[i][0]})
	if len(lst2)%2==1: ret.append({helper[0],helper[1]})
	#print(ret)
	return ret

if __name__ == '__main__':
	assert mind_switcher(({'scout', 'super'},))
	assert mind_switcher(({'hater', 'scout'}, {'planer', 'hater'}))
	assert mind_switcher([['digger', 'melter'], ['melter', 'planer'], ['digger', 'planer']])
	assert mind_switcher([['melter', 'drawer'], ['hammer', 'hater'], ['melter', 'hater'], ['scout', 'planer'],
					  ['driller', 'lister'], ['digger', 'drawer']])