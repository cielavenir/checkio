import itertools,random
num=4
def hit_and_blow(a,b):
	hit=sum(a[i]==b[i] for i in range(4))
	blow=len(a)+len(b)-len(set(iter(a+b)))
	return (hit,blow-hit)

def checkio(data):
	global lst
	if len(data)==0:
		lst=list(''.join(e) for e in itertools.permutations(iter('0123456789'),num))
		return '0123'
	last=data[-1].split()
	hit=int(last[1][0])
	blow=int(last[1][2])
	last=last[0]
	for i in range(len(lst)-1,-1,-1):
		if hit_and_blow(lst[i],last)!=(hit,blow): lst.pop(i)
	return random.choice(lst)

if __name__ == '__main__':
	#This part is using only for self-checking and not necessary for auto-testing
	def check_solution(func, goal):
		recent = []
		for step in range(8):
			user_result = func(recent)
			bulls = cows = 0
			for u, g in zip(user_result, goal):
				if u == g:
					bulls += 1
				elif u in goal:
					cows += 1
			recent.append("{0} {1}B{2}C".format(user_result, bulls, cows))
			if bulls == 4:
				print("{0} Win with {1} steps.".format(goal, step + 1))
				return True
		print("{0} Fail.".format(goal))
		return False
	assert check_solution(checkio, "1234"), "1234"
	assert check_solution(checkio, "6130"), "6130"
	assert check_solution(checkio, "0317"), "0317"
	assert check_solution(checkio, "9876"), "9876"