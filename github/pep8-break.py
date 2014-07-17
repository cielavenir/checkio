import re ;O='01234,!({[<@;:#>]})?.56789' ;twist=lambda l :re.sub ( '[a-zA-Z]+',
lambda x:x.group(0).swapcase()[::-1],re.sub(' +',' ',l)).translate(str.maketrans
(O,O[::-1]));1;1;1;1;1;1;1;1;1;1;1;1;1;1;1;1;1;1;1;1;1;1;1;1;1;1;1;1;1;1;1;1;1;#
1;1;1;1;1;1;1;1;1;1;1;1;1;1;1;1;1;1;1;1;1;1;1;1;1;1;1;1;1;1;1;1;1;1;1;1;1;1;1;1;
1;1;1;1;1;1;1;1;1;1;1;1;1;1;1;1;1;1;1;1;1;1;1;1;1;1;1;1;1;1;1;1;1;1;1;1;1;1;1;1;
1;1;1;1;1;1;1;1;1;1;1;1;1;1;1;1;1;1;1;1;1;1;1;1;1;1;1;1;1;1;1;1;1;1;1;1;1;1;1;1;
1;1;1;1;1;1;1;1;1;1;1;1;1;1;1;1;1;1;1;1;1;1;1;1;1;1;1;1;1;1;1;1;1;1;1;1;1;1;1;1;
1;1;1;1;1;1;1;1;1;1;1;1;1;1;1;1;1;1;1;1;1;1;1;1;1;1;1;1;1;1;1;1;1;1;1;1;1;1;1;1;
1;1;1;1;1;1;1;1;1;1;1;1;1;1;1;1;1;1;1;1;1;1;1;1;1;1;1;1;1;1;1;1;1;1;1;1;1;1;1;1;
1;1;1;1;1;1;1;1;1;1;1;1;1;1;1;1;1;1;1;1;1;1;1;1;1;1;1;1;1;1;1;1;1;1;1;1;1;1;1;1;
1;1;1;1;1;1;1;1;1;1;1;1;1;1;1;1;1;1;1;1;1;1;1;1;1;1;1;1;1;1;1;1;1;1;1;1;1;1;1;1;
1;1;1;1;1;1;1;1;1;1;1;1;1;1;1;1;1;1;1;1;1;1;1;1;1;1;1;1;1;1;1;1;1;1;1;1;1;1;1;1;

'''
1;1;1;1;1;1;1;1;1;1;1;1;1;1;1;1;1;1;1;1;1;1;1;1;1;1;1;1;1;1;1;1;1;1;1;1;1;1;1;1;
1;1;1;1;1;1;1;1;1;1;1;1;1;1;1;1;1;1;1;1;1;1;1;1;1;1;1;1;1;1;1;1;1;1;1;1;1;1;1;1;
O='01234,!({[<@;:#>]})?.56789';1;1;1;1;1;1;1;1;1;1;1;1;1;1;1;1;1;1;1;1;1;1;1;1;#
twist=lambda l :' '.join ( map ( a,( '*'+l+'*' ).split ( ) ) ) [ 1:-1 ];1;1;1;1;
def a ( b,i=0,z=[ 1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1 ] ) :#
 while[ 1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1 ]and i<len ( b ) :
  if[ 1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1 ]and b [ i ].isalpha ( ) :
   z=i;1;1;1;1;1;1;1;1;1;1;1;1;1;1;1;1;1;1;1;1;1;1;1;1;1;1;1;1;1;1;1;1;1;1;1;1;#
   while i<len ( b )and b [ i ].isalpha ( ) :i+=1;1;1;1;1;1;1;1;1;1;1;1;1;1;1;1;
   b=b [ :z ] +b [ z:i ] [ ::-1 ] +b [ i: ] ;1;1;1;1;1;1;1;1;1;1;1;1;1;1;1;1;1;#
  i+=1;1;1;1;1;1;1;1;1;1;1;1;1;1;1;1;1;1;1;1;1;1;1;1;1;1;1;1;1;1;1;1;1;1;1;1;1;#
 return b.swapcase ( ).translate ( str.maketrans ( O,O [ ::-1 ] ) );1;1;1;1;1;1;
'''

if __name__ == '__main__':
 #Basics
 assert twist("Hello World!") == "OLLEh DLROw?"
 assert twist("I'm 1st") == "i'M 8TS"
 assert twist("How are you? 905th.") == "WOh ERA UOY! 094HT,"
 assert twist("The code - ([{<;#>}])") == "EHt EDOC - )]}>:@<{[("
 assert twist("EMAIL        a@b.ru") == "liame A#B,UR"
 assert twist(";-) 0_0 @__@") == ":-( 9_9 #__#"
 #Edge
 assert twist("") == ""
 assert twist("0123456789") == "9876543210"
 assert twist("How are you? 905th.") == "WOh ERA UOY! 094HT,"
 assert twist("A1bc2") == "a8CB7"
 #(omitted)
 assert twist("!#$%&()*+,-./:;<=>?@[\]^_`{|}~") == "?@$%&)(*+.-,/;:>=<!#]\[^_`}|{~"
 #Extra
 assert twist("pep8 requirements!?!") == "PEP1 STNEMERIUQER?!?"
 #(omitted)
 assert twist("9+5*2-1=18") == "0+4*7-8=81"
 assert twist("PEP8? I don`t know anything about this.") == "pep1! i NOD`T WONK GNIHTYNA TUOBA SIHT,"
 lines=[]
 for line in open(__file__,'r'):
   if not line.rstrip(): break
   if len(line.rstrip())>80: raise Exception('Line too long (max 80)')
   lines.append(line)
 lines[-1]=lines[-1].rstrip()
 if len(lines)>12: raise Exception('Program too long (max 12 lines)')
 print('Assertion successful.')
 try:
  import pep8
 except ImportError: exit()
 if len(__import__('sys').argv)>1:
  pep8.Checker(lines=lines).check_all()
 else:
  error=0
  warning=0
  checker=pep8.Checker(lines=lines,quiet=True)
  checker.check_all()
  for k,v in checker.report.counters.items():
   if len(k)==4 and k[1].isdigit() and k[2].isdigit() and k[3].isdigit():
    if k[0]=='E': error+=v
    if k[0]=='W': warning+=v
  print('Error=%d'%error)
  print('Warning=%d'%warning)
  print('Score=%d'%(error*2+warning))