#import collections
def iterable(obj):
	#return isinstance(args,collections.Iterable)
	try:
		iter(obj)
		return True
	except TypeError:
		return False

def min2(cur,ite,key):
	try:
		nxt=next(ite)
		return min2(nxt if key(nxt)<key(cur) else cur,ite,key=key)
	except StopIteration:
		return cur
def min(*args,**kwargs):
	try:
		key=kwargs['key']
	except KeyError:
		key=lambda x:x
	ite=iter(args[0]) if len(args)==1 and iterable(args[0]) else iter(args)
	return min2(next(ite),ite,key=key)
def max2(cur,ite,key):
	try:
		nxt=next(ite)
		return max2(nxt if key(nxt)>key(cur) else cur,ite,key=key)
	except StopIteration:
		return cur
def max(*args,**kwargs):
	try:
		key=kwargs['key']
	except KeyError:
		key=lambda x:x
	ite=iter(args[0]) if len(args)==1 and iterable(args[0]) else iter(args)
	return max2(next(ite),ite,key=key)

if __name__ == '__main__':
    assert max(3, 2) == 3, "Simple case max"
    assert min(3, 2) == 2, "Simple case min"
    assert max([1, 2, 0, 3, 4]) == 4, "From a list"
    assert min("hello") == "e", "From string"
    assert max(2.2, 5.6, 5.9, key=int) == 5.6, "Two maximal items"
    assert min([[1, 2], [3, 4], [9, 0]], key=lambda x: x[1]) == [9, 0], "lambda key"