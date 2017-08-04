def long_repeat(s):
	if not s:return 0
	r=c=j=1
	for i in range(1,len(s)):
		if s[i]==s[i-1]:
			c+=1
			if r<c:
				r=c
				j=i
		else:
			c=1
	return r
