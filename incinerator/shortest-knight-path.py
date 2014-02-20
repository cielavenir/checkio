between=lambda a,x,b: (a)<=(x) and (x)<=(b)
x=[
	[0,3,2,3,2,3,4,5],
	[3,4,1,2,3,4,3,4],
	[2,1,4,3,2,3,4,5],
	[3,2,3,2,3,4,3,4],
	[2,3,2,3,4,3,4,5],
	[3,4,3,4,3,4,5,4],
	[4,3,4,3,4,5,4,5],
	[5,4,5,4,5,4,5,6]
]
def checkio(move):
	a=ord(move[0])-ord('a')
	b=ord(move[3])-ord('a')
	c=ord(move[1])-ord('1')
	d=ord(move[4])-ord('1')
	i=b-a
	j=d-c
	r=x[abs(i)][abs(j)];
	if abs(i)==1 and abs(j)==1:
		if (between(0,a+i*2,7) and between(0,c-j,7))or(between(0,c+j*2,7) and between(0,a-i,7)): r=2
	return r

#These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == "__main__":
	assert checkio("b1-d5") == 2, "1st example"
	assert checkio("a6-b8") == 1, "2nd example"
	assert checkio("h1-g2") == 4, "3rd example"
	assert checkio("h8-d7") == 3, "4th example"
	assert checkio("a1-h8") == 6, "5th example"