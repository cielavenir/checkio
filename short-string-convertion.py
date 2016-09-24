def maximum3(a):
	if len(a)==0: [None,0]
	ret = [a[0],0]
	for i in range(1,len(a)):
		if ret[0] < a[i]: ret = [a[i],i]
	return ret

def steps_to_convert(x, y):
	#initialize
	a = [[0]*(len(y)+1) for _ in range(len(x)+1)]
	back = [[0]*(len(y)+1) for _ in range(len(x)+1)]
	tx = ""; ty = ""; t=""
	#DP
	for i in range(1,len(a)):
		a[i][0] = a[i-1][0] - 1
		back[i][0]=[i-1,0,  "a"]
	for j in range(1,len(a[0])):
		a[0][j] = a[0][j-1] - 1
		back[0][j]=[0,  j-1,"b"]
	for i in range(1,len(a)):
		for j in range(1,len(a[0])):
			z = maximum3([a[i-1][j-1] if x[i-1] == y[j-1] else a[i-1][j-1]-1, a[i-1][j]-1, a[i][j-1]-1])
			a[i][j]=z[0]
			if z[1]==0:   back[i][j]=[i-1,j-1,"c"]
			elif z[1]==1: back[i][j]=[i-1,j,  "a"]
			elif z[1]==2: back[i][j]=[i,  j-1,"b"]
	return -a[len(x)][len(y)]

if __name__ == "__main__":
	assert steps_to_convert('line1', 'line1') == 0, "eq"
	assert steps_to_convert('line1', 'line2') == 1, "2"
	assert steps_to_convert('line', 'line2') == 1, "none to 2"
	assert steps_to_convert('ine', 'line2') == 2, "need two more"
	assert steps_to_convert('line1', '1enil') == 4, "everything is opposite"
	assert steps_to_convert('', '') == 0, "two empty"
	assert steps_to_convert('l', '') == 1, "one side"
	assert steps_to_convert('', 'l') == 1, "another side"
	print("You are good to go!")
