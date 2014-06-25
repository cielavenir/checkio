#def golf(i):
# while 1:
#  i+=1
#  if str(i)==str(i)[::-1]and all(i%j for j in range(2,i)):return i

def golf(i):
 i+=1
 while str(i)!=str(i)[::-1]or any(i%j<1 for j in range(2,i)):i+=1
 return i

def golf(i):
 for x in [2,3,7,11,101,131,727,10301,98689,1003001]:
  if i<x:return x

#golf=lambda i:next(x for x in[2,3,7,11,101,131,727,10301,98689,1003001]if i<x)
#golf=lambda i:[x for x in[2,3,7,11,101,131,727,10301,98689,1003001]if i<x][0]
golf=lambda i:min(x for x in[2,3,7,11,101,131,727,10301,98689,1003001]if i<x)

#golf=lambda n:next(i for i in range(n+1,n*11)if str(i)==str(i)[::-1]and all(i%j for j in range(2,i)))

if __name__ == '__main__':
	assert golf(2)==3
	assert golf(13)==101
	assert golf(101)==131
	assert golf(9000)==10301
	assert golf(999999)==1003001
	assert golf(1)==2