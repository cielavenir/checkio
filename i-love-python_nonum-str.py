def i_love_python():
	szero=len(str(len([])))
	#szero=int(True)
	sone=szero<<szero
	stwo=szero<<(szero+szero)
	sthree=szero<<(szero+szero+szero)
	sfour=szero<<(szero+szero+szero+szero)
	sfive=szero<<(szero+szero+szero+szero+szero)
	ssix=szero<<(szero+szero+szero+szero+szero+szero)
	s=chr(ssix|sthree|szero)
	s+=chr(sfive)
	s+=chr(ssix|sfive|sthree|stwo)
	s+=chr(ssix|sfive|sthree|stwo|sone|szero)
	s+=chr(ssix|sfive|sfour|stwo|sone)
	s+=chr(ssix|sfive|stwo|szero)
	s+=chr(sfive)
	s+=chr(ssix|sfour)
	s+=chr(ssix|sfive|sfour|sthree|szero)
	s+=chr(ssix|sfive|sfour|stwo)
	s+=chr(ssix|sfive|sthree)
	s+=chr(ssix|sfive|sthree|stwo|sone|szero)
	s+=chr(ssix|sfive|sthree|stwo|sone)
	s+=chr(sfive|szero)
	return s

if __name__=='__main__':
	print(i_love_python())