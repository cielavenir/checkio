#!/usr/bin/ruby
#build dictionary for checkio 40coins
#http://members3.jcom.home.ne.jp/ta-higu/math/tenbin-to-coin.html

L=5
_dict=1.step(3**L-1).to_a.select{|e|
	x=e.to_s(3).tr('0','')
	x[0,1]=='1'
}.map{|e|
	x=e.to_s(3)
	'0'*(L-x.size)+x
}
dict=[_dict,_dict.map{|e|e.tr('12','21')}].transpose
#Now, choose each element of dict, to match the number of 1 and 2 of each digits are the same.
p dict
loop{
	a=dict.sample(100).map(&:sample)
	if a.map{|e|e.chars.to_a}.transpose.all?{|e|e.count('1')==e.count('2')}
		p a.sort
		exit
	end
}
__END__
OK, we use this as dictionary!
["00010", "00012", "00022", "00100", "00110", "00111", "00112", "00122", "00201", "00210", "00212", "01101", "01110", "01111", "01112", "01201", "01202", "01212", "01221", "01222", "02000", "02002", "02012", "02020", "02022", "02100", "02110", "02120", "02122", "02210", "10000", "10001", "10011", "10012", "10020", "10022", "10100", "10121", "10122", "10200", "10201", "10202", "10211", "10220", "10221", "11012", "11020", "11101", "11111", "11112", "11201", "11202", "11212", "11220", "11221", "12001", "12011", "12020", "12022", "12101", "12102", "12120", "12122", "12202", "12211", "20001", "20111", "20120", "20121", "20201", "20202", "20210", "20220", "20221", "20222", "21001", "21012", "21020", "21021", "21100", "21102", "21110", "21112", "21120", "21121", "21200", "21212", "21221", "22000", "22001", "22011", "22012", "22020", "22100", "22111", "22122", "22200", "22210", "22211", "22220"]