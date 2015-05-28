golf=lambda r:sum((ord(e[0])-65)*9+int(e[1])for e in __import__('re').findall(r'[A-Z][1-9]',r))

if __name__ == '__main__':
	golf("ASDA1,BB22D01C1") == 31
	golf("B1,C2,D3") == 60