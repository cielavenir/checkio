def checkio(data):
	a=[sum(f<<(8*i) for i,f in enumerate(reversed(list(map(int,e.split('.')))))) for e in data]
	for i in range(33):
		x=a[0]>>i
		if all(x==(e>>i) for e in a):
			x=x<<i
			b=[]
			for _ in range(4):
				b.append(x&255)
				x>>=8
			return '.'.join(map(str,reversed(b)))+'/'+str(32-i)

if __name__ == '__main__':
	assert (checkio(["172.16.12.0", "172.16.13.0", "172.16.14.0", "172.16.15.0"]) == "172.16.12.0/22"), "First Test"