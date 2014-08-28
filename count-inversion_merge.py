def M(l,r):
	if l+1>=r: return 0
	if l+2==r:
		if A[l]<=A[l+1]: return 0
		A[l],A[l+1]=A[l+1],A[l]
		return 1
	m = (l+r)//2
	i=l
	j=m
	k=l
	cl=M(l,m)
	cr=M(m,r)
	c=0
	while i<m and j<r:
		if A[i]<=A[j]:
			W[k]=A[i]
			k+=1
			i+=1
		else:
			W[k]=A[j]
			k+=1
			j+=1
			c+=m-i
	while i<m:
		W[k]=A[i]
		k+=1
		i+=1
	while j<r:
		W[k]=A[j]
		k+=1
		j+=1
	for i in range(l,r): A[i]=W[i]
	return cl+cr+c

def count_inversion(a):
	global A,W
	A=list(a)
	W=[0]*len(A)
	return M(0,len(A))

if __name__=='__main__':
	assert count_inversion((1, 2, 5, 3, 4, 7, 6)) == 3
	assert count_inversion((0, 1, 2, 3)) == 0