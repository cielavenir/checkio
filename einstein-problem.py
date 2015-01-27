color       = ['blue', 'green', 'red', 'white', 'yellow']
pet         = ['cat', 'bird', 'dog', 'fish', 'horse']
beverage    = ['beer', 'coffee', 'milk', 'tea', 'water'] 
cigarettes  = ['Rothmans', 'Dunhill', 'Pall Mall', 'Winfield' , 'Marlboro']
nationality = ['Brit', 'Dane', 'German', 'Norwegian', 'Swede'] 
number      = ['1','2','3','4','5']

import itertools
lst=list(itertools.product(color,pet,beverage,cigarettes,nationality,number))
def answer(data,question):
	processed = [l for l in lst if all(sum(e in l for e in d.split('-'))!=1 for d in data)]
	q = question.split('-')
	row = next(e for e in processed if q[0] in e)
	return next(e for e in globals()[q[1]] if e in row)

if __name__ == '__main__':
	assert answer(['Norwegian-Dunhill','Marlboro-blue','Brit-3',
					'German-coffee','beer-white','cat-water',
					'horse-2','milk-3','4-Rothmans',
					'dog-Swede','Norwegian-1','horse-Marlboro',
					'bird-Brit','4-green','Winfield-beer',
					'Dane-blue','5-dog','blue-horse',
					'yellow-cat','Winfield-Swede','tea-Marlboro'],'fish-color')=='green' #1st test
	assert answer(['Norwegian-Dunhill','Marlboro-blue','Brit-3',
					'German-coffee','beer-white','cat-water',
					'horse-2','milk-3','4-Rothmans',
					'dog-Swede','Norwegian-1','horse-Marlboro',
					'bird-Brit','4-green','Winfield-beer',
					'Dane-blue','5-dog','blue-horse',
					'yellow-cat','Winfield-Swede','tea-Marlboro'],'tea-number')=='2' #2st test
	assert answer(['Norwegian-Dunhill','Marlboro-blue','Brit-3',
					'German-coffee','beer-white','cat-water',
					'horse-2','milk-3','4-Rothmans',
					'dog-Swede','Norwegian-1','horse-Marlboro',
					'bird-Brit','4-green','Winfield-beer',
					'Dane-blue','5-dog','blue-horse',
					'yellow-cat','Winfield-Swede','tea-Marlboro'],'Norwegian-beverage')=='water' #3st test