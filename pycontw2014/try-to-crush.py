from itertools import groupby

def check(state):
	for j in range(len(state[0])):
		for k,v in groupby([state[i][j] for i in range(len(state))]):
			if len(list(v))>=3: return 1
	for i in range(len(state)):
		for k,v in groupby([state[i][j] for j in range(len(state[0]))]):
			if len(list(v))>=3: return 1
	return 0

def checkio(state):
	r=0
	#vertical
	for i in range(len(state)-1):
		for j in range(len(state[0])):
			state[i][j],state[i+1][j]=state[i+1][j],state[i][j]
			r+=check(state)
			state[i][j],state[i+1][j]=state[i+1][j],state[i][j]
	#horizontal
	for i in range(len(state)):
		for j in range(len(state[0])-1):
			state[i][j],state[i][j+1]=state[i][j+1],state[i][j]
			r+=check(state)
			state[i][j],state[i][j+1]=state[i][j+1],state[i][j]
	return r

if __name__ == '__main__':
	assert checkio([[2,1,3,2],
					[1,1,3,3],
					[2,2,1,3],
					[1,1,3,2],
					[3,2,3,2]]) == 7
	print('Done')