def checkio(enemy):
	player=sorted(enemy)
	l=len(player)
	#n=min(player[l-1]-1,l-1)
	#player[l-1]-=n
	#for i in range(n): player[i]+=1
	for i in range(player[l-1]-1):
		player[i%(l-1)]+=1
	player[l-1]=1
	result=sum(sum(int(player[i]>enemy[j])-int(player[i]<enemy[j]) for j in range(l)) for i in range(l))
	return [] if result<=0 else player

if __name__ == '__main__':
	def test_dice(enemy):
		player=checkio(enemy)
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
	assert test_dice([3, 3, 3, 3, 6, 6])
	assert test_dice([4, 4, 4, 4, 4, 4])
	assert test_dice([1, 1, 1, 4])
	assert test_dice([2, 3, 4, 5, 6, 7])
	assert test_dice([1, 1, 1, 2, 2, 2, 3, 3, 3, 4])
	assert checkio([1, 2, 3, 4, 5, 6]) == []