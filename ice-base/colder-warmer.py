def checkio(steps):
	global x,y,z
	xf=False
	if len(steps)==1:
		x=z=None
		return [0,0]
	if x==None:
		if len(steps)==2 or steps[-1][2]==1:
			if steps[-1][0]<8:
				return [steps[-1][0]+2,steps[-1][1]]
			x=steps[-1][0]
		if steps[-1][2]==0:
			x=steps[-1][0]-1
		if steps[-1][2]==-1:
			x=steps[-1][0]-2
		xf=True
	if z==None:
		if xf or steps[-1][2]==1:
			if steps[-1][1]<8:
				return [x,steps[-1][1]+2]
			y=steps[-1][1]
		if steps[-1][2]==0:
			y=steps[-1][1]-1
		if steps[-1][2]==-1:
			y=steps[-1][1]-2
		if [x,y]!=steps[-1][:2]:
			z=len(steps)
			return [x,y]
		z=len(steps)-1
	if len(steps)-z==1: return [steps[z][0]+1,steps[z][1]+0]
	if len(steps)-z==2: return [steps[z][0]+0,steps[z][1]+1]
	if len(steps)-z==3: return [steps[z][0]+1,steps[z][1]+1]

#These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
	#This part is using only for self-checking and not necessary for auto-testing
	from math import hypot
	MAX_STEP = 12
	def check_solution(func, goal, start):
		#print('---')
		prev_steps = [start]
		for step in range(MAX_STEP):
			row, col = func([s[:] for s in prev_steps])
			#print(row,col)
			if [row, col] == goal:
				return True
			if 10 <= row or 0 > row or 10 <= col or 0 > col:
				print("You gave wrong coordinates.")
				return False
			prev_distance = hypot(prev_steps[-1][0] - goal[0], prev_steps[-1][1] - goal[1])
			distance = hypot(row - goal[0], col - goal[1])
			alteration = 0 if prev_distance == distance else (1 if prev_distance > distance else -1)
			prev_steps.append([row, col, alteration])
		print("Too many steps")
		return False
	assert check_solution(checkio, [7, 7], [5, 5, 0]), "1st example"
	assert check_solution(checkio, [5, 6], [0, 0, 0]), "2nd example"
	assert check_solution(checkio, [9, 9], [0, 0, 0]), "3rd example"
	assert check_solution(checkio, [9, 0], [7, 7, 0]), "4th example"