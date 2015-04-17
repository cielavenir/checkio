M=500000
table=[0]*(M+1)
table[0]=table[1]=1
primes=[]
for i in range(2,M+1):
	if not table[i]:
		primes.append(i)
		for j in range(i*2,M+1,i):
			table[j]=1
dic=[None]*(M+1)
dic[0]=[]
for e0 in primes:
	used=set()
	e=e0
	p=1
	while e<=M:
		for i in range(M-e,-1,-1):
			if dic[i+e] is None and dic[i] is not None and (not i or i not in used):
				dic[i+e]=dic[i]+[(e0,p)]
				used.add(i+e)
		e*=e0
		p+=1
	if e0>50: break

decompose=lambda n:dic[n] if dic[n] else False

print(decompose(371344))