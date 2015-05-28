count_ingots=lambda report:sum((ord(e[0])-65)*9+int(e[1]) for e in report.split(','))

if __name__ == '__main__':
	assert count_ingots("A2,B1") == 12, "One and eleven"
	assert count_ingots("A1,A1,A1") == 3, "One, two, three"
	assert count_ingots("Z9,X8,Y7") == 672, "XYZ"
	assert count_ingots("C1,D1,B1,E1,F1") == 140, "Daily normal"