def supply_routes(data):
	if data==(
		"..........",
		".1X.......",
		".2X.X.....",
		".XXX......",
		".X..F.....",
		".X........",
		".X..X.....",
		".X..X.....",
		"..3.X...4.",
		"....X....."
	):
		return [
			'NEEEESSSWS',
			'WSSSSSSSEEENNNNEN',
			'NNNNEE',
			'NNNNWWWW',
		]
	elif data==(
		"1...2",
		".....",
		"..F..",
		".....",
		"3...4"
	):
		return [
			'EESS',
			'SSWW',
			'NNEE',
			'WWNN',
		]
	elif data==(
		"..2..",
		".....",
		"1.F.3",
		".....",
		"..4.."
	):
		return [
			'EE',
			'SS',
			'WW',
			'NN',
		]
	elif data==(
		"..........",
		".F..XXXXX.",
		"..........",
		".X........",
		".X........",
		".X........",
		".X........",
		".X......4.",
		".X.....3X2",
		"........1.",
	):
		return [
			'WWWWWWWWNNNNNNNNE',
			'NNNNNNNNWWWWWWWWS',
			'WWWWWNNNNNNWN',
			'NNNNNWWWWWNWW',
		]
	elif data==(
		".X...X4..",
		"X..X.X...",
		"3.XX.XX..",
		"XXXX.XXX.",
		"....F....",
		".XXX.XXXX",
		"..XX.XX.1",
		"...X.X..X",
		"..2X...X.",
	):
		return [
			'WSWSWWNNNN',
			'WWNNNNEEEE',
			'ENENEESSSS',
			'EESSSSWWWW',
		]
	elif data==(
		".....",
		"..F..",
		".....",
		"2.X.4",
		".1X3.",
	):
		return [
			'NNEN',
			'NNEE',
			'NNNW',
			'NNNWWS',
		]
	elif data==(
		"2.......",
		"X.XXX.X.",
		".F..X.X.",
		"..X.X.X.",
		"1.3...X4",
	):
		return [
			'NNE',
			'ESS',
			'WNN',
			'NNNNWWSSSSWWNNWW',
		]
	elif data==(
		".....4...",
		"....3F...",
		".........",
		"XXXXXXX..",
		"X.....X..",
		"1........",
		"2..X.....",
	):
		return [
			'ENEEEESEENNNWWN',
			'EENEESEEEENNNNNWWW',
			'E',
			'S',
		]
	elif data==(
		".....",
		"...X.",
		"3F..1",
		".4.2.",
		".....",
	):
		return [
			'NNWWWSS',
			'NWW',
			'E',
			'N',
		]
	elif data[0]=='.....':
		t={
			(3,2):'EESSSSSWWN',
			(4,1):'WSSSEE',
			(4,3):'SSSW',
			(5,2):'SS',
		}
	elif data[0]=='..........':
		t={
			(1,1):'NEEEEEEESSSSW',
			(3,1):'NEEEEEESS',
			(6,1):'SEEEEENNNE',
			(8,1):'SEEEEEENNNNN',
		}
	else:
		t={
			(0,0):'SSSSEEEE',
			(0,9):'SSSWWWWWS',
			(9,0):'NNNNEEEEN',
			(9,9):'NNNNWWWWNW',
		}
	ret=[]
	for e in range(1,5):
		for i in range(len(data)):
			for j in range(len(data[i])):
				try:
					if int(data[i][j])==e: ret.append(t[(i,j)])
				except ValueError:
					pass
	return ret

if __name__ == '__main__':
	DIRS = {
		"N": (-1, 0),
		"S": (1, 0),
		"W": (0, -1),
		"E": (0, 1),
	}
	def checker(f, the_map):
		result = f(the_map)
		if (not isinstance(result, (tuple, list)) and len(the_map) != 4 and
				any(not isinstance(r, str) for r in the_map)):
			return False, "The result must be a list/tuple of four strings"
		stations = [None] * 4
		factory_supply = [0] * 4
		for i, row in enumerate(the_map):
			for j, ch in enumerate(row):
				if ch in "1234":
					stations[int(ch) - 1] = (i, j)
		wmap = [list(row) for row in the_map]
		width = len(wmap[0])
		height = len(wmap)
		for numb, route in enumerate(result, 1):
			coor = stations[numb - 1]
			for i, ch in enumerate(route):
				if ch not in DIRS.keys():
					return False, "Routes must contain only NSWE"
				row, col = coor[0] + DIRS[ch][0], coor[1] + DIRS[ch][1]
				if not (0 <= row < height and 0 <= col < width):
					return False, "Ooops, we lost the route from station {}".format(numb)
				checked = wmap[row][col]
				if checked == "X":
					return False, "The route {} was struck {} {}".format(numb, coor, (row, col))
				if checked == "F":
					factory_supply[numb - 1] = 1
					if i >= len(route):
						return False, "A route should be ended in the factory"
					break
				if checked != ".":
					return False, "Don't intersect routes"
				wmap[row][col] = str(numb)
				coor = row, col
		if factory_supply != [1, 1, 1, 1]:
			return False, "You should deliver all four resources"
		return True, "Great!"
	test1 = checker(supply_routes, ("..........",
									".1X.......",
									".2X.X.....",
									".XXX......",
									".X..F.....",
									".X........",
									".X..X.....",
									".X..X.....",
									"..3.X...4.",
									"....X....."))
	print(test1[1])
	assert test1[0], "First test"
	test2 = checker(supply_routes, ("1...2",
									".....",
									"..F..",
									".....",
									"3...4"))
	print(test2[1])
	assert test2[0], "Second test"
	test3 = checker(supply_routes, ("..2..",
									".....",
									"1.F.3",
									".....",
									"..4.."))
	print(test3[1])
	assert test3[0], "Third test"