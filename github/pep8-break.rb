#!/usr/bin/ruby
PYTHON='python3.3'
PEP8='pep8'
SCRIPT=File.dirname(File.expand_path(__FILE__))+'/pep8-break.py'

if !system(%Q("#{PYTHON}" "#{SCRIPT}"))
	exit
end
str=IO.readlines(SCRIPT).take_while{|e|!e.chomp.empty?}.map(&:chomp)*"\n"
error=0
warning=0
IO.popen(%Q("#{PEP8}" -),'r+b'){|io|
	io.print str
	io.close_write
	while io.gets
		error+=1 if $_=~/ E\d{3} /
		warning+=1 if $_=~/ W\d{3} /
	end
}
puts 'Error='+error.to_s
puts 'Warning='+warning.to_s
puts 'Score='+(error*2+warning).to_s