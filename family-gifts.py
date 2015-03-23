import random

family=[]
used_list=set()

def dfs(lst,couples):
	global family,used_list
	if len(lst)==len(family):
		if {lst[-1],lst[0]} not in couples and (lst[-1],lst[0]) not in used_list:
			for i in range(len(lst)):
				used_list.add((lst[i],lst[(i+1)%len(lst)]))
			return lst
	else:
		family2=family
		random.shuffle(family2)
		for e in family2:
			if e not in lst and {lst[-1],e} not in couples and (lst[-1],e) not in used_list:
				x=dfs(lst+[e],couples)
				if x:return x
	return []

def perform(couples):
	global family,used_list
	used_list=set()
	ret=[]
	for e in family:
		#if any(e in f for f in couples):
			while True:
				x=dfs([e],couples)
				if not x:break
				ret.append(x)
	return ret

def find_chains(_family, couples):
	global family,used_list
	'''
	n={
		(3,1):0,
		(4,2):2,
		(6,2):4,
		(5,2):2,
		(6,3):4,
		(9,3):6,
		(10,5):8,
		(9,0):8,
		(9,1):7,
		(10,2):7,
		(17,5):14,
	}[(len(_family),len(couples))]
	'''
	family=list(_family)
	ret=[]
	for i in range(10):
		r=perform(couples)
		if len(r)>len(ret):
			ret=r
	return ret

