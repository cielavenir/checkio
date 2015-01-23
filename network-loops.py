from collections import defaultdict
def rec(lst,hist,visit,cur,prev):
	visit.add(cur)
	ret=[]
	for e in lst[cur]:
		if e!=prev:
			try:
				idx=hist.index(e)
				if len(hist[idx:]+[e])>len(ret):
					ret=hist[idx:]+[e]
			except ValueError:
				hist.append(e)
				ret=max(ret,rec(lst,hist,visit,e,cur),key=len)
				hist.pop()
	return ret
			
def find_cycle(_lst):
	lst=defaultdict(list)
	for e in _lst:
		lst[e[0]].append(e[1])
		lst[e[1]].append(e[0])
	keys=list(lst)
	visit=set()
	ret=[]
	for e in keys:
		if e not in visit:
			ret=max(ret,rec(lst,[],visit,e,-1),key=len)
	return ret

TESTS = {
	"Basics": [
		{
			"input": [[1, 2], [2, 3], [3, 4], [4, 5], [5, 7], [7, 6], [8, 5], [8, 4], [1, 5], [2, 4], [1, 8]],
			"answer": [[[1, 2], [2, 3], [3, 4], [4, 5], [5, 7], [7, 6], [8, 5], [8, 4], [1, 5], [2, 4], [1, 8]], 6],
			"vertexes": 8
		},
		{
			"input": [[1, 2], [2, 3], [3, 4], [4, 5], [5, 7], [7, 6], [8, 5], [8, 4], [1, 5], [2, 4]],
			"answer": [[[1, 2], [2, 3], [3, 4], [4, 5], [5, 7], [7, 6], [8, 5], [8, 4], [1, 5], [2, 4]], 6],
			"vertexes": 8
		},

		{
			"input": [[1, 2], [2, 3], [3, 4], [4, 5], [5, 7], [7, 6], [8, 4], [1, 5], [2, 4]],
			"answer": [[[1, 2], [2, 3], [3, 4], [4, 5], [5, 7], [7, 6], [8, 4], [1, 5], [2, 4]], 5],
			"vertexes": 8
		},
		{
			"input": [[1, 4], [3, 6], [5, 8], [1, 2], [1, 8], [2, 3], [1, 7], [2, 5], [6, 7], [2, 6], [2, 7], [1, 5],
					  [5, 7], [4, 8], [3, 5], [3, 4], [2, 8], [3, 8], [4, 7], [2, 4], [3, 7], [4, 5], [7, 8], [4, 6],
					  [1, 6], [6, 8], [1, 3], [5, 6]],
			"answer": [
				[[1, 4], [3, 6], [5, 8], [1, 2], [1, 8], [2, 3], [1, 7], [2, 5], [6, 7], [2, 6], [2, 7], [1, 5], [5, 7],
				 [4, 8], [3, 5], [3, 4], [2, 8], [3, 8], [4, 7], [2, 4], [3, 7], [4, 5], [7, 8], [4, 6], [1, 6], [6, 8],
				 [1, 3], [5, 6]], 8],
			"vertexes": 8
		},
	],
	"Extra": [
		{
			"input": [[3, 4], [2, 3], [1, 2]],
			"answer": [[[3, 4], [2, 3], [1, 2]], 0],
			"vertexes": 4,
			"no": 0
		},
		{
			"input": [[2, 8], [1, 8], [3, 6], [1, 5], [3, 8], [5, 6], [2, 7], [2, 4], [2, 5], [2, 6], [1, 2], [4, 6],
					  [5, 8], [4, 5], [1, 7], [2, 3], [1, 3], [4, 8], [3, 7], [5, 7], [3, 5], [3, 4], [7, 8], [4, 7],
					  [6, 7], [1, 4], [1, 6], [6, 8]],
			"answer": [
				[[2, 8], [1, 8], [3, 6], [1, 5], [3, 8], [5, 6], [2, 7], [2, 4], [2, 5], [2, 6], [1, 2], [4, 6], [5, 8],
				 [4, 5], [1, 7], [2, 3], [1, 3], [4, 8], [3, 7], [5, 7], [3, 5], [3, 4], [7, 8], [4, 7], [6, 7], [1, 4],
				 [1, 6], [6, 8]], 8],
			"vertexes": 8,
			"no": 1
		},
		{
			"input": [[3, 4], [1, 6], [3, 6], [2, 5], [1, 4], [4, 7], [3, 7]],
			"answer": [[[3, 4], [1, 6], [3, 6], [2, 5], [1, 4], [4, 7], [3, 7]], 5],
			"vertexes": 7,
			"no": 2
		},
		{
			"input": [[7, 10], [2, 4], [1, 5], [7, 9], [4, 10], [4, 7], [6, 8], [3, 8], [1, 4], [2, 9], [4, 9], [3, 7],
					  [2, 8], [1, 2], [3, 9], [1, 3], [2, 5], [5, 8], [9, 10], [3, 10], [8, 9], [6, 10]],
			"answer": [
				[[7, 10], [2, 4], [1, 5], [7, 9], [4, 10], [4, 7], [6, 8], [3, 8], [1, 4], [2, 9], [4, 9], [3, 7],
				 [2, 8], [1, 2], [3, 9], [1, 3], [2, 5], [5, 8], [9, 10], [3, 10], [8, 9], [6, 10]], 10],
			"vertexes": 10,
			"no": 3
		},
		{
			"input": [[1, 7], [1, 5]],
			"answer": [[[1, 7], [1, 5]], 0],
			"vertexes": 7,
			"no": 4
		},
		{
			"input": [[2, 3], [9, 10], [5, 11], [5, 10], [1, 10], [3, 11], [5, 6], [6, 11], [3, 8], [5, 7], [4, 9],
					  [6, 8], [6, 10], [2, 6], [2, 4], [10, 11], [3, 4], [1, 8]],
			"answer": [
				[[2, 3], [9, 10], [5, 11], [5, 10], [1, 10], [3, 11], [5, 6], [6, 11], [3, 8], [5, 7], [4, 9], [6, 8],
				 [6, 10], [2, 6], [2, 4], [10, 11], [3, 4], [1, 8]], 10],
			"vertexes": 11,
			"no": 9
		},
		{
			"input": [[3, 5], [1, 3], [3, 4], [4, 6], [1, 6], [3, 6], [4, 5], [2, 3], [1, 2], [3, 7], [4, 7], [5, 7],
					  [2, 4], [2, 7], [1, 7]],
			"answer": [
				[[3, 5], [1, 3], [3, 4], [4, 6], [1, 6], [3, 6], [4, 5], [2, 3], [1, 2], [3, 7], [4, 7], [5, 7], [2, 4],
				 [2, 7], [1, 7]], 7],
			"vertexes": 7,
			"no": 10
		},
		{
			"input": [[1, 2], [1, 6], [5, 6], [2, 5]],
			"answer": [[[1, 2], [1, 6], [5, 6], [2, 5]], 4],
			"vertexes": 6,
			"no": 13
		},
		{
			"input": [[6, 8], [3, 8], [3, 4], [3, 5], [2, 8], [3, 9], [2, 7], [4, 7], [5, 8], [5, 10], [7, 9], [2, 6],
					  [5, 6], [7, 8], [6, 7], [1, 3], [9, 10], [1, 10], [3, 6], [4, 10], [6, 9], [2, 3], [3, 10],
					  [1, 5], [1, 7], [4, 5], [2, 4], [8, 9], [2, 9], [4, 8], [2, 10], [2, 5], [8, 10], [1, 6]],
			"answer": [[[6, 8], [3, 8], [3, 4], [3, 5], [2, 8], [3, 9], [2, 7], [4, 7], [5, 8], [5, 10], [7, 9], [2, 6],
						[5, 6], [7, 8], [6, 7], [1, 3], [9, 10], [1, 10], [3, 6], [4, 10], [6, 9], [2, 3], [3, 10],
						[1, 5], [1, 7], [4, 5], [2, 4], [8, 9], [2, 9], [4, 8], [2, 10], [2, 5], [8, 10], [1, 6]], 10],
			"vertexes": 10,
			"no": 15
		},
		{
			"input": [[2, 7], [2, 5], [2, 3], [1, 7], [3, 7], [5, 7]],
			"answer": [[[2, 7], [2, 5], [2, 3], [1, 7], [3, 7], [5, 7]], 4],
			"vertexes": 7,
			"no": 17
		},
		{
			"input": [[2, 5], [2, 3], [1, 4], [4, 7], [5, 7], [6, 7], [1, 6]],
			"answer": [[[2, 5], [2, 3], [1, 4], [4, 7], [5, 7], [6, 7], [1, 6]], 4],
			"vertexes": 7,
			"no": 18
		},
		{
			"input": [[3, 6], [3, 5], [5, 7], [1, 3], [2, 5], [2, 3], [4, 6], [6, 8], [2, 8], [1, 4], [5, 6], [4, 5],
					  [1, 7], [2, 4], [3, 4], [1, 5], [5, 8], [7, 8], [1, 2], [6, 7], [4, 7], [3, 8], [1, 6]],
			"answer": [
				[[3, 6], [3, 5], [5, 7], [1, 3], [2, 5], [2, 3], [4, 6], [6, 8], [2, 8], [1, 4], [5, 6], [4, 5], [1, 7],
				 [2, 4], [3, 4], [1, 5], [5, 8], [7, 8], [1, 2], [6, 7], [4, 7], [3, 8], [1, 6]], 8],
			"vertexes": 8,
			"no": 100
		},
		{
			"input": [[2, 4], [1, 3], [1, 4], [1, 2]],
			"answer": [[[2, 4], [1, 3], [1, 4], [1, 2]], 3],
			"vertexes": 4,
			"no": 101
		},
		{
			"input": [[2, 5], [4, 5], [3, 4], [1, 3], [2, 4], [2, 3], [3, 5]],
			"answer": [[[2, 5], [4, 5], [3, 4], [1, 3], [2, 4], [2, 3], [3, 5]], 4],
			"vertexes": 5,
			"no": 102
		},
		{
			"input": [[2, 7], [4, 9], [3, 6], [2, 4], [3, 8], [1, 5], [2, 3], [4, 7], [1, 8], [6, 8]],
			"answer": [[[2, 7], [4, 9], [3, 6], [2, 4], [3, 8], [1, 5], [2, 3], [4, 7], [1, 8], [6, 8]], 3],
			"vertexes": 9,
			"no": 103
		},
		{
			"input": [[7, 12], [2, 7], [7, 10], [9, 12], [2, 4], [4, 11], [6, 12], [8, 11], [2, 6], [3, 9], [5, 11],
					  [7, 9], [4, 9], [3, 11], [1, 2], [3, 8], [3, 5], [4, 8], [2, 3], [8, 10], [5, 8], [4, 7], [2, 5],
					  [3, 4], [5, 10], [6, 8], [3, 6], [5, 6], [5, 9], [10, 11]],
			"answer": [
				[[7, 12], [2, 7], [7, 10], [9, 12], [2, 4], [4, 11], [6, 12], [8, 11], [2, 6], [3, 9], [5, 11], [7, 9],
				 [4, 9], [3, 11], [1, 2], [3, 8], [3, 5], [4, 8], [2, 3], [8, 10], [5, 8], [4, 7], [2, 5], [3, 4],
				 [5, 10], [6, 8], [3, 6], [5, 6], [5, 9], [10, 11]], 11],
			"vertexes": 12,
			"no": 104
		},
		{
			"input": [[6, 9], [3, 10], [5, 8], [4, 9], [3, 11], [8, 10], [3, 6], [1, 2], [5, 11], [2, 9], [5, 10],
					  [1, 5], [2, 5], [3, 4], [9, 11], [1, 6], [8, 11], [10, 11], [1, 8], [6, 10], [6, 8], [7, 10],
					  [2, 3], [1, 7], [4, 8]],
			"answer": [
				[[6, 9], [3, 10], [5, 8], [4, 9], [3, 11], [8, 10], [3, 6], [1, 2], [5, 11], [2, 9], [5, 10], [1, 5],
				 [2, 5], [3, 4], [9, 11], [1, 6], [8, 11], [10, 11], [1, 8], [6, 10], [6, 8], [7, 10], [2, 3], [1, 7],
				 [4, 8]], 11],
			"vertexes": 11,
			"no": 105
		},
		{
			"input": [[1, 3], [1, 4], [3, 11], [2, 4], [9, 12], [5, 8], [4, 12], [7, 12], [5, 12], [6, 8], [4, 6],
					  [5, 9], [10, 11], [1, 2], [3, 8], [2, 11], [1, 9], [7, 11], [7, 8], [5, 7], [5, 6], [3, 4],
					  [6, 11], [2, 5]],
			"answer": [
				[[1, 3], [1, 4], [3, 11], [2, 4], [9, 12], [5, 8], [4, 12], [7, 12], [5, 12], [6, 8], [4, 6], [5, 9],
				 [10, 11], [1, 2], [3, 8], [2, 11], [1, 9], [7, 11], [7, 8], [5, 7], [5, 6], [3, 4], [6, 11], [2, 5]],
				11],
			"vertexes": 12,
			"no": 106
		},
		{
			"input": [[5, 9], [7, 8], [6, 9], [6, 11], [5, 8], [5, 11], [3, 8], [5, 6], [5, 10], [2, 4], [3, 10],
					  [5, 7], [1, 5], [3, 11], [4, 6], [7, 10], [4, 5], [1, 3], [9, 11], [3, 7]],
			"answer": [
				[[5, 9], [7, 8], [6, 9], [6, 11], [5, 8], [5, 11], [3, 8], [5, 6], [5, 10], [2, 4], [3, 10], [5, 7],
				 [1, 5], [3, 11], [4, 6], [7, 10], [4, 5], [1, 3], [9, 11], [3, 7]], 9],
			"vertexes": 11,
			"no": 107
		},
		{
			"input": [[4, 8], [1, 6], [1, 5], [1, 3], [1, 11], [5, 6], [4, 10], [6, 11], [4, 7], [5, 12], [9, 11],
					  [8, 9], [3, 9], [2, 3]],
			"answer": [
				[[4, 8], [1, 6], [1, 5], [1, 3], [1, 11], [5, 6], [4, 10], [6, 11], [4, 7], [5, 12], [9, 11], [8, 9],
				 [3, 9], [2, 3]], 6],
			"vertexes": 12,
			"no": 108
		},
	]
}

if __name__ == '__main__':
	def checker(function, connections, best_size):
		user_result = function(connections)
		print(user_result)
		if not isinstance(user_result, (tuple, list)) or not all(isinstance(n, int) for n in user_result):
			print("You should return a list/tuple of integers.")
			return False
		if not best_size and user_result:
			print("Where did you find a cycle here?")
			return False
		if not best_size and not user_result:
			return True
		if len(user_result) < best_size + 1:
			print("You can find a better loop.")
			return False
		if user_result[0] != user_result[-1]:
			print("A cycle starts and ends in the same node.")
			return False
		if len(set(user_result)) != len(user_result) - 1:
			print("Repeat! Yellow card!")
			return False
		for n1, n2 in zip(user_result[:-1], user_result[1:]):
			if (n1, n2) not in connections and (n2, n1) not in connections:
				print("{}-{} is not exist".format(n1, n2))
				return False
		return True, "Ok"
	for k in TESTS:
		for v in TESTS[k]:
			assert checker(find_cycle, tuple(map(tuple,v['input'])), v['answer'][1])