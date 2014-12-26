colors        = ['blue', 'green', 'red', 'white', 'yellow']
pets          = ['cat', 'bird', 'dog', 'fish', 'horse']
potables      = ['beer', 'coffee', 'milk', 'tea', 'water'] 
cigarettes    = ['Rothmans', 'Dunhill', 'Pall Mall', 'Winfield' , 'Marlboro']
person        = ['Brit', 'Dane', 'German', 'Norwegian', 'Swede'] 
num           = ['1','2','3','4','5']
point         = [colors,pets,potables,cigarettes,person,num]  

import itertools
lst=list(itertools.product(*point))

def checkio(data,question):
	processed = [l for l in lst if all(sum(e in l for e in d.split('-'))!=1 for d in data)]
	q = question[0].split('-')
	row = next(e for e in processed if q[0] in e)
	return next(e for e in globals()[q[1]] if e in row)

if __name__ == '__main__':
	assert checkio(['Norwegian-Dunhill','Marlboro-blue','Brit-3',
					'German-coffee','beer-white','cat-water',
					'horse-2','milk-3','4-Rothmans',
					'dog-Swede','Norwegian-1','horse-Marlboro',
					'bird-Brit','4-green','Winfield-beer',
					'Dane-blue','5-dog','blue-horse',
					'yellow-cat','Winfield-Swede','tea-Marlboro'],['fish-colors'])=='green' #1st test
	assert checkio(['Norwegian-Dunhill','Marlboro-blue','Brit-3',
					'German-coffee','beer-white','cat-water',
					'horse-2','milk-3','4-Rothmans',
					'dog-Swede','Norwegian-1','horse-Marlboro',
					'bird-Brit','4-green','Winfield-beer',
					'Dane-blue','5-dog','blue-horse',
					'yellow-cat','Winfield-Swede','tea-Marlboro'],['tea-num'])=='2' #2st test
	assert checkio(['Norwegian-Dunhill','Marlboro-blue','Brit-3',
					'German-coffee','beer-white','cat-water',
					'horse-2','milk-3','4-Rothmans',
					'dog-Swede','Norwegian-1','horse-Marlboro',
					'bird-Brit','4-green','Winfield-beer',
					'Dane-blue','5-dog','blue-horse',
					'yellow-cat','Winfield-Swede','tea-Marlboro'],['Norwegian-potables'])=='water' #3st test