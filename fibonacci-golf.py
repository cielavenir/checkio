def fib(start,l,n):
 a,b,c=start
 i=3
 while True:
  a,b,c=b,c,a*l[0]+b*l[1]+c*l[2]
  if i==n: return c
  i+=1

def fibgolf(s,n):
 a,b={
  'fibonacci':[[0,1,1],[0,1,1]],
  'tribonacci':[[0,1,1],[1,1,1]],
  'lucas':[[2,1,3],[0,1,1]],
  'jacobsthal':[[0,1,1],[0,2,1]],
  'pell':[[0,1,2],[0,1,2]],
  'perrin':[[3,0,2],[1,1,0]],
  'padovan':[[0,1,1],[1,1,0]]
 }[s]
 return fib(a,b,n)