#checkio=lambda data: len(data)>=10 and any(e.isdigit() for e in data) and any(e.islower() for e in data) and any(e.isupper() for e in data)

checkio=lambda d:len(d)>9 and all(any(getattr(e,'is'+z)()for e in d)for z in['digit','lower','upper'])

if __name__ == '__main__':
	assert checkio('A1213pokl') == False, "1st example"
	assert checkio('bAse730onE4') == True, "2nd example"
	assert checkio('asasasasasasasaas') == False, "3rd example"
	assert checkio('QWERTYqwerty') == False, "4th example"
	assert checkio('123456123456') == False, "5th example"
	assert checkio('QwErTy911poqqqq') == True, "6th example"