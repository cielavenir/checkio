from fractions import Fraction
def gauss(a):
	if not a or len(a)==0: return None
	n=len(a)
	for i in range(n):
		if a[i][i]==0:
			for j in range(i+1,n):
				if a[j][i]!=0:
					for k in range(i,n+1): a[i][k]+=a[j][k]
					break
		for j in range(n):
			if i!=j:
				r = Fraction(a[j][i],1) / a[i][i]
				for k in range(i,n+1): a[j][k] = a[j][k] - a[i][k]*r
	for i in range(n):
		x=Fraction(a[i][i],1)
		for j in range(len(a[i])):
			a[i][j] /= x
	return a

def checkio(matrix):
	lst={'gold':0,'tin':1,'iron':2,'copper':3}
	m=[[1,1,1,1,1]]
	for k,v in matrix.items():
		a=[0,0,0,0,v]
		for e in k.split('-'): a[lst[e]]=1
		m.append(a)
	return gauss(m)[0][4]

if __name__ == '__main__':
	checkio({
		'gold-tin': Fraction(1, 2),
		'gold-iron': Fraction(1, 3),
		'gold-copper': Fraction(1, 4),
	}) == Fraction(1, 24)
	checkio({
		'tin-iron': Fraction(1, 2),
		'iron-copper': Fraction(1, 2),
		'copper-tin': Fraction(1, 2),
	}) == Fraction(1, 4)