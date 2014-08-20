def fibgolf(X,N):
 a,b,c,l,m,n={
  'fibonacci': [0,1,1, 0,1,1],
  'tribonacci':[0,1,1, 1,1,1],
  'lucas':     [2,1,3, 0,1,1],
  'jacobsthal':[0,1,1, 0,2,1],
  'pell':      [0,1,2, 0,1,2],
  'perrin':    [3,0,2, 1,1,0],
  'padovan':   [0,1,1, 1,1,0]
 }[X]
 i=2
 while i<N:
  a,b,c=b,c,a*l+b*m+c*n
  i+=1
 return c