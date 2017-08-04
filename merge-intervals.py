### painting-wall ###

import bisect

def merge_intervals(data):
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
	#cleanup
	for i in range(len(se)-2,-1,-1):
		if se[i][1]+1==se[i+1][0]:
			se[i]=(se[i][0],se[i+1][1])
			del se[i+1]
	return se
