def backtrack(i,j):
	if i==0 or j==0: return {""}
	if (i,j) in memo: return memo[(i,j)]
	elif a[i-1]==b[j-1]:
		x={e+a[i-1] for e in backtrack(i-1,j-1)}
		if lcs[i][j]==lcs[i-1][j]: x.update(backtrack(i-1,j))
		if lcs[i][j]==lcs[i][j-1]: x.update(backtrack(i,j-1))
		memo[(i,j)]=x
		return x
	x=set()
	if lcs[i][j-1]>=lcs[i-1][j]: x.update(backtrack(i,j-1))
	if lcs[i-1][j]>=lcs[i][j-1]: x.update(backtrack(i-1,j))
	memo[(i,j)]=x
	return x

def common(x,y):
	global memo,lcs,a,b
	memo={}
	a=x
	b=y
	lcs=[[0]*(len(y)+1) for i in range(len(x)+1)]
	for i in range(1,len(a)+1):
		for j in range(1,len(b)+1):
			lcs[i][j]=max(max(lcs[i-1][j],lcs[i][j-1]),lcs[i-1][j-1]+(a[i-1]==b[j-1]))
	r=','.join(sorted(backtrack(len(a),len(b))))
	return r

if __name__=='__main__':
	assert common("ACGTC", "TTACTC") == "ACTC"
	assert common("CGCTA", "TACCG") == "CC,CG,TA"
	assert common("GCTT", "AAAAA") == ""
	assert common("TGCAAAACGT", "ACGTAAAATGCA") == "CAAAAC,CAAAAG,CAAAAT,GAAAAC,GAAAAG,GAAAAT,TAAAAC,TAAAAG,TAAAAT"