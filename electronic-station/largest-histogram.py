def largest_histogram(m):
	st=[[0,0] for _ in range(len(m))]
	m.append(0)
	r=0
	ptr=0
	j=0
	for j in range(len(m)):
		left=j
		while ptr and st[ptr-1][0]>m[j]:
			ptr-=1
			h=st[ptr][0]
			l=st[ptr][1]
			if r<h*(j-l): r=h*(j-l)
			left=l
		st[ptr]=[m[j],left]
		ptr+=1
	m.pop()
	return r

if __name__ == "__main__":
	assert largest_histogram([5]) == 5, "one is always the biggest"
	assert largest_histogram([5, 3]) == 6, "two are smallest X 2"
	assert largest_histogram([1, 1, 4, 1]) == 4, "vertical"
	assert largest_histogram([1, 1, 3, 1]) == 4, "horizontal"
	assert largest_histogram([2, 1, 4, 5, 1, 3, 3]) == 8, "complex"
	print("Done! Go check it!")
