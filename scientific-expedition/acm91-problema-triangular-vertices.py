import sys
if sys.version_info[0]>=3: raw_input=input

def triangle(row,col):
	if row[0]==row[1]:
		len=col[1]-col[0]
		return len>0 and col[2]==col[1] and row[2]==row[0]+len
	else:
		len=row[1]-row[0]
		return len>0 and col[0]==col[1] and row[2]==row[1] and col[2]==col[1]+len

def parallelogram(row,col):
	if row[0]==row[1]:
		len=col[1]-col[0]
		return len>0 and row[2]==row[3] and col[3]-col[2]==len and row[2]-row[0]==len and (col[2]==col[0] or col[2] == col[1])
	else:
		len=row[1]-row[0]
		return len>0 and col[0]==col[1] and col[2]==col[3] and row[1]==row[2] and row[3]-row[2]==len and col[2]-col[1]==len

def hexagon(row,col):
	len=col[1]-col[0]
	return len>0 and row[0]==row[1] and col[2]==col[0] and row[2]==row[0]+len and col[3]==col[1]+len and row[3]==row[2] and col[4]==col[1] and row[4]==row[2]+len and col[5]==col[3] and row[5]==row[4]

def rowcol(p):
	row=[]
	col=[]
	for e in p:
		head=inc=1
		while e>=head+inc:
			head+=inc
			inc+=1
		row.append(inc)
		col.append(e-head)
	return (row,col)

def checkio(data):
	points=sorted(data)
	row,col=rowcol(points)
	if len(data)==3: return 3 if triangle(row,col) else 0
	if len(data)==4: return 4 if parallelogram(row,col) else 0
	if len(data)==6: return 6 if hexagon(row,col) else 0
	return 0

if __name__ == "__main__":
	m={
		0: ' are not the vertices of an acceptable figure',
		3: ' are the vertices of a triangle',
		4: ' are the vertices of a parallelogram',
		6: ' are the vertices of a hexagon',
	}
	try:
		while True:
			a=[int(e) for e in raw_input().split()]
			print(' '.join(str(e) for e in a)+m[checkio(a)])
	except EOFError:
		pass