z=0
def guess(attempts):
	global z
	if z==0:
		z=1
		return 2,1
	if z==1:
		z=2
		return 3,1
	if z==2:
		z=3
		return 5,1
	if z==3:
		z=4
		return 7,1
	idx=0
	result=[e[0] for e in attempts[1:]]
	while True:
		if result==[idx%2,idx%3,idx%5,idx%7]:
			z=0
			return 9,idx
		idx+=1
'''
	#irb> (0..100).map{|e|[e%2,e%3,e%5,e%7]}
	a=[[e%2,e%3,e%5,e%7] for e in range(101)]
	for index, item in enumerate(a):
		if item==result:
			return 9,index
	#This "9" is just dummy.
'''

if __name__ == '__main__':
	MAX_ATTEMPT = 13
	def initial_referee(data):
		data["attempt_count"] = 0
		data["guess"] = 0
		return data
	def check_solution(func, goal, initial):
		prev_steps = [initial]
		for attempt in range(MAX_ATTEMPT):
			divisor, guess_number = func(prev_steps[:])
			if guess_number == goal:
				return True
			prev_steps.append((goal % divisor, divisor))
		print("Too many attempts.")
		return False
	assert check_solution(guess, 47, (2, 5)), "1st example"
	assert check_solution(guess, 94, (3, 7)), "2nd example"
	assert check_solution(guess, 52, (0, 2)), "3rd example"