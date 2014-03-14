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
	tr=[list(e) for e in zip(*matrix)]
	a=(0,225,315)
	for i in range(-2,3):
		for j in range(-2,3):
			for k in range(-2,3):
				x=[tr[z]+[a[z]+(i,j,k)[z]*360] for z in range(len(a))]
				result=list(zip(*gauss(x)))[-1]
				if any(not -180<=e<=180 or e.denominator>1 for e in result): continue
				return [int(e) for e in result]

#These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
	print(checkio([
		[1, 2, 3],
		[3, 1, 2],
		[2, 3, 1]]))
	print(checkio([
		[1, 4, 2],
		[2, 1, 2],
		[2, 2, 1]]))