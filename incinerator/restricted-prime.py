zero=int(False)
one=int(True)
ten=int(str(one)+str(zero))
tent=ten**(one+one+one+one)
t=[zero]*(tent)
t[zero]=t[one]=one
for i,e in enumerate(t):
	if i>one and not t[i]:
		for j,e in enumerate(t):
			if i*(one+one+j)>=tent: break
			t[i*(one+one+j)]=one
checkio=lambda n: t[n]==zero