#davasaan=lambda x:x*0xcccccccd>>35
#davasaan=lambda x:x+(x<<2)+(x<<3)+(x<<6)+(x<<7)+(x<<10)+(x<<11)+(x<<14)+(x<<15)+(x<<18)+(x<<19)+(x<<22)+(x<<23)+(x<<26)+(x<<27)+(x<<30)+(x<<31)>>35
f=lambda x,n:x and f(x>>1,n+n)+[0,n][x%2];davasaan=lambda x:f(x,3435973837)>>35

if __name__ == '__main__':
	assert davasaan(0) == 0, "First"
	assert davasaan(7) == 0, "Second"
	assert davasaan(81) == 8, "Third"
	assert davasaan(199) == 19, "Fourth"
	assert davasaan(4500) == 450, "Fifth"
	assert davasaan(9999) == 999, "Sixth"