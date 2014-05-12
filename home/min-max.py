#import collections
def iterable(obj):
	#return isinstance(args,collections.Iterable)
	#return hasattr(obj,'__iter__') # only Py3
	try:
		iter(obj)
		return True
	except TypeError:
		return False

def minmax2(cur,ite,compare,key):
	try:
		nxt=next(ite)
		return minmax2(nxt if compare(key(nxt),key(cur)) else cur,ite,compare,key)
	except StopIteration:
		return cur
def min(*args,**kwargs):
	ite=iter(args[0]) if len(args)==1 and iterable(args[0]) else iter(args)
	return minmax2(next(ite),ite,lambda x,y: x<y,kwargs.get('key',lambda x:x))
def max(*args,**kwargs):
	ite=iter(args[0]) if len(args)==1 and iterable(args[0]) else iter(args)
	return minmax2(next(ite),ite,lambda x,y: x>y,kwargs.get('key',lambda x:x))

if __name__ == '__main__':
    assert max(3, 2) == 3, "Simple case max"
    assert min(3, 2) == 2, "Simple case min"
    assert max([1, 2, 0, 3, 4]) == 4, "From a list"
    assert min("hello") == "e", "From string"
    assert max(2.2, 5.6, 5.9, key=int) == 5.6, "Two maximal items"
    assert min([[1, 2], [3, 4], [9, 0]], key=lambda x: x[1]) == [9, 0], "lambda key"