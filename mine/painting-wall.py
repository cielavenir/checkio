import bisect

def checkio(num,data):
	if num==0: return 0
	ret_idx=0
	result=0
	se=[]
	for l,r in data:
		ret_idx+=1
		while True:
			p=[l,r]
			right_idx=bisect.bisect_left(se,[l,0]) #p[0] <= se[right][0]
			if right_idx!=0:
				left_idx=right_idx-1
				if p[0]<=se[left_idx][1]: # overlap with left
					l=min(p[0],se[left_idx][0])
					r=max(p[1],se[left_idx][1])
					result-=se[left_idx][1]-se[left_idx][0]+1
					se.pop(left_idx)
					continue
			if right_idx<len(se) and se[right_idx][0]<=p[1]: # overlap with right
				l=p[0]
				r=max(p[1],se[right_idx][1])
				result-=se[right_idx][1]-se[right_idx][0]+1
				se.pop(right_idx)
				continue
			result+=p[1]-p[0]+1
			se.insert(right_idx,p)
			break
		if num<=result: return ret_idx
	return -1

if __name__=='__main__':
	assert checkio(5,[[1,5],[11,15],[2,14],[21,25]]) == 1, "1st"
	assert checkio(6,[[1,5],[11,15],[2,14],[21,25]]) == 2, "2nd"
	assert checkio(11,[[1,5],[11,15],[2,14],[21,25]]) == 3, "3rd"
	assert checkio(16,[[1,5],[11,15],[2,14],[21,25]]) == 4, "4th"
	assert checkio(21,[[1,5],[11,15],[2,14],[21,25]]) == -1, "not enough"
	assert checkio(1000000011,[[1,1000000000],[11,1000000010]]) == -1, "large"