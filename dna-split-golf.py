def golf(s,n):
 a=[];i=0
 while i+n<=len(s):
  z=s[i:i+n]
  x=['ACGT'.index(e)for e in z]
  a.append([sum(sum(m<n for m in x[j+1:])for j,n in enumerate(x)),i,z])
  i+=n
 return''.join(e[2]for e in sorted(a))

print(golf('ACGGCATAACCCTCGA',3))