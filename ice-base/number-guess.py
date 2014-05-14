z=0
def checkio(attempts):
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
		if result==[idx%2,idx%3,idx%5,idx%7]: return 9,idx
		idx+=1
'''
	#irb> (0..100).map{|e|[e%2,e%3,e%5,e%7]}
	a=[[e%2,e%3,e%5,e%7] for e in range(101)]
	for index, item in enumerate(a):
		if item==result:
			return 9,index
	#This "9" is just dummy.
'''

'''
if __name__ == '__main__':
	checkio([(1, 5)])									# the number has a remainder 1
	checkio([(1, 5), (1, 2)])							# the number has a remainder 1
	checkio([(1, 5), (1, 2), (2, 3)])					# the number has a remainder 2
	checkio([(1, 5), (1, 2), (2, 3), (5, 6)])			# the number has a remainder 5
	checkio([(1, 5), (1, 2), (2, 3), (5, 6), (3, 4)])	# the number has a remainder 3
'''