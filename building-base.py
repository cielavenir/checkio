class Building():
	def __init__(self, south, west, width_we, width_ns, height=10):
		self.south=south
		self.west=west
		self.width_we=width_we
		self.width_ns=width_ns
		self.height=height
	def corners(self):
		return {
			'south-west':[self.south,self.west],
			'north-west':[self.south+self.width_ns,self.west],
			'south-east':[self.south,self.west+self.width_we],
			'north-east':[self.south+self.width_ns,self.west+self.width_we],
		}
	def area(self):
		return self.width_we*self.width_ns
	def volume(self):
		return self.width_we*self.width_ns*self.height
	def __repr__(self):
		return 'Building at [{}, {}]. Size {} by {}. Height {}.'.format(self.south,self.west,self.width_we,self.width_ns,self.height)

if __name__ == '__main__':
	def json_dict(d):
		return dict((k, list(v)) for k, v in d.items())
	b = Building(1, 2, 2, 3)
	b2 = Building(1, 2, 2, 3, 5)
	assert json_dict(b.corners()) == {'north-east': [4, 4], 'south-east': [1, 4],
									  'south-west': [1, 2], 'north-west': [4, 2]}, "Corners"
	assert b.area() == 6, "Area"
	assert b.volume() == 60, "Volume"
	assert b2.volume() == 30, "Volume2"
	assert str(b) == "Building at [1, 2]. Size 2 by 3. Height 10.", "String"