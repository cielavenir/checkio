'''
def golf(s,l):
 a=[]
 i=0
 while i+l<=len(s):
  x=s[i:i+l]
  a+=[(sum(sum(m<n for m in x[j+1:])for j,n in enumerate(x)),i,x)]
  i+=l
 return''.join(e[2]for e in sorted(a))
'''

'''
f=lambda i,s,l:[]if len(s)<l else[(sum(sum(m<n for m in s[j+1:l])for j,n in enumerate(s[:l])),i,s[:l])]+f(i+1,s[l:],l)
golf=lambda s,l:''.join(e[2]for e in sorted(f(0,s,l)))
'''

golf=lambda s,l:''.join(sorted([s[i*l:i*l+l]for i in range(len(s)//l)],key=lambda x:sum(sum(m<n for m in x[j+1:])for j,n in enumerate(x))))

print(golf('ACGGCATAACCCTCGA',3))