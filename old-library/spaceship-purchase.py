def checkio(data):
	while True:
		if data[0]+data[1]>=data[2]: return data[2]
		data[0]+=data[1]
		if data[0]>=data[2]-data[3]: return data[0]
		data[2]-=data[3]

#These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
	assert checkio([150, 50, 1000, 100]) == 450, "1st example"
	assert checkio([150, 50, 900, 100]) == 400, "2nd example"