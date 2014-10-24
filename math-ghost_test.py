SIZE=10
import itertools
from sklearn.linear_model import LinearRegression
def predict_ghost(values):
	factors=[(1.0/e,e,e**2,e**3) for e in range(1,SIZE+1)]
	clf = LinearRegression()
	clf.fit(factors,values)
	return clf.predict((1.0/(SIZE+1),(SIZE+1),(SIZE+1)**2,(SIZE+1)**3))

if __name__=='__main__':
	N=20
	SCORE_DIST = 0.1
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
	for dummy in range(N):
		formula_x = generate_formula()
		# formula_y = generate_formula()
		values = []
		for x in range(1, SIZE+2):
			try:
				i = round(eval(formula_x), 3)
				# j = round(eval(formula_y) % 10, 3)
				values.append(i)
			except OverflowError:
				dummy -= 1
				break
		else:
			score_distance = (max(values) - min(values)) * SCORE_DIST
			user_result=predict_ghost(values[:-1])
			distance = abs(user_result - values[-1])
			score = 0 if distance >= score_distance else round(100 * ((score_distance - distance) / score_distance))
			print('real=%f, predicted=%f, score=%d'%(values[-1],user_result,score))