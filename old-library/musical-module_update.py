from functools import reduce
from fractions import gcd
#gcd=lambda a,b: a if b==0 else gcd(b,a%b)
greatest_common_divisor=lambda *args:reduce(gcd,args)
#old library musical-module compatibility
checkio=lambda args:greatest_common_divisor(*args)
	
if __name__ == '__main__':
	assert greatest_common_divisor(6, 4) == 2, "Simple"
	assert greatest_common_divisor(2, 4, 8) == 2, "Three arguments"
	assert greatest_common_divisor(2, 3, 5, 7, 11) == 1, "Prime numbers"
	assert greatest_common_divisor(3, 9, 3, 9) == 3, "Repeating arguments"