from datetime import date,timedelta

def checkio(from_date, to_date):
	r=0
	while from_date<=to_date:
		if from_date.weekday()>=5: r+=1
		from_date+=timedelta(1)
	return r

if __name__ == '__main__':
	assert checkio(date(2013, 9, 18), date(2013, 9, 23)) == 2, "1st example"
	assert checkio(date(2013, 1, 1), date(2013, 2, 1)) == 8, "2nd example"
	assert checkio(date(2013, 2, 2), date(2013, 2, 3)) == 2, "3rd example"