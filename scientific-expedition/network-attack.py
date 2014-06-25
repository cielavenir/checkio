def capture(matrix):
	infected={}
	queue=[[0,0]]
	while len(queue)>0:
		machine,time=queue.pop(0)
		if machine not in infected or infected[machine]>time:
			infected[machine]=time
			for i in range(len(matrix)):
				if i!=machine and matrix[machine][i]:
					queue.append([i,time+matrix[i][i]])
	return max(infected.values())

if __name__ == '__main__':
	assert capture([[0, 1, 0, 1, 0, 1],
					[1, 8, 1, 0, 0, 0],
					[0, 1, 2, 0, 0, 1],
					[1, 0, 0, 1, 1, 0],
					[0, 0, 0, 1, 3, 1],
					[1, 0, 1, 0, 1, 2]]) == 8, "Base example"
	assert capture([[0, 1, 0, 1, 0, 1],
					[1, 1, 1, 0, 0, 0],
					[0, 1, 2, 0, 0, 1],
					[1, 0, 0, 1, 1, 0],
					[0, 0, 0, 1, 3, 1],
					[1, 0, 1, 0, 1, 2]]) == 4, "Low security"
	assert capture([[0, 1, 1],
					[1, 9, 1],
					[1, 1, 9]]) == 9, "Small"