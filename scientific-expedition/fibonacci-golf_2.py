def fibgolf(X,N):
 a,b,c,l,m,n=[
  [0,1,1, 0,1,1],
  [0,1,1, 1,1,1],
  [2,1,3, 0,1,1],
  [0,1,1, 0,2,1],
  [0,1,2, 0,1,2],
  [3,0,2, 1,1,0],
  [0,1,1, 1,1,0]
 ]['ibriucacelerad'.find(X[1:3])//2]
 i=2
 while i<N:
  a,b,c=b,c,a*l+b*m+c*n
  i+=1
 return c