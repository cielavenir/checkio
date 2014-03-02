#coding:utf-8
from struct import pack

table='''
	H																He
Li	Be											B	C	N	O	F	Ne
Na	Mg											Al	Si	P	S	Cl	Ar
K	Ca	Sc	Ti	V	Cr	Mn	Fe	Co	Ni	Cu	Zn	Ga	Ge	As	Se	Br	Kr
Rb	Sr	Y	Zr	Nb	Mo	Tc	Ru	Rh	Pd	Ag	Cd	In	Sn	Sb	Te	I	Xe
Cs	Ba	La	Ce	Pr	Nd	Pm	Sm	Eu	Gd	Tb	Dy	Ho	Er	Tm	Yb	Lu
Hf	Ta	W	Re	Os	Ir	Pt	Au	Hg	Tl	Pb	Bi	Po	At	Rn
Fr	Ra	Ac	Th	Pa	U	Np	Pu	Am	Cm	Bk	Cf	Es	Fm	Md	No	Lr
Rf	Db	Sg	Bh	Hs	Mt	Ds	Rg	Cn	Uut	Fl	Uup	Lv	Uus	Uuo
'''.split()

orbital=('s','p','d','f','g','h','i')

def superscript(n):
	return ''.join(pack('H',(0x2070,0xb9,0xb2,0xb3,0x2074,0x2075,0x2076,0x2077,0x2078,0x2079)[int(e)]).decode('utf-16') for e in str(n))

def checkio(element):
	#unusual elements
	if element=='Cr': return ["24",u"[Ar] 3d⁵ 4s¹","2 2 222 2 222 1 11111"]
	if element=='Cu': return ["29","[Ar] 3d¹⁰ 4s¹","2 2 222 2 222 1 22222"]
	for i,e in enumerate(table):
		if e==element:
			_n=n=i+1
			break
	result_notation=[]
	result_diagram=[]
	_outer=0
	while n>0:
		outer=_outer//2+1
		for inner in range(outer,0,-1):
			dec=min(inner*4-2,n)
			n-=dec
			result_notation.append((_outer+2-inner,inner-1,dec))
			diagram=[0]*((inner*4-2)//2)
			for j in range(2):
				for i in range(len(diagram)):
					diagram[i]+=1
					dec-=1
					if dec==0: break
				if dec==0: break
			result_diagram.append(''.join(str(e) for e in diagram))
			if n==0: break
		_outer+=1
	noble_gas=''
	if len(result_notation)>19 and result_notation[18]==(7,1,6):
		noble_gas='[Uuo] '
		result_notation=result_notation[19:]
	if len(result_notation)>15 and result_notation[14]==(6,1,6):
		noble_gas='[Rn] '
		result_notation=result_notation[15:]
	if len(result_notation)>11 and result_notation[10]==(5,1,6):
		noble_gas='[Xe] '
		result_notation=result_notation[11:]
	if len(result_notation)>8 and result_notation[7]==(4,1,6):
		noble_gas='[Kr] '
		result_notation=result_notation[8:]
	if len(result_notation)>5 and result_notation[4]==(3,1,6):
		noble_gas='[Ar] '
		result_notation=result_notation[5:]
	if len(result_notation)>3 and result_notation[2]==(2,1,6):
		noble_gas='[Ne] '
		result_notation=result_notation[3:]
	if len(result_notation)>1 and result_notation[0]==(1,0,2):
		noble_gas='[He] '
		result_notation=result_notation[1:]
	result_notation.sort()
	result_notation=[str(a)+orbital[b]+superscript(c) for a,b,c in result_notation]
	notation=' '.join(result_notation)
	return [str(_n), noble_gas+notation, ' '.join(result_diagram)]

if __name__ == '__main__':
	#These "asserts" using only for self-checking and not necessary for auto-testing
	assert (checkio('H') == ["1", u"1s¹", "1"]), "First Test - 1s¹"
	assert (checkio('He') == ["2", u"1s²", "2"]), "Second Test - 1s²"
	assert (checkio('Al') == ["13", u"[Ne] 3s² 3p¹", "2 2 222 2 100"]), "Third Test - 1s² 2s² 2p⁶ 3s² 3p¹"
	assert (checkio('O') == ["8", u"[He] 2s² 2p⁴", "2 2 211"]), "Fourth Test - 1s² 2s² 2p⁴"
	assert (checkio('Li') == ["3", u"[He] 2s¹", "2 1"]), "Fifth Test - 1s² 2s¹"
	print('All done!')