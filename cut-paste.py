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
	return s

if __name__ == '__main__':
	def check_solution(func, data):
		try:
			solver = func(data[:])
			stripe = eval(solver)
			if any((type(stripe) != str,
					len(stripe) != sum(len(ribbon) for ribbon in data),
					any(a not in '01' for a in stripe),
					any(a == b for a, b in zip(stripe, stripe[1:])))):
				return False
			cuts = sum(a == b for ribbon in data for a, b in zip(ribbon, ribbon[1:]))
			commutator = [[False] * len(ribbon) for ribbon in data]
			data = ['0' * len(ribbon) for ribbon in data]
			res = eval(solver)
			if '1' in res:
				return False
			targets = []
			for i, ribbon in enumerate(data):
				ribbon = list(ribbon)
				for j in range(len(ribbon)):
					ribbon[j] = '1'
					data[i] = ''.join(ribbon)
					res = eval(solver)
					if res.count('1') != 1:
						return False
					k = res.index('1')
					targets.append(k)
					commutator[i][j], ribbon[j] = k, '0'
				data[i] = ''.join(ribbon)
			targets.sort()
			if targets != list(range(len(stripe))):
				return False
			for i, switches in enumerate(commutator):
				for a, b in zip(switches, switches[1:]):
					cuts -= abs(a - b) != 1
			return not cuts
		except Exception:
			return False
	assert check_solution(checkio, ['11000101', '101']), 'Basic sample'