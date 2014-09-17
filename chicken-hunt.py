#this is currently stub

def search(a,c):
	for y in range(len(a)):
		for x in range(len(a[y])):
			if a[y][x]==c:
				return (x,y)
def hunt(a):
	my=search(a,'I')
	companion=search(a,'S')
	chicken=search(a,'C')
