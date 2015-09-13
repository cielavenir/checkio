import re

def solve(m):
	s=m.group(1)
	a=re.split(r'[\.,]',s)
	if len(a)>1 and len(a[-1])==2:
		a[-2]+='.'+a[-1]
		a.pop()
	return ','.join(a)

checkio=lambda s:re.sub(r'(\$[\d\.,]*\d+)',solve,s)

if __name__ == '__main__':
	assert checkio("$1.234.567,89") == "$1,234,567.89" , "1st Example"
	assert checkio("$0,89") == "$0.89" , "2nd Example"
	assert checkio("Euro Style = $12.345,67, US Style = $12,345.67") == \
				   "Euro Style = $12,345.67, US Style = $12,345.67" , "European and US"
	assert checkio("Us Style = $12,345.67, Euro Style = $12.345,67") == \
				   "Us Style = $12,345.67, Euro Style = $12,345.67" , "US and European"
	assert checkio("$1.234, $5.678 and $9") == \
				   "$1,234, $5,678 and $9", "Dollars without cents"