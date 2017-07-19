def bigger_together(data):
	d1=reversed(sorted(map(str,data)))
	d2=sorted(map(str,data))
	return int(''.join(d1))-int(''.join(d2))
