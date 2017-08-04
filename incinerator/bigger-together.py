from functools import cmp_to_key
if 'maketrans' in str.__dict__: cmp=lambda a,b:(a>b)-(a<b)

def bigger_together(data):
	d1=sorted(map(str,data),key=cmp_to_key(lambda a,b:cmp(b+a,a+b)))
	d2=sorted(map(str,data),key=cmp_to_key(lambda a,b:cmp(a+b,b+a)))
	return int(''.join(d1))-int(''.join(d2))
