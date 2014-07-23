def safe_pawns(pawns):
	safe=set()
	for e in pawns:
		safe.add(chr(ord(e[0])-1)+chr(ord(e[1])+1))
		safe.add(chr(ord(e[0])+1)+chr(ord(e[1])+1))
	return len(safe.intersection(pawns))

if __name__=='__main__':
	assert safe_pawns({"b4", "d4", "f4", "c3", "e3", "g5", "d2"}) == 6
	assert safe_pawns({"b4", "c4", "d4", "e4", "f4", "g4", "e5"}) == 1