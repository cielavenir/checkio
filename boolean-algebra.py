import operator
boolean=lambda x,y,z:{
	'conjunction':operator.and_,
	'disjunction':operator.or_,
	'implication':lambda x,y:not x or y,
	'exclusive':operator.xor,
	'equivalence':operator.eq,
}[z](x,y)

if __name__ == '__main__':
	assert boolean(1, 0, "conjunction") == 0, "and"
	assert boolean(1, 0, "disjunction") == 1, "or"
	assert boolean(1, 1, "implication") == 1, "material"
	assert boolean(0, 1, "exclusive") == 1, "xor"
	assert boolean(0, 1, "equivalence") == 0, "same?"