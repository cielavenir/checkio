from fractions import Fraction
def divide_pie(groups):
	s=sum(map(abs,groups))
	p=Fraction(1)
	for e in groups: p=p-Fraction(e,s) if e>0 else p*Fraction(s+e,s)
	return (p.numerator,p.denominator)

if __name__ == '__main__':
	assert isinstance((2, -2), (tuple, list)), "Return tuple or list"
	assert tuple(divide_pie((2, -1, 3))) == (1, 18), "Example"
	assert tuple(divide_pie((1, 2, 3))) == (0, 1), "All know about the pie"
	assert tuple(divide_pie((-1, -1, -1))) == (8, 27), "One by one"
	assert tuple(divide_pie((10,))) == (0, 1), "All together"