TESTS = {
    "Basics": [
        {
            "input": [['Doreen', 'Fred', 'Yolanda'], [['Doreen', 'Fred']]],
            "answer": [0,
                       [['Doreen', 'Fred', 'Yolanda'], [['Doreen', 'Fred']]]],
        },
        {
            "input": [['Nelson', 'Kaitlin', 'Amelia', 'Jack'],
                      [['Kaitlin', 'Jack'], ['Nelson', 'Amelia']]],
            "answer": [2,
                       [['Nelson', 'Kaitlin', 'Amelia', 'Jack'],
                        [['Kaitlin', 'Jack'], ['Nelson', 'Amelia']]]],
        },
        {
            "input": [['Allison', 'Robin', 'Petra', 'Curtis', 'Bobbie', 'Kelly'],
                      [['Allison', 'Curtis'], ['Robin', 'Kelly']]],
            "answer": [4,
                       [['Allison', 'Robin', 'Petra', 'Curtis', 'Bobbie', 'Kelly'],
                        [['Allison', 'Curtis'], ['Robin', 'Kelly']]]],
        },
        {
            "input": [['Melisa', 'Dee', 'Annmarie', 'Gerald', 'Rafael'],
                      [['Melisa', 'Gerald'], ['Rafael', 'Annmarie']]],
            "answer": [2,
                       [['Melisa', 'Dee', 'Annmarie', 'Gerald', 'Rafael'],
                        [['Melisa', 'Gerald'], ['Rafael', 'Annmarie']]]],
        },
        {
            "input": [['Ricardo', 'Eugene', 'Delia', 'Delores', 'Ella', 'Kurt'],
                      [['Eugene', 'Ella'], ['Delores', 'Kurt'], ['Ricardo', 'Delia']]],
            "answer": [4,
                       [['Ricardo', 'Eugene', 'Delia', 'Delores', 'Ella', 'Kurt'],
                        [['Eugene', 'Ella'], ['Delores', 'Kurt'], ['Ricardo', 'Delia']]]],
        },
        {
            "input": [
                ['Loraine', 'Leah', 'Jenifer', 'Russell', 'Benjamin', 'Todd', 'Maryanne', 'Penny',
                 'Matthew'], [['Loraine', 'Benjamin'], ['Leah', 'Matthew'], ['Todd', 'Jenifer']]],
            "answer": [6,
                       [['Loraine', 'Leah', 'Jenifer', 'Russell', 'Benjamin', 'Todd', 'Maryanne',
                         'Penny', 'Matthew'],
                        [['Loraine', 'Benjamin'], ['Leah', 'Matthew'], ['Todd', 'Jenifer']]]],
        },
    ],
    "Extra": [
        {
            "input": [['Alex', 'Monique', 'Tim', 'Robert', 'Joseph', 'Kitty', 'Eugenia', 'Tamika',
                       'Rene', 'Maggie'],
                      [['Kitty', 'Robert'], ['Tamika', 'Tim'], ['Joseph', 'Maggie'],
                       ['Alex', 'Eugenia'], ['Monique', 'Rene']]],
            "answer": [8,
                       [['Alex', 'Monique', 'Tim', 'Robert', 'Joseph', 'Kitty', 'Eugenia',
                         'Tamika', 'Rene', 'Maggie'],
                        [['Kitty', 'Robert'], ['Tamika', 'Tim'], ['Joseph', 'Maggie'],
                         ['Alex', 'Eugenia'], ['Monique', 'Rene']]]],
        },
        {
            "input": [
                ['Kasey', 'Madelyn', 'Marvin', 'Julia', 'Earlene', 'Cathryn', 'Fern', 'Derrick',
                 'Lois'], []],
            "answer": [8,
                       [['Kasey', 'Madelyn', 'Marvin', 'Julia', 'Earlene', 'Cathryn', 'Fern',
                         'Derrick', 'Lois'], []]],
        },
        {
            "input": [
                ['Winnie', 'Stella', 'Estela', 'Gordon', 'Jacklyn', 'Lela', 'Barbra', 'Lavonne',
                 'Maurice'], [['Maurice', 'Lela']]],
            "answer": [7,
                       [['Winnie', 'Stella', 'Estela', 'Gordon', 'Jacklyn', 'Lela', 'Barbra',
                         'Lavonne', 'Maurice'], [['Maurice', 'Lela']]]],
        },
        {
            "input": [
                ['Carl', 'Esperanza', 'Tabitha', 'Fred', 'Dixie', 'Delores', 'Erica', 'Samuel',
                 'Erin', 'Amber'], [['Carl', 'Erica'], ['Delores', 'Fred']]],
            "answer": [7,
                       [['Carl', 'Esperanza', 'Tabitha', 'Fred', 'Dixie', 'Delores', 'Erica',
                         'Samuel', 'Erin', 'Amber'], [['Carl', 'Erica'], ['Delores', 'Fred']]]],
        },
        {
            "input": [
                ['Louis', 'Theodore', 'Eleanor', 'Sondra', 'David', 'Herbert', 'Fay', 'Alexandria',
                 'Meghan', 'Nettie', 'Autumn', 'June', 'Jane', 'Jeffery', 'Herminia', 'Jeannie',
                 'Lynnette'], [['Theodore', 'Meghan'], ['Herbert', 'Eleanor'], ['Louis', 'Autumn'],
                               ['Nettie', 'David'], ['Jeffery', 'Fay']]],
            "answer": [14,
                       [['Louis', 'Theodore', 'Eleanor', 'Sondra', 'David', 'Herbert', 'Fay',
                         'Alexandria', 'Meghan', 'Nettie', 'Autumn', 'June', 'Jane', 'Jeffery',
                         'Herminia', 'Jeannie', 'Lynnette'],
                        [['Theodore', 'Meghan'], ['Herbert', 'Eleanor'], ['Louis', 'Autumn'],
                         ['Nettie', 'David'], ['Jeffery', 'Fay']]]],
        },
    ]
}

if __name__ == '__main__':
	def checker(function, family, couples, total):
		user_result = function(family.copy(), tuple(c.copy() for c in couples))
		if (not isinstance(user_result, (list, tuple)) or
				any(not isinstance(chain, (list, tuple)) for chain in user_result)):
			return False
		if len(user_result) < total:
			return False
		gifted = set()
		for chain in user_result:
			if set(chain) != family or len(chain) != len(family):
				return False
			for f, s in zip(chain, chain[1:] + [chain[0]]):
				if {f, s} in couples:
					return False
				if (f, s) in gifted:
					return False
				gifted.add((f, s))
		return True
	for k in TESTS:
		for v in TESTS[k]:
			assert checker(find_chains,set(v['input'][0]),tuple(set(e) for e in v['input'][1]),v['answer'][0])