def digit_stack(commands):
	r=0
	stack=[]
	for e in commands:
		a=e.split()
		if a[0]=='PUSH': stack.append(a[1])
		elif len(stack):
			r+=int(stack[-1])
			if a[0]=='POP': stack.pop()
	return r

if __name__ == '__main__':
	assert digit_stack(["PUSH 3", "POP", "POP", "PUSH 4", "PEEK",
						"PUSH 9", "PUSH 0", "PEEK", "POP", "PUSH 1", "PEEK"]) == 8, "Example"
	assert digit_stack(["POP", "POP"]) == 0, "pop, pop, zero"
	assert digit_stack(["PUSH 9", "PUSH 9", "POP"]) == 9, "Push the button"
	assert digit_stack([]) == 0, "Nothing"