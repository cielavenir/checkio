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
	#irb> (0..100).map{|e|[e%2,e%3,e%5,e%7]}
	a=[[0, 0, 0, 0], [1, 1, 1, 1], [0, 2, 2, 2], [1, 0, 3, 3], [0, 1, 4, 4], [1, 2, 0, 5], [0, 0, 1, 6], [1, 1, 2, 0], [0, 2, 3, 1], [1, 0, 4, 2], [0, 1, 0, 3], [1, 2, 1, 4], [0, 0, 2, 5], [1, 1, 3, 6], [0, 2, 4, 0], [1, 0, 0, 1], [0, 1, 1, 2], [1, 2, 2, 3], [0, 0, 3, 4], [1, 1, 4, 5], [0, 2, 0, 6], [1, 0, 1, 0], [0, 1, 2, 1], [1, 2, 3, 2], [0, 0, 4, 3], [1, 1, 0, 4], [0, 2, 1, 5], [1, 0, 2, 6], [0, 1, 3, 0], [1, 2, 4, 1], [0, 0, 0, 2], [1, 1, 1, 3], [0, 2, 2, 4], [1, 0, 3, 5], [0, 1, 4, 6], [1, 2, 0, 0], [0, 0, 1, 1], [1, 1, 2, 2], [0, 2, 3, 3], [1, 0, 4, 4], [0, 1, 0, 5], [1, 2, 1, 6], [0, 0, 2, 0], [1, 1, 3, 1], [0, 2, 4, 2], [1, 0, 0, 3], [0, 1, 1, 4], [1, 2, 2, 5], [0, 0, 3, 6], [1, 1, 4, 0], [0, 2, 0, 1], [1, 0, 1, 2], [0, 1, 2, 3], [1, 2, 3, 4], [0, 0, 4, 5], [1, 1, 0, 6], [0, 2, 1, 0], [1, 0, 2, 1], [0, 1, 3, 2], [1, 2, 4, 3], [0, 0, 0, 4], [1, 1, 1, 5], [0, 2, 2, 6], [1, 0, 3, 0], [0, 1, 4, 1], [1, 2, 0, 2], [0, 0, 1, 3], [1, 1, 2, 4], [0, 2, 3, 5], [1, 0, 4, 6], [0, 1, 0, 0], [1, 2, 1, 1], [0, 0, 2, 2], [1, 1, 3, 3], [0, 2, 4, 4], [1, 0, 0, 5], [0, 1, 1, 6], [1, 2, 2, 0], [0, 0, 3, 1], [1, 1, 4, 2], [0, 2, 0, 3], [1, 0, 1, 4], [0, 1, 2, 5], [1, 2, 3, 6], [0, 0, 4, 0], [1, 1, 0, 1], [0, 2, 1, 2], [1, 0, 2, 3], [0, 1, 3, 4], [1, 2, 4, 5], [0, 0, 0, 6], [1, 1, 1, 0], [0, 2, 2, 1], [1, 0, 3, 2], [0, 1, 4, 3], [1, 2, 0, 4], [0, 0, 1, 5], [1, 1, 2, 6], [0, 2, 3, 0], [1, 0, 4, 1], [0, 1, 0, 2]]
	for index, item in enumerate(a):
		if item[0]==attempts[1][0] and item[1]==attempts[2][0] and item[2]==attempts[3][0] and item[3]==attempts[4][0]:
			return 9,index
	#This "9" is just dummy.

#These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
	checkio([(1, 5)])									# the number has a remainder 1
	checkio([(1, 5), (1, 2)])							# the number has a remainder 1
	checkio([(1, 5), (1, 2), (2, 3)])					# the number has a remainder 2
	checkio([(1, 5), (1, 2), (2, 3), (5, 6)])			# the number has a remainder 5
	checkio([(1, 5), (1, 2), (2, 3), (5, 6), (3, 4)])	# the number has a remainder 3