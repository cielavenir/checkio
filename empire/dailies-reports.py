import datetime
convert=lambda a:[datetime.datetime.strptime(a[0],'%Y-%m-%d'),sum((ord(e[0])-65)*9+int(e[1]) for e in a[1].split(','))]
solve=lambda report,start,end:sum(e[1] for e in report if start<=e[0] and e[0]<=end)
count_reports=lambda full_report, from_date, to_date:solve([convert(e.split()) for e in full_report.split("\n")] ,datetime.datetime.strptime(from_date,'%Y-%m-%d'),datetime.datetime.strptime(to_date,'%Y-%m-%d'))

if __name__ == '__main__':
	assert count_reports("2015-01-01 A1,B2\n"
						 "2015-01-05 C3,C2,C1\n"
						 "2015-02-01 B4\n"
						 "2015-01-03 Z9,Z9",
						 "2015-01-01", "2015-01-31") == 540, "Normal"
	assert count_reports("2000-02-02 Z2,Z1\n"
						 "2000-02-01 Z2,Z1\n"
						 "2000-02-03 Z2,Z1",
						 "2000-02-04", "2000-02-28") == 0, "Zero"
	assert count_reports("2999-12-31 Z9,A1", "2000-01-01", "2999-12-31") == 235, "Millenium"