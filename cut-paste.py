def checkio(data):
	data2=[]
	for n,e in enumerate(data):
		cur=0
		for i in range(1,len(e)):
			if e[i-1]==e[i]:
				data2.append([e[cur:i],n,cur,i,1])
				cur=i
		data2.append([e[cur:len(e)],n,cur,len(e),1])
	rets=data2[0][0]
	ret=[data2[0][1:]]
	data2=data2[1:]
	while data2:
		for i,e in enumerate(data2):
			#append
			if rets[-1]!=e[0][0]:
				rets+=e[0]
				ret+=[e[1:]]
				data2.pop(i)
				break
			elif rets[-1]!=e[0][-1]:
				rets+=e[0][::-1]
				ret+=[[e[1],e[3]-1,e[2]-1,-1]]
				data2.pop(i)
				break
			#prepend
			elif rets[0]!=e[0][0]:
				rets=e[0][::-1]+rets
				ret=[[e[1],e[3]-1,e[2]-1,-1]]+ret
				data2.pop(i)
				break
			elif rets[0]!=e[0][-1]:
				rets=e[0]+rets
				ret=[e[1:]]+ret
				data2.pop(i)
				break
	s="''.join(("+','.join('data[%d][%d:%d:%d]'%tuple(e) for e in ret)+"))"
	print(s)
	print(eval(s))

if __name__ == '__main__':
	checkio(['11000101', '101'])