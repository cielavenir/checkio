#According to https://github.com/Bryukh-Checkio-Tasks/checkio-task-box-probability/blob/master/verification/tests.py ,
#max(step) is 11. So O(2^n) will work.

def dfs(b,w,prob,step):
	if step==0: return prob*w/(w+b)
	if b==0: return dfs(1,w-1,prob,step-1)
	if w==0: return dfs(b-1,1,prob,step-1)
	return dfs(b-1,w+1,prob*b/(w+b),step-1)+dfs(b+1,w-1,prob*w/(w+b),step-1)

def checkio(marbles, step):
	b=sum(e=='b' for e in iter(marbles))
	w=sum(e=='w' for e in iter(marbles))
	return dfs(b,w,1.0,step-1)

if __name__ == '__main__':
	assert checkio('bbw', 3) == 0.48, "1st example"
	assert checkio('wwb', 3) == 0.52, "2nd example"
	assert checkio('www', 3) == 0.56, "3rd example"
	assert checkio('bbbb', 1) == 0, "4th example"
	assert checkio('wwbb', 4) == 0.5, "5th example"
	assert checkio('bwbwbwb', 5) == 0.48, "6th example"