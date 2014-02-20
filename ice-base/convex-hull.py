def _det(p, q, r):
	sum1 = q[0]*r[1] + p[0]*q[1] + r[0]*p[1]
	sum2 = q[0]*p[1] + r[0]*q[1] + p[0]*r[1]
	return sum1 - sum2

def _isRightTurn(a):
	p=a[0][0]
	q=a[1][0]
	r=a[2][0]
	assert p != q and q != r and p != r
	if _det(p, q, r) <= 0:
		return 1
	else:
		return 0

def checkio(P):
	points=[[e,i] for i,e in enumerate(P)]
	points.sort()
	# Build upper half of the hull.
	upper = [points[0], points[1]]
	for p in points[2:]:
		upper.append(p)
		while len(upper) > 2 and not _isRightTurn(upper[-3:]):
			del upper[-2]
	# Build lower half of the hull.
	points.reverse()
	lower = [points[0], points[1]]
	for p in points[2:]:
		lower.append(p)
		while len(lower) > 2 and not _isRightTurn(lower[-3:]):
			del lower[-2]
	# Remove duplicates.
	del lower[0]
	del lower[-1]
	# Concatenate both halfs and return.
	return [i for e,i in upper+lower]

#These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
	assert checkio(
		[[7, 6], [8, 4], [7, 2], [3, 2], [1, 6], [1, 8], [4, 9]]
	) == [4, 5, 6, 0, 1, 2, 3], "First example"
	assert checkio(
		[[3, 8], [1, 6], [6, 2], [7, 6], [5, 5], [8, 4], [6, 8]]
	) == [1, 0, 6, 3, 5, 2], "Second example"