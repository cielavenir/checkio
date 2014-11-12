class Friends:
	def __init__(self, connections):
		self.conn={frozenset(e) for e in connections}
	def add(self, connection):
		if connection in self.conn: return False
		self.conn.add(frozenset(connection))
		return True
	def remove(self, connection):
		if connection not in self.conn: return False
		self.conn.remove(connection)
		return True
	def names(self):
		r=set()
		for e in self.conn:
			for f in e: r.add(f)
		return r
	def connected(self, name):
		r=set()
		for e in self.conn:
			r.update({f for f in e if f!=name and name in e})
		return r

if __name__ == '__main__':
	letter_friends = Friends(({"a", "b"}, {"b", "c"}, {"c", "a"}, {"a", "c"}))
	digit_friends = Friends([{"1", "2"}, {"3", "1"}])
	assert letter_friends.add({"c", "d"}) is True, "Add"
	assert letter_friends.add({"c", "d"}) is False, "Add again"
	assert letter_friends.remove({"c", "d"}) is True, "Remove"
	assert digit_friends.remove({"c", "d"}) is False, "Remove non exists"
	assert letter_friends.names() == {"a", "b", "c"}, "Names"
	assert letter_friends.connected("d") == set(), "Non connected name"
	assert letter_friends.connected("a") == {"b", "c"}, "Connected name"