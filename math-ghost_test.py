import itertools
from sklearn.linear_model import LinearRegression
def predict_ghost(values):
	factors=[(1.0/e,e,e**2,e**3) for e in range(1,11)]
	clf = LinearRegression()
	clf.fit(factors,values)
	return clf.predict((1.0/11,11,11**2,11**3))

if __name__=='__main__':
	import random
	def generate_formula(prob_x=0.3, prob_bracket=0.2):
		formula = "x"
		for _ in range(15):
			operation = random.choice(["+", "-", "*", "/"])
			formula += operation
			if random.random() < prob_x:
				formula += "x"
			else:
				formula += str(round(random.random() * 10, 3))
			if random.random() < prob_bracket:
				formula = "(" + formula + ")"
		return formula
	for dummy in range(20):
		formula_x = generate_formula()
		# formula_y = generate_formula()
		values = []
		for x in range(1, 12):
			try:
				# print(eval(formula_x))
				i = round(eval(formula_x), 3)
				# j = round(eval(formula_y) % 10, 3)
				values.append(i)
			except OverflowError:
				dummy -= 1
				break
		else:
			print(formula_x)
			print(abs(predict_ghost(values[:-1])-values[-1]))