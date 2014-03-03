from itertools import combinations
from fractions import Fraction
from random import randint
ZDE='ZeroDivisionError'

def dfs(a,x,y):
	if len(a)<2: yield (a[0],'x' if x==a[0] else 'y')
	for i in range(len(a)-1):
		for l in dfs(a[:i+1],x,y):
			for r in dfs(a[i+1:],x,y):
				yield (l[0]+r[0] if ZDE not in [l[0],r[0]] else ZDE,'(%s+%s)'%(l[1],r[1]))
				yield (l[0]-r[0] if ZDE not in [l[0],r[0]] else ZDE,'(%s-%s)'%(l[1],r[1]))
				yield (l[0]*r[0] if ZDE not in [l[0],r[0]] else ZDE,'(%s*%s)'%(l[1],r[1]))
				yield (Fraction(l[0],r[0]) if ZDE not in [l[0],r[0]] and r[0]!=0 else ZDE,'(%s/%s)'%(l[1],r[1]))

def gen(x,y):
	for l in range(2,5):
		for i in range(1,l):
			for e in combinations(range(l),i):
				a=[x]*l
				for f in e: a[f]=y
				for n,s in dfs(a,x,y):
					yield (n,s)

def checkio(data):
	global lst
	if len(data)==0:
		lst=set([e[1] for e in gen(2,3)])
		return ['x+y',2,3]
	newlst=[]
	for n,s in gen(data[-1][0],data[-1][1]):
		if n==Fraction(*data[-1][2]) and s in lst: newlst.append(s)
	lst=set(newlst)
	return [newlst[0],randint(-100, 100),randint(-100, 100)] #lol

#This part is using only for self-testing
#It's "light" version of the grader
#The hidden expression should be correct (non x/(y-y))
if __name__ == '__main__':
	def test_it(hidden_expression, solver):
		from fractions import Fraction
		from random import randint
		def check_is_right(guess, expression):
			for _ in range(10):
				result_guess = 0
				result_expr = 1
				for __ in range(100):
					x, y = Fraction(randint(-100, 100)), Fraction(randint(-100, 100))
					try:
						result_expr = eval(expression)
						result_guess = eval(guess)
					except ZeroDivisionError:
						continue
					break
				if result_guess != result_expr:
					return False
			return True
		input_data = []
		for step in range(50):
			user_guess, x_real, y_real = solver(input_data)
			x = Fraction(x_real)
			y = Fraction(y_real)
			try:
				result = eval(hidden_expression)
				output = [result.numerator, result.denominator]
			except ZeroDivisionError:
				output = ZDE
			input_data.append([x_real, y_real, output])
			if check_is_right(user_guess, hidden_expression):
				return True
		else:
			return False
	assert test_it("x+y", checkio), "x+y"
	assert test_it("x*y", checkio), "x*y"
	assert test_it("x-y", checkio), "x-y"
	assert test_it("x/y", checkio), "x/y"