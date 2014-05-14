def checkio(data):
	while True:
		f=True
		nxt=[]
		for e in data:
			try:
				for f in e:
					nxt.append(f)
				f=False
			except TypeError:
				nxt.append(e)
		if f: return nxt
		data=nxt

if __name__ == '__main__':
	assert checkio([1, 2, 3]) == [1, 2, 3], 'First example'
	assert checkio([1, [2, 2, 2], 4]) == [1, 2, 2, 2, 4], 'Second example'
	assert checkio([[[2]], [4, [5, 6, [6], 6, 6, 6], 7]]) == [2, 4, 5, 6, 6, 6, 6, 6, 7], 'Third example'