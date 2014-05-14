from collections import defaultdict
from operator import methodcaller
def total_cost(calls):
	d=defaultdict(int)
	for e in map(methodcaller('split'),calls): d[e[0]]+=(int(e[2])+59)//60
	return sum(e if e<100 else 100+2*(e-100) for e in d.values())

if __name__ == '__main__':
	assert total_cost(("2014-01-01 01:12:13 181",
					   "2014-01-02 20:11:10 600",
					   "2014-01-03 01:12:13 6009",
					   "2014-01-03 12:13:55 200")) == 124, "Base example"
	assert total_cost(("2014-02-05 01:00:00 1",
					   "2014-02-05 02:00:00 1",
					   "2014-02-05 03:00:00 1",
					   "2014-02-05 04:00:00 1")) == 4, "Short calls but money..."
	assert total_cost(("2014-02-05 01:00:00 60",
					   "2014-02-05 02:00:00 60",
					   "2014-02-05 03:00:00 60",
					   "2014-02-05 04:00:00 6000")) == 106, "Precise calls"