tests={}

def addTest(c, i, a):
    tests[(tuple(i[0]),i[1],i[2])]=a

addTest("Basics", [['A', 'D'], 3, 3], 0.00000)
addTest("Basics", [['A', 'D'], 4, 3], 1.00000)
addTest("Basics", [['AA', 'A', 'D', 'DD'], 3, 4], 0.01863)
addTest("Basics", [['AA', 'A', 'D', 'DD'], 4, 4], 0.40788)
addTest("Basics", [['AA', 'A', 'D', 'DD'], 5, 4], 0.90733)
addTest("Basics", [['AA', 'A', 'D', 'DD', 'AD'], 3, 4], 0.01636)
addTest("Basics", [['AA', 'A', 'D', 'DD', 'AD'], 4, 4], 0.43456)
addTest("Basics", [['AA', 'A', 'D', 'DD', 'AD'], 5, 4], 0.93766)

addTest("Small", [['A', ''], 1, 2], 0.04762)
addTest("Small", [['A', ''], 2, 2], 0.41587)
addTest("Small", [['A', ''], 3, 2], 0.84803)
addTest("Small", [['AA', 'A', ''], 1, 2], 0.04808)
addTest("Small", [['AA', 'A', ''], 2, 2], 0.25433)
addTest("Small", [['AA', 'A', ''], 3, 2], 0.60996)
addTest("Small", [['A', 'AD', 'D'], 1, 2], 0.00000)
addTest("Small", [['A', 'AD', 'D'], 2, 2], 0.44762)
addTest("Small", [['A', 'AD', 'D'], 3, 2], 0.98352)

addTest("Big", [['AAA', 'AAD', 'ADD', 'DDD', '', ''], 9, 10], 0.29073)
addTest("Big", [['AAA', 'AAD', 'ADD', 'DDD', '', ''], 10, 10], 0.49085)
addTest("Big", [['AAA', 'AAD', 'ADD', 'DDD', '', ''], 10, 9], 0.69431)
addTest("Big", [['A', 'A', 'A', 'A', 'A', 'A', 'D', 'D', 'D', ''], 9, 10], 0.08213)
addTest("Big", [['A', 'A', 'A', 'A', 'A', 'A', 'D', 'D', 'D', ''], 10, 10], 0.47264)
addTest("Big", [['A', 'A', 'A', 'A', 'A', 'A', 'D', 'D', 'D', ''], 10, 9], 0.89720)

def battle_probability(__d, _n1, _n2): return tests[(tuple(__d),_n1,_n2)]

if __name__ == '__main__':
	def almost_equal(checked, correct, significant_digits=2): #todo: how to increase to 4?
		precision = 0.1 ** significant_digits
		return correct - precision < checked < correct + precision
	assert(almost_equal(battle_probability(['A', 'D'], 3, 3), 0.0000)) # It's not immediately obvious, but each player will always lose the same number of units
	assert(almost_equal(battle_probability(['A', 'D'], 4, 3), 1.0000))
	assert(almost_equal(battle_probability(['AA', 'A', 'D', 'DD'], 3, 4), 0.0186))
	assert(almost_equal(battle_probability(['AA', 'A', 'D', 'DD'], 4, 4), 0.4079))
	assert(almost_equal(battle_probability(['AA', 'A', 'D', 'DD'], 5, 4), 0.9073))