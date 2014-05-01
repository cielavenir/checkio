def count_gold(pyramid):
	data=[list(e) for e in pyramid]
	for i in range(1,len(data)):
		data[i][0]+=data[i-1][0]
		for j in range(1,i): data[i][j]+=max(data[i-1][j-1],data[i-1][j])
		data[i][i]+=data[i-1][i-1]
	return max(data[len(data)-1])

if __name__ == '__main__':
	assert count_gold((
		(1,),
		(2, 3),
		(3, 3, 1),
		(3, 1, 5, 4),
		(3, 1, 3, 1, 3),
		(2, 2, 2, 2, 2, 2),
		(5, 6, 4, 5, 6, 4, 3)
	)) == 23, "First example"
	assert count_gold((
		(1,),
		(2, 1),
		(1, 2, 1),
		(1, 2, 1, 1),
		(1, 2, 1, 1, 1),
		(1, 2, 1, 1, 1, 1),
		(1, 2, 1, 1, 1, 1, 9)
	)) == 15, "Second example"
	assert count_gold((
		(9,),
		(2, 2),
		(3, 3, 3),
		(4, 4, 4, 4)
	)) == 18, "Third example"