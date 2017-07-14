def reverse_roman(roman):
    m={'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000}
	r=0
	for i in range(len(roman)):
		r+=m[roman[i]]*(1 if i==len(roman)-1 or m[roman[i]]>=m[roman[i+1]] else -1)
	return r
