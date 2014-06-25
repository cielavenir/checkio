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
			else:
				return None
		for j in range(n):
			if i!=j:
				r = Fraction(a[j][i],a[i][i])
				for k in range(i,n+1): a[j][k] = a[j][k] - a[i][k]*r
	for i in range(n):
		x=Fraction(a[i][i],1)
		for j in range(len(a[i])):
			a[i][j] /= x
	return a

def expected(n, s, t, b):
	#perform probably-dice
	a=[0]*(s*(n+1)+1)
	for i in range(1,s+1):
		a[i+s]=Fraction(1,s)**n
	for e in range(n-1):
		for i in reversed(range(0,s*n+1)):
			a[i+s]=sum(a[i:i+s])
	l = len(b)
	A = [[int(i==j) for i in range(l)]+[int(j!=t)] for j in range(l)]
	for start in range(l):
		if start != t:
			for roll in range(n,s*n+1):
				end = roll + start
				end = (end + b[end%l])%l
				A[start][end] -= a[roll+s]
	return float(gauss(A)[0][-1])

if __name__ == '__main__':
	def almost_equal(checked, correct, significant_digits=2):
		precision = 0.1 ** significant_digits
		assert correct - precision < checked < correct + precision
	def addTest(c, i, a):
		almost_equal(expected(*i),a)
	addTest("Basics", [1, 4, 1, [0, 0, 0, 0]], 4.00)
	addTest("Basics", [1, 4, 2, [0, 0, 0, 0]], 4.00)
	addTest("Basics", [1, 4, 3, [0, 0, 0, 0]], 4.00)
	addTest("Basics", [1, 4, 3, [0, 2, 1, 0]], 1.33)
	addTest("Basics", [1, 4, 3, [0, -1, -2, 0]], 4.00)
	addTest("Basics", [1, 3, 3, [0, 0, 0, 0, 0]], 3.51)
	addTest("Basics", [1, 6, 1, [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]], 8.57)
	addTest("Basics", [2, 6, 1, [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]], 10.21)
	addTest("Basics", [1, 10, 1, [0, 0, 0, 0, 0, 0, 0, 0]], 7.20)
	addTest("Jumps", [1, 6, 9, [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]], 9.81)
	addTest("Jumps", [1, 6, 9, [0, 1, 0, 0, 0, 0, 0, 0, 0, 0]], 9.66)
	addTest("Jumps", [1, 6, 9, [0, 2, 0, 0, 0, 0, 0, 0, 0, 0]], 8.48)
	addTest("Jumps", [1, 6, 9, [0, 3, 0, 0, 0, 0, 0, 0, 0, 0]], 8.65)
	addTest("Jumps", [1, 6, 9, [0, 2, 1, 0, 0, 0, 0, 0, 0, 0]], 7.66)
	addTest("Jumps", [1, 6, 9, [0, 2, 2, 0, 0, 0, 0, 0, 0, 0]], 7.77)
	addTest("Jumps", [1, 6, 9, [0, 2, 3, 0, 0, 0, 0, 0, 0, 0]], 7.75)
	addTest("Jumps", [1, 6, 9, [0, 3, 1, 0, 0, 0, 0, 0, 0, 0]], 7.79)
	addTest("Jumps", [1, 6, 9, [0, 3, 2, 1, 0, 0, 0, 0, 0, 0]], 8.00)
	addTest("Jumps", [1, 6, 9, [0, 3, 3, 3, 0, 0, 0, 0, 0, 0]], 8.00)
	addTest("Jumps", [1, 6, 9, [0, 0, 0, 0, 0, 0, 0, 0, -1, 0]], 9.85)
	addTest("Jumps", [1, 6, 9, [0, 0, 0, 0, 0, 0, 0, 0, -2, 0]], 9.95)
	addTest("Jumps", [1, 6, 9, [0, 0, 0, 0, 0, 0, 0, 0, -3, 0]], 9.79)
	addTest("Jumps", [1, 6, 9, [0, 0, 0, 0, 0, 0, 0, 0, -7, 0]], 11.08)
	addTest("Jumps", [1, 6, 9, [0, 0, 0, 0, 0, 0, 0, 0, -99, 0]], 5.16)
	addTest("Jumps", [1, 6, 9, [0, 0, 0, 0, 2, -2, 0, 0, 0, 0]], 9.77)
	addTest("Jumps", [1, 6, 9, [0, 0, 0, 0, -2, 2, 0, 0, 0, 0]], 11.37)
	addTest("Big", [1, 4, 29, [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]], 29.60)
	addTest("Big", [1, 6, 29, [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]], 29.71)
	addTest("Big", [3, 10, 29, [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]], 30.00)
	addTest("Big", [2, 6, 29, [0, -1, -2, -3, -4, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]], 31.67)
	addTest("Big", [2, 6, 29, [0, -2, -3, -4, -5, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]], 5.70)
	addTest("Big", [1, 6, 29, [0, -1, -2, -3, -4, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]], 35.67)
	addTest("Big", [1, 6, 29, [0, -2, -3, -4, -5, -6, -7, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]], 1.00)