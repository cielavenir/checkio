def solve(head,enemy):
	try:
		return max(
			solve(enemy[i],enemy[:i]+enemy[i+1:])+1
			for i in range(len(enemy)) if any(
				enemy[i][n]==head[n] and
				not any(
					enemy[j][n]==head[n] and (head[n^1]<enemy[j][n^1]<enemy[i][n^1] or enemy[i][n^1]<enemy[j][n^1]<head[n^1])
					for j in range(len(enemy))
				)
				for n in (0,1)
			)
		)
	except ValueError:
		return 0

berserk_rook=lambda head,enemy: solve(head,list(enemy))

if __name__=='__main__':
	assert berserk_rook('d3', {'d6', 'b6', 'c8', 'g4', 'b8', 'g6'}) == 5
	assert berserk_rook('a2', {'f6', 'f2', 'a6', 'f8', 'h8', 'h6'}) == 6
	assert berserk_rook('a2', {'f6', 'f8', 'f2', 'a6', 'h6'}) == 4