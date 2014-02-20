def dfs(h,a,c,edges):
	if a[-1]=='1' and len(set(a))==8: return ''.join(a)
	for e in h[c]:
		edge=''.join(sorted([c,e]))
		if edge not in edges:
			r=dfs(h,a+[e],e,edges+[edge])
			if r: return r
	return None

def checkio(teleports_string):
	h={}
	for e in teleports_string.split(','):
		if e[0] not in h: h[e[0]]=[]
		if e[1] not in h: h[e[1]]=[]
		h[e[0]].append(e[1])
		h[e[1]].append(e[0])
	return dfs(h,['1'],'1',[])

if __name__ == "__main__":
	print(checkio("12,23,34,45,56,67,78,81"))  # "123456781"
	print(checkio("12,28,87,71,13,14,34,35,45,46,63,65"))  # "1365417821"
	print(checkio("12,15,16,23,24,28,83,85,86,87,71,74,56"))  # "12382478561"
	print(checkio("13,14,23,25,34,35,47,56,58,76,68"))  # "132586741"