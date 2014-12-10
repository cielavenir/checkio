from collections import Counter
#dices: 9S TH JS QH KH AS
def poker_dice(hands,category):
	numbers=Counter([e[0] for e in hands[-1]])
	suits=Counter([e[1] for e in hands[-1]])
	if 'five of a kind' not in category and [e[1] for e in numbers.most_common(1)]==[5]:
		return 'five of a kind'
	if 'four of a kind' not in category and ([e[1] for e in numbers.most_common(1)]==[4] or [e[1] for e in numbers.most_common(1)]==[5]):
		if len(hands)==3: return 'four of a kind'
		return [e for e in hands[-1] if e[0]==numbers.most_common(1)[0][0]]
	if 'full house' not in category and [e[1] for e in numbers.most_common(2)]==[3,2]:
		return 'full house'
	if 'three of a kind' not in category and ([e[1] for e in numbers.most_common(1)]==[3] or [e[1] for e in numbers.most_common(1)]==[4] or [e[1] for e in numbers.most_common(1)]==[5]):
		if len(hands)==3: return 'three of a kind'
		return [e for e in hands[-1] if e[0]==numbers.most_common(1)[0][0]]
	if 'flush' not in category and [e[1] for e in suits.most_common(1)]==[5]:
		return 'flush'
	if 'two pair' not in category and ([e[1] for e in numbers.most_common(2)]==[2,2] or [e[1] for e in numbers.most_common(2)]==[3,2]):
		return 'two pair'
	if ([e[1] for e in numbers.most_common(1)]==[2] or [e[1] for e in numbers.most_common(1)]==[3] or [e[1] for e in numbers.most_common(1)]==[4] or [e[1] for e in numbers.most_common(1)]==[5]):
		if len(hands)==3: return 'one pair'
		return [e for e in hands[-1] if e[0]==numbers.most_common(1)[0][0]]
	if len(hands)<3: return []
	return 'straight'
	#for e in ['four of a kind','full house','straight','flush','three of a kind','two pair','one pair','five of a kind']: return e