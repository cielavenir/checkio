ROLL=(
	(0,3,5,2),
	(1,4,6,3),
	(5,8,10,7),
	(6,9,11,8)
)
GOAL=(1, 2, 1, 0, 2, 0, 0, 3, 0, 4, 3, 4)

def rotatecounter(marbles,idx):
	t=marbles[ROLL[idx][0]]
	marbles[ROLL[idx][0]]=marbles[ROLL[idx][1]]
	marbles[ROLL[idx][1]]=marbles[ROLL[idx][2]]
	marbles[ROLL[idx][2]]=marbles[ROLL[idx][3]]
	marbles[ROLL[idx][3]]=t
def rotateclock(marbles,idx):
	t=marbles[ROLL[idx][0]]
	marbles[ROLL[idx][0]]=marbles[ROLL[idx][3]]
	marbles[ROLL[idx][3]]=marbles[ROLL[idx][2]]
	marbles[ROLL[idx][2]]=marbles[ROLL[idx][1]]
	marbles[ROLL[idx][1]]=t
def puzzle88(marbles):
	back={marbles:marbles}
	backi={}
	q=[marbles]
	while q:
		marbles=q[0]
		q.pop(0)
		nxt=list(marbles)
		for i in range(len(ROLL)):
			rotateclock(nxt,i)
			if tuple(nxt) not in back:
				back[tuple(nxt)]=marbles
				backi[tuple(nxt)]=i+1
				q.append(tuple(nxt))
			if tuple(nxt)==GOAL: break
			rotatecounter(nxt,i)
		else:
			continue
		break
	ret=''
	g=GOAL
	while back[g]!=g:
		ret=str(backi[g])+ret
		g=back[g]
	return ret

if __name__=='__main__':
	assert puzzle88((0, 2, 1, 3, 2, 1, 4, 0, 0, 4, 0, 3)) in ('1433', '4133'), "Example"
	assert puzzle88((0, 2, 1, 2, 0, 0, 4, 1, 0, 4, 3, 3)) in ('4231', '4321'), "Rotate all"
	assert puzzle88((0, 2, 1, 2, 4, 0, 0, 1, 3, 4, 3, 0)) in ('2314', '2341', '3214', '3241'), "Four paths"