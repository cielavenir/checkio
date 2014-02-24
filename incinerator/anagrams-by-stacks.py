def checkio(str):
	start,goal=str.split('-')
	back={('',start,''):None}
	back_perform={('',start,''):None}
	q=[('',start,'')]
	while len(q)>0:
		x=q[0]
		if x[2]==goal: break
		q.pop(0)
		a=[]
		if len(x[1])>0:
			a.append(('12',(x[0],x[1][:-1],x[2]+x[1][-1])))
			if len(x[0])==0:
				a.append(('10',(x[1][-1],x[1][:-1],x[2])))
		if len(x[2])>0:
			a.append(('21',(x[0],x[1]+x[2][-1],x[2][:-1])))
			if len(x[0])==0:
				a.append(('20',(x[2][-1],x[1],x[2][:-1])))
		if len(x[0])>0:
			a+=[
				('01',('',x[1]+x[0],x[2])),
				('02',('',x[1],x[2]+x[0])),
			]
		for e in a:
			if e[1] not in back:
				back[e[1]]=x
				back_perform[e[1]]=e[0]
				q.append(e[1])
	if len(q)==0: return []
	r=[]
	while back[x]:
		r.append(back_perform[x])
		x=back[x]
	return ','.join(reversed(r))

if __name__ == '__main__':
	#This part is using only for self-checking and not necessary for auto-testing
	GOOD_ACTIONS = ("12", "10", "01", "02", "20", "21")
	def check_solution(func, anagrams, min_length):
		start, end = anagrams.split("-")
		stacks = [[], list(start), []]
		user_result = func(anagrams)
		actions = user_result.split(",")
		user_actions = []
		for act in actions:
			if act not in GOOD_ACTIONS:
				print("Wrong action")
				return False
			from_s = int(act[0])
			to_s = int(act[1])
			if not stacks[from_s]:
				print("You can not get from an empty stack")
				return False
			if to_s == 0 and stacks[to_s]:
				print("You can not push in the full buffer")
				return False
			stacks[to_s].append(stacks[from_s].pop())
			user_actions.append(act)
		res_word = ''.join(stacks[2])
		if len(actions) > min_length:
			print("It can be shorter.")
			return False
		if res_word == end:
			return True
		else:
			print("The result anagram is wrong.")
			return False
	assert check_solution(checkio, "rice-cire", 5), "rice-cire"
	assert check_solution(checkio, "tort-trot", 4), "tort-trot"
	assert check_solution(checkio, "hello-holle", 14), "hello-holle"
	assert check_solution(checkio, "anagram-mragana", 8), "anagram-mragana"
	assert check_solution(checkio, "mirror-mirorr", 25), "mirror-mirorr"