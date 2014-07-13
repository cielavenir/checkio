def swapsort(_a):
	r=[]
	a=list(_a)
	for i in range(len(_a)-1):
		for j in range(len(_a)-1-i):
			if a[j]>a[j+1]:
				a[j],a[j+1]=a[j+1],a[j]
				r.append(str(j)+str(j+1))
	#print(','.join(r))
	return ','.join(r)

if __name__ == '__main__':
	assert swapsort((6, 4, 2)) == "01,12,01", "Reverse simple"
	assert swapsort((1, 2, 3, 4, 5)) == "", "All right!"
	assert swapsort((1, 2, 3, 5, 3)) == "34", "One move"