def follow(s):
	x=y=0
	for c in s:
		if c=='l':y-=1
		if c=='r':y+=1
		if c=='f':x+=1
		if c=='b':x-=1
	return (y,x)

'''
D=[[0,1],[1,0],[0,-1],[-1,0]]
def follow(s):
	x=y=d=0
	for c in s:
		if c=='l':d=(d-1)%4
		if c=='r':d=(d+1)%4
		if c=='f':y+=D[d][0];x+=D[d][1]
		if c=='b':y-=D[d][0];x-=D[d][1]
	return (y,x)
'''
