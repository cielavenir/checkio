import itertools

tbl_num=dict(zip('AKQJT987654321',range(0,13)))
tbl_suit=dict(zip('hdcs',range(0,4)))
isflush=lambda a: all(e[1]==a[0][1] for e in a)
isstraight=lambda a: all(tbl_num[a[i+1][0]]-tbl_num[a[i][0]]==1 for i in range(0,len(a)-1))
cardnums=lambda a: sorted(len(list(v)) for k,v in itertools.groupby(sorted(tbl_num[e[0]] for e in a)))

def check(a):
	if isflush(a):
		if isstraight(a): return 8
		return 5
	if isstraight(a): return 4
	v=cardnums(a)
	if v==[5] or v==[1,4]: return 7
	if v==[2,3]: return 6
	if v==[1,1,3]: return 3
	if v==[1,2,2]: return 2
	if v==[1,1,1,2]: return 1
	return 0

def texas_referee(s):
	hand=sorted(s.split(','),key=lambda e:tbl_num[e[0]]*4+tbl_suit[e[1]])
	result_num=-1
	result=[]
	for candidate in itertools.combinations(hand,5):
		r=check(candidate)
		if result_num<r:
			result_num=r
			result=candidate
	return ','.join(result)

if __name__ == '__main__':
	assert texas_referee("Kh,Qh,Ah,9s,2c,Th,Jh") == "Ah,Kh,Qh,Jh,Th", "High Straight Flush"
	assert texas_referee("Qd,Ad,9d,8d,Td,Jd,7d") == "Qd,Jd,Td,9d,8d", "Straight Flush"
	assert texas_referee("5c,7h,7d,9s,9c,8h,6d") == "9c,8h,7h,6d,5c", "Straight"
	assert texas_referee("Ts,2h,2d,3s,Td,3c,Th") == "Th,Td,Ts,3c,3s", "Full House"
	assert texas_referee("Jh,Js,9h,Jd,Th,8h,Td") == "Jh,Jd,Js,Th,Td", "Full House vs Flush"
	assert texas_referee("Js,Td,8d,9s,7d,2d,4d") == "Td,8d,7d,4d,2d", "Flush"
	assert texas_referee("Ts,2h,Tc,3s,Td,3c,Th") == "Th,Td,Tc,Ts,3c", "Four of Kind"
	assert texas_referee("Ks,9h,Th,Jh,Kd,Kh,8s") == "Kh,Kd,Ks,Jh,Th", "Three of Kind"
	assert texas_referee("2s,3s,4s,5s,2d,7h") == "7h,5s,4s,2d,2s", "Two Pairs"
	assert texas_referee("2s,3s,4s,7s,2d,7h") == "7h,7s,4s,2d,2s", "One Pair"
	assert texas_referee("3h,4h,Th,6s,Ad,Jc") == "Ad,Jc,Th,6s,4h", "High Cards"