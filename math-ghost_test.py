SIZE=10
import itertools,math
#from sklearn.linear_model import LinearRegression
def predict_ghost(values):
	#factors=[(1.0/e,e,e**2,e**3,math.cos(e)) for e in range(1,SIZE+1)]
	#clf = LinearRegression()
	#clf.fit(factors,values)
	#return clf.predict((1.0/(SIZE+1),(SIZE+1),(SIZE+1)**2,(SIZE+1)**3,math.cos(SIZE+1)))
	return values[-2]+2*(values[-1]-values[-2])

if __name__ == '__main__':
	import math
	from random import choice, random
	TESTS_QUANTITY = 30
	SCORE_DIST = 0.1
	def generate_formula(prob_x=0.5, prob_bracket=0.2, prob_trig=0.25):
		formula = "x"
		for _ in range(15):
			operation = choice(["+", "-", "*", "/"])
			formula += operation
			if random() < prob_x:
				formula += "x"
			else:
				formula += str(round(random() * 10, 3))
			if random() < prob_bracket:
				formula = "(" + formula + ")"
			if random() < prob_trig:
				formula = "math." + choice(["sin", "cos"]) + "(" + formula + ")"
		return formula
	def calculate_score(f):
		score = 0
		for count in range(TESTS_QUANTITY):
			formula_x = generate_formula()
			values = []
			for x in range(1, 12):
				try:
					i = round(eval(formula_x), 3)
					values.append(i)
				except OverflowError:
					count -= 1
					break
			else:
				if abs(max(values) - min(values)) < 1:
					count -= 1
				else:
					score_distance = (max(values) - min(values)) * SCORE_DIST
					user_result = f(values[:-1])
					distance = abs(user_result - values[-1])
					if distance < score_distance:
						score += round(100 * ((score_distance - distance) / score_distance))
		print("Total score: {}".format(score))
		return score
	calculate_score(predict_ghost)