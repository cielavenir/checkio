from fractions import Fraction
def dfs(s):
	yield int(s)
	for i in range(len(s)-1):
		for l in dfs(s[:i+1]):
			for r in dfs(s[i+1:]):
				yield l+r
				yield l-r
				yield l*r
				if r!=0: yield Fraction(l,r)

checkio=lambda s: all(e!=100 for e in dfs(s))

#These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
	assert checkio('000000') == True, "All zeros"
	assert checkio('707409') == True, "You can not transform it to 100"
	assert checkio('595347') == False, "(5 + ((9 / (3 / 34)) - 7)) = 100"
	assert checkio('271353') == False, "(2 - (7 * (((1 / 3) - 5) * 3))) = 100"