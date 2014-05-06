from collections import Counter
#dices: 9S TH JS QH KH AS
def checkio(hands,category):
	numbers=Counter([e[0] for e in hands[-1]])
	suits=Counter([e[1] for e in hands[-1]])
	if not 'Five of a Kind' in category and [e[1] for e in numbers.most_common(1)]==[5]:
		return 'Five of a Kind'
	if not 'Four of a Kind' in category and ([e[1] for e in numbers.most_common(1)]==[4] or [e[1] for e in numbers.most_common(1)]==[5]):
		if len(hands)==3: return 'Four of a Kind'
		return [e for e in hands[-1] if e[0]==numbers.most_common(1)[0][0]]
	if not 'Full House' in category and [e[1] for e in numbers.most_common(2)]==[3,2]:
		return 'Full House'
	if not 'Three of a Kind' in category and ([e[1] for e in numbers.most_common(1)]==[3] or [e[1] for e in numbers.most_common(1)]==[4] or [e[1] for e in numbers.most_common(1)]==[5]):
		if len(hands)==3: return 'Three of a Kind'
		return [e for e in hands[-1] if e[0]==numbers.most_common(1)[0][0]]
	if not 'Flush' in category and [e[1] for e in suits.most_common(1)]==[5]:
		return 'Flush'
	if not 'Two Pair' in category and ([e[1] for e in numbers.most_common(2)]==[2,2] or [e[1] for e in numbers.most_common(2)]==[3,2]):
		return 'Two Pair'
	if ([e[1] for e in numbers.most_common(1)]==[2] or [e[1] for e in numbers.most_common(1)]==[3] or [e[1] for e in numbers.most_common(1)]==[4] or [e[1] for e in numbers.most_common(1)]==[5]):
		if len(hands)==3: return 'One Pair'
		return [e for e in hands[-1] if e[0]==numbers.most_common(1)[0][0]]
	if len(hands)<3: return []
	return 'Straight'
	#for e in ['Four of a Kind','Full House','Straight','Flush','Three of a Kind','Two Pair','One Pair','Five of a Kind']: return e