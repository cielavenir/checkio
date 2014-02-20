#coding:utf-8
from struct import pack
import sys
month=['','Jan','Feb','Mar','Apr','May','Jun','Jul','Aug','Sep','Oct','Nov','Dec']

def checkio(_data):
	data=[int(_data[i*2:i*2+2],16) for i in range(len(_data)//2)]
	type=data[0]
	length=data[8]
	tz='+'
	if data[7]&0x08:
		tz='-'
		data[7]&=0xf7
	time=[(e&0xf)*10+(e>>4) for e in data[1:8]]
	if time[0]>=70: time[0]-=100
	if time[6]==0: tz='+'
	time='%02d %s %04d %02d:%02d:%02d GMT %s%d'%(time[2],month[time[1]],2000+time[0],time[3],time[4],time[5],tz,time[6]//4)
	data=data[9:]
	if type&12==0:
		x=[]
		b=0
		n=0
		for e in data:
			n=e<<b|n
			b+=8
			while b>7:
				x.append(n&127)
				n>>=7
				b-=7
		if n!=0: x.append(n)
		data=x
		type|=4
	if type&12==8:
		data=[(data[i*2]<<8)|data[i*2+1] for i in range(len(data)//2)]
	message=pack('H'*length,*data).decode('utf-16')
	return [time,length,message]

#These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
	assert (checkio('002080629173148007EDF27C1E3E9701') ==
			['26 Aug 2002 19:37:41 GMT +2', 7, u'message']), "First Test"
	assert (checkio('00317050201171820FD3323BDC0ED341C4303DEC3E8700') ==
			['05 Jul 2013 02:11:17 GMT +7', 15, u'Selamat Datang!']), "Second Test, 7 bit"
	assert (checkio('000130925161956915C8729E054A82C26D50DA0D7296EFA0EC5BBE06') ==
			['29 Mar 2010 15:16:59 GMT -4', 21, u'Hey, I am in New York']), "Third Test, negative timezone"
	assert (checkio('08071010101010611F04180441043A043B044E04470435043D043804350020043F043E04340442043204350440043604340430043504420020043F0440043004320438043B043E') ==
			['01 Jan 1970 01:01:01 GMT +4', 31,
			 u'Исключение подтверждает правило']), "Fourth Test, simulate 32-bit signed integer real life problem"
	assert (checkio('088310913041804C23805E4E0D82E5805E4E4B002C805E4E4B4E0D82E5898B4E4B002C898B4E4B4E0D82E577E54E4B002C77E54E4B4E0D82E5884C4E4B002C5B7881F365BC884C4E4B800C6B6277E3 ') ==
			['19 Jan 2038 03:14:08 GMT -11', 35, u'聞不若聞之,聞之不若見之,見之不若知之,知之不若行之,學至於行之而止矣']), "But, we pass Y2K38 problem"