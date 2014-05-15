def check_connection(_conn,a,b):
	conn=[e.split('-') for e in _conn]
	n=0
	d={}
	for e in conn:
		for f in e:
			if not f in d:
				d[f]=n
				n+=1
	mat=[[1<<30]*n for i in range(n)]
	for i in range(n): mat[i][i]=0
	for e in conn: mat[d[e[0]]][d[e[1]]]=mat[d[e[1]]][d[e[0]]]=1
	#Warshall-Floyd
	for k in range(n):
		for i in range(n):
			for j in range(n):
				if mat[i][j]>mat[i][k]+mat[k][j]: mat[i][j]=mat[i][k]+mat[k][j]
	return mat[d[a]][d[b]] < 1<<30

if __name__ == '__main__':
	assert check_connection(
    ("dr101-mr99", "mr99-out00", "dr101-out00", "scout1-scout2",
     "scout3-scout1", "scout1-scout4", "scout4-sscout", "sscout-super"),
    "scout2", "scout3") == True
	assert check_connection(
    ("dr101-mr99", "mr99-out00", "dr101-out00", "scout1-scout2",
     "scout3-scout1", "scout1-scout4", "scout4-sscout", "sscout-super"),
    "dr101", "sscout") == False