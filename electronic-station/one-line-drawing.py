from collections import defaultdict

def dfs(roads,cur,points,num):
	for nxt in points[cur]:
		num[nxt]+=2
		cur_road=list(sorted([cur,nxt]))
		r=None
		if num[nxt]<=len(points[nxt]) and cur_road not in roads:
			r=dfs(roads+[cur_road],nxt,points,num)
		num[nxt]-=2
		if r!=None: return [cur]+r
	if all(len(points[e])==num[e] for e in points): return [cur]

def draw(segments):
	points={}
	for _p in segments:
		p,q=((_p[0],_p[1]),(_p[2],_p[3]))
		if p not in points: points[p]=[]
		if q not in points: points[q]=[]
		points[p].append(q)
		points[q].append(p)
	odd=[]
	for p in points:
		if len(points[p])%2==1: odd.append(p)
	if 1==len(odd) or 2<len(odd): return []
	cur,end=(odd[0],odd[1]) if odd else (q,q)
	num=defaultdict(int)
	num[cur]+=1
	num[end]-=1
	for nxt in points[cur]:
		num[nxt]+=2
		r=None
		if num[nxt]<=len(points[nxt]):
			r=dfs([list(sorted([cur,nxt]))],nxt,points,num)
		num[nxt]-=2
		if r!=None: return [cur]+r

if __name__ == '__main__':
	def checker(func, in_data, is_possible=True):
		user_result = func(in_data)
		if not is_possible:
			if user_result:
				print("How did you draw this?")
				return False
			else:
				return True
		if len(user_result) < 2:
			print("More points please.")
			return False
		data = list(in_data)
		for i in range(len(user_result) - 1):
			f, s = user_result[i], user_result[i + 1]
			if (f + s) in data:
				data.remove(f + s)
			elif (s + f) in data:
				data.remove(s + f)
			else:
				print("The wrong segment {}.".format(f + s))
				return False
		if data:
			print("You forgot about {}.".format(data[0]))
			return False
		return True
	assert checker(draw,
				   {(1, 2, 1, 5), (1, 2, 7, 2), (1, 5, 4, 7), (4, 7, 7, 5)}), "Example 1"
	assert checker(draw,
				   {(1, 2, 1, 5), (1, 2, 7, 2), (1, 5, 4, 7),
					(4, 7, 7, 5), (7, 5, 7, 2), (1, 5, 7, 2), (7, 5, 1, 2)},
				   False), "Example 2"
	assert checker(draw,
				   {(1, 2, 1, 5), (1, 2, 7, 2), (1, 5, 4, 7), (4, 7, 7, 5),
					(7, 5, 7, 2), (1, 5, 7, 2), (7, 5, 1, 2), (1, 5, 7, 5)}), "Example 3"