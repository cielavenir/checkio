between=lambda a,x,b: (a)<=(x) and (x)<=(b)
x=[
	[0,3,2,3,2,3,4,5],
	[3,4,1,2,3,4,3,4],
	[2,1,4,3,2,3,4,5],
	[3,2,3,2,3,4,3,4],
	[2,3,2,3,4,3,4,5],
	[3,4,3,4,3,4,5,4],
	[4,3,4,3,4,5,4,5],
	[5,4,5,4,5,4,5,6]
]
def checkio(move):
	a=ord(move[0])-ord('a')
	b=ord(move[3])-ord('a')
	c=ord(move[1])-ord('1')
	d=ord(move[4])-ord('1')
	i=b-a
	j=d-c
	r=x[abs(i)][abs(j)];
	if abs(i)==1 and abs(j)==1:
		if (between(0,a+i*2,7) and between(0,c-j,7))or(between(0,c+j*2,7) and between(0,a-i,7)): r=2
	return r

if __name__ == "__main__":
	assert checkio("b1-d5") == 2, "1st example"
	assert checkio("a6-b8") == 1, "2nd example"
	assert checkio("h1-g2") == 4, "3rd example"
	assert checkio("h8-d7") == 3, "4th example"
	assert checkio("a1-h8") == 6, "5th example"

#pbpaste|zlibrawstdio -c9|zbase85rfc
#import zlib,base64;exec(zlib.decompress(base64.b85decode('c-n1|(Q3mW6o#+$DZHz$3Q3x6kj*CvUL2zt32g$d+kE_~b686+4*GxJkBDk}{jqkFXSiqs1i0sVAQafUq@EGj452;-&9IjvMq|TIyvx(`XT<}HyEc<BiFJYW_q~+rULn<ah2&mEaxd=6yeO=&u`~JD&ojO3-<Ay+f!v)*X>1e|F&yB)Fw#YwDlrw&{);vWQ$$~hMQQ;Ut<s1IBPaa``jak9rFCWMEp%q`2c>M&yCxM=xMZ|6{{?M09G9n#zp~UTcoJ)XY<KjA9oI)y5KF8M#K{gLXRlvwBkmV1u75!')))