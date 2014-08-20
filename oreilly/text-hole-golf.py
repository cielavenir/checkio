def golf(a):
 r=0
 for i in range(1,len(a)):
  for j in range(1,len(a[i])):
   try:r+=a[i][j]==' 'and all(a[i+y][j+x]!=' 'for x,y in((-1,-1),(-1,0),(-1,1),(0,-1),(0,1),(1,-1),(1,0),(1,1)))
   except IndexError:1
 return r

def golf(a):
 r=0
 for i in range(1,len(a)):
  for j in range(1,len(a[i])):
   try: r+=all((not x and not y)^(a[i+y][j+x]!=' ')for x in range(-1,2)for y in range(-1,2))
   except IndexError:1
 return r

def golf(a):
 r=0
 for i in range(1,len(a)):
  for j in range(1,len(a[i])):
   try: r+=all((x//3*(x%3)==1)^(a[i-1+x%3][j-1+x//3]!=' ')for x in range(9))
   except IndexError:1
 return r

assert golf([
	"How are you doing?",
	"I'm fine. OK.",
	"Lorem Ipsum?",
	"Of course!!!",
	"1234567890",
	"0        0",
	"1234567890",
	"Fine! good buy!"]) == 3