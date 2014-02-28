from functools import reduce
def checkio(line):
	S='abcdefghijklmnopqrstuvwxyz_.,! '
	return reduce(lambda s,e: s+S.index(e)%3+1,iter(line),0)

if __name__ == '__main__':
	assert checkio('diamonds are forever') == 38, 'First'
	assert checkio('just do it') == 18, 'Second'
	assert checkio('tastes great, less filling') == 48, 'Third'
	print('All is ok')