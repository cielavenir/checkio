from itertools import combinations
checkio=lambda data: sum(e[0]>e[1]+e[2] for e in combinations(reversed(sorted(data)),3))

if __name__ == '__main__':
	assert checkio([4, 2, 10]) == 1, "First"
	assert checkio([1, 2, 3]) == 0, "Second"
	assert checkio([5, 2, 9, 6]) == 2, "Third"