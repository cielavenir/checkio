dfs=lambda arr,d: d if arr[d]==0 else dfs(arr,d+1)
checkio=lambda arr: dfs(arr,0)

if __name__ == '__main__':
	assert checkio([1,1,0,3]) == 2, 'First'
	assert checkio([1,0,1]) == 1, 'Second'
	assert checkio([1,10,1,0,1]) == 3, 'Third'
	print('All ok :)')