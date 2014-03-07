import bisect

def checkio(num,data):
	if num==0: return 0
	ret_idx=0
	result=0
	se=[]
	for l,r in data:
		ret_idx+=1
		right_idx=bisect.bisect_left(se,(l,0)) #l <= se[right_idx][0]
		if right_idx!=0:
			left_idx=right_idx-1
			if l<=se[left_idx][1]: # overlap with left
				l=se[left_idx][0]
				r=max(r,se[left_idx][1])
				result-=se[left_idx][1]-se[left_idx][0]+1
				se.pop(left_idx)
				right_idx-=1
		while right_idx<len(se) and se[right_idx][0]<=r: # overlap with right
			r=max(r,se[right_idx][1])
			result-=se[right_idx][1]-se[right_idx][0]+1
			se.pop(right_idx)
		result+=r-l+1
		se.insert(right_idx,(l,r))
		if num<=result: return ret_idx
	return -1

if __name__=='__main__':
	assert checkio(5,[[1,5],[11,15],[2,14],[21,25]]) == 1, "1st"
	assert checkio(6,[[1,5],[11,15],[2,14],[21,25]]) == 2, "2nd"
	assert checkio(11,[[1,5],[11,15],[2,14],[21,25]]) == 3, "3rd"
	assert checkio(16,[[1,5],[11,15],[2,14],[21,25]]) == 4, "4th"
	assert checkio(21,[[1,5],[11,15],[2,14],[21,25]]) == -1, "not enough"
	assert checkio(1000000011,[[1,1000000000],[11,1000000010]]) == -1, "large"