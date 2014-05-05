from functools import reduce
flat_list=lambda a:reduce(lambda x,y:x+y,(flat_list(e) for e in a),[]) if isinstance(a,list) else [a]