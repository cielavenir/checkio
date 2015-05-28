check_grid=lambda grid:not any('XX' in ''.join(e) or 'ZZ' in ''.join(e) for e in grid) and not any('XX' in ''.join(e) or 'ZZ' in ''.join(e) for e in zip(*grid))

if __name__ == '__main__':
	assert check_grid([["X", "Z"], ["Z", "X"]]), "2x2 Good"
	assert check_grid([["X", "Z", "X"],
					   ["Z", "X", "Z"],
					   ["X", "Z", "X"]]), "3x3 Good"
	assert check_grid([["X", "Z", "X", "Z"],
					   ["Z", "X", "Z", "X"]]), "2x4 Good"
	assert not check_grid([["X", "X"],
						   ["X", "X"]]), "2x2 Bad"
	assert not check_grid([["X", "Z", "X"],
						   ["Z", "Z", "Z"],
						   ["X", "Z", "X"]]), "3x3 Bad"
	assert not check_grid([["X", "Z", "X", "Z"],
						   ["X", "Z", "X", "Z"]]), "2x4 Bad"
