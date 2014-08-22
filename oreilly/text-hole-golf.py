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
 l=len(a)
 r=0
 for i in range(l*99):
  try: r+=all((x//3*(x%3)==1)^(a[i%l+x%3][i//l+x//3]!=' ')for x in range(9))
  except:1
 return r

def golf(a):
 r=0
 for i in range(999):
  try:r+=all((x//3*(x%3)==1)^(a[i%30+x%3][i//30+x//3]!=' ')for x in range(9))
  except:1
 return r

#solutions without except

z=lambda a,x,y:a[x:]!=[]and (a[x][y:]+' ')[0]!=' '
golf=lambda a:sum(all((x//3*(x%3)==1)^(z(a,i%30+x%3,i//30+x//3))for x in range(9))for i in range(999))

golf=lambda a:sum(all((x//3*(x%3)==1)^(a[i%30+x%3:]!=[]and (a[i%30+x%3][i//30+x//3:]+' ')[0]!=' ')for x in range(9))for i in range(999))

def golf(a):
 l=len(a)-2
 return sum(all((x//3*(x%3)==1)^((a[i%l+x%3][i//l+x//3:]+' ')[0]!=' ')for x in range(9))for i in range(l*99))


assert golf([
	"How are you doing?",
	"I'm fine. OK.",
	"Lorem Ipsum?",
	"Of course!!!",
	"1234567890",
	"0        0",
	"1234567890",
	"Fine! good buy!"]) == 3