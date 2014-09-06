from functools import reduce
import datetime,operator
days_diff=lambda *a:abs(reduce(operator.sub,map(datetime.date,*zip(*a))).days)

if __name__ == '__main__':
	days_diff((1982, 4, 19), (1982, 4, 22)) == 3
	days_diff((2014, 1, 1), (2014, 8, 27)) == 238
	days_diff((2014, 8, 27), (2014, 1, 1)) == 238