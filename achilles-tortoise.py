chase=lambda a,b,c:a*c/(a-b)

if __name__=='__main__':
	assert chase(6,3,2)==4
	assert chase(2,1,1)==2
	assert chase(15,13,56)==420