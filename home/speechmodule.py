FIRST_TEN = ['', "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
SECOND_TEN = ["ten", "eleven", "twelve", "thirteen", "fourteen", "fifteen", "sixteen", "seventeen", "eighteen", "nineteen"]
OTHER_TENS = ['', '', "twenty", "thirty", "forty", "fifty", "sixty", "seventy", "eighty", "ninety"]
HUNDRED = "hundred"

def checkio(number):
	if number==0: return 'zero'
	ret=''
	if number//100>0:
		ret+=FIRST_TEN[number//100]+' hundred'
		if number%100>0: ret+=' '
	if 10<=number%100 and number%100<=19:
		ret+=SECOND_TEN[number%100-10]
	else:
		if number//10%10>0:
			ret+=OTHER_TENS[number//10%10]
			if number%10>0: ret+=' '
		ret+=FIRST_TEN[number%10]
	return ret

if __name__ == '__main__':
	assert checkio(4) == 'four', "1st example"
	assert checkio(133) == 'one hundred thirty three', "2nd example"
	assert checkio(12) == 'twelve', "3rd example"
	assert checkio(101) == 'one hundred one', "4th example"
	assert checkio(212) == 'two hundred twelve', "5th example"
	assert checkio(40) == 'forty', "6th example"