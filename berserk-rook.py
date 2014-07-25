def solve(head,enemy):
	r=0
	for i in range(len(enemy)):
		if enemy[i][0]==head[0] and not any(enemy[j][0]==head[0] and (head[1]<enemy[j][1]<enemy[i][1] or enemy[i][1]<enemy[j][1]<head[1]) for j in range(len(enemy))):
			r=max(r,solve(enemy[i],enemy[:i]+enemy[i+1:])+1)
		if enemy[i][1]==head[1] and not any(enemy[j][1]==head[1] and (head[0]<enemy[j][0]<enemy[i][0] or enemy[i][0]<enemy[j][0]<head[0]) for j in range(len(enemy))):
			r=max(r,solve(enemy[i],enemy[:i]+enemy[i+1:])+1)
	return r

berserk_rook=lambda head,enemy: solve(head,list(enemy))

if __name__=='__main__':
	assert berserk_rook('d3', {'d6', 'b6', 'c8', 'g4', 'b8', 'g6'}) == 5
	assert berserk_rook('a2', {'f6', 'f2', 'a6', 'f8', 'h8', 'h6'}) == 6
	assert berserk_rook('a2', {'f6', 'f8', 'f2', 'a6', 'h6'}) == 4