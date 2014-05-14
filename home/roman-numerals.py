checkio=lambda data: ['','M','MM','MMM'][data//1000]+['','C','CC','CCC','CD','D','DC','DCC','DCCC','CM'][data//100%10]+['','X','XX','XXX','XL','L','LX','LXX','LXXX','XC'][data//10%10]+['','I','II','III','IV','V','VI','VII','VIII','IX'][data%10]

if __name__ == '__main__':
	assert checkio(6) == 'VI', '6'
	assert checkio(76) == 'LXXVI', '76'
	assert checkio(499) == 'CDXCIX', '499'
	assert checkio(3888) == 'MMMDCCCLXXXVIII', '3888'