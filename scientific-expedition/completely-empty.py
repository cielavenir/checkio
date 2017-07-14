import collections
def completely_empty(data):
	if not isinstance(data,collections.Iterable): return False
	if isinstance(data,str) and data: return False
	return all(completely_empty(e) for e in data)
