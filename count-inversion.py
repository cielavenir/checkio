count_inversion=lambda a:sum(sum(a[i]<a[j] for j in range(i)) for i in range(len(a)))

if __name__=='__main__':
	assert count_inversion((1, 2, 5, 3, 4, 7, 6)) == 3
	assert count_inversion((0, 1, 2, 3)) == 0