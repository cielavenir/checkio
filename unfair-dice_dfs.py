def dfs(enemy,se,player,sp):
	if len(enemy)==len(player):
		l=len(enemy)
		result=sum(sum(int(player[i]>enemy[j])-int(player[i]<enemy[j]) for j in range(l)) for i in range(l))
		if result>0: yield player
	elif len(enemy)==len(player)+1:
		n=se-sp
		if n>=player[-1]:
			for e in dfs(enemy,se,player+[n],sp+n): yield e
	else:
		for i in range(player[-1],(se-sp)//(len(enemy)-len(player))+1):
			for e in dfs(enemy,se,player+[i],sp+i): yield e

def winning_die(enemy):
	se=sum(enemy)
	for i in range(1,se//len(enemy)+1):
		for e in dfs(enemy,se,[i],i):
			#print(e)
			return e
	return []

if __name__ == '__main__':
	def test_dice(enemy):
		player=winning_die(enemy)
		assert len(player)==len(enemy)
		assert sum(player)==sum(enemy)
		total = 0
		for p in player:
			for e in enemy:
				if p > e:
					total += 1
				elif p < e:
					total -= 1
		return total > 0
	assert test_dice([4, 6, 10, 10])
	assert test_dice([3, 3, 3, 3, 6, 6])
	assert test_dice([4, 4, 4, 4, 4, 4])
	assert test_dice([1, 1, 1, 4])
	assert test_dice([2, 3, 4, 5, 6, 7])
	assert test_dice([1, 1, 1, 2, 2, 2, 3, 3, 3, 4])
	assert winning_die([1, 2, 3, 4, 5, 6]) == []