def decode_vigenere(*args):
	x,y,z=[[ord(e)-65 for e in a] for a in args]
	key=[(e[1]-e[0])%26 for e in zip(x,y)]
	if len(key)<len(z):
		l=1
		while l<len(key)//2:
			i=0
			while i<l:
				if key[i]!=key[i+l]: break
				i+=1
			if i==l: break
			l+=1
		else:
			raise Exception("cannot understand key")
	else:
		l=len(key)
	return ''.join(chr(65+(e-key[i%l])%26) for i,e in enumerate(z))

if __name__=='__main__':
	assert checkio('DONTWORRYBEHAPPY', 'FVRVGWFTFFGRIDRF', 'DLLCZXMFVRVGWFTF') == "BEHAPPYDONTWORRY"
	assert checkio('ANODSASGOODASAWINKTOABLINDBATEH', 'MBBWQMGTHMPOFTUUBXMMMPYBLPPNMCT',
                      'TSFGMFHUXKQGFBYTVRLYHSERLMITARKPBR') == "HESNOTTHEMESSIAHHESAVERYNAUGHTYBOY"