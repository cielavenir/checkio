x=[[0,0],[0,0]]
for i in range(500):
	for j in range(1,i*2+1): x.append([-i,-i+j])
	for j in range(1,i*2+1): x.append([-i+j,i])
	for j in range(1,i*2+1): x.append([i,i-j])
	for j in range(1,i*2+1): x.append([i-j,-i])
def checkio(data):
	a, b = data
	return abs(x[a][0]-x[b][0])+abs(x[a][1]-x[b][1])

#These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
	assert checkio([1, 9]) == 2, "First"
	assert checkio([9, 1]) == 2, "Reverse First"
	assert checkio([10, 25]) == 1, "Neighbours"
	assert checkio([5, 9]) == 4, "Diagonal"
	assert checkio([26, 31]) == 5, "One row"
	assert checkio([50, 16]) == 10, "One more test"