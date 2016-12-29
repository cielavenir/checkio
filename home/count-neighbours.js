"use strict";

var countNeighbours=function(a,y,x){
	var r=0;
	for(var dx=-1;dx<2;dx++)for(var dy=-1;dy<2;dy++){
		if(dx|dy && 0<=x+dx&&x+dx<a[0].length && 0<=y+dy&&y+dy<a.length && a[y+dy][x+dx])r++;
	}
	return r;
}

var assert = require('assert');

if (!global.is_checking) {
	assert.equal(countNeighbours([[1, 0, 0, 1, 0],
								  [0, 1, 0, 0, 0],
								  [0, 0, 1, 0, 1],
								  [1, 0, 0, 0, 0],
								  [0, 0, 1, 0, 0]], 1, 2), 3, "1st example");

	assert.equal(countNeighbours([[1, 0, 0, 1, 0],
								  [0, 1, 0, 0, 0],
								  [0, 0, 1, 0, 1],
								  [1, 0, 0, 0, 0],
								  [0, 0, 1, 0, 0]], 0, 0), 1, "2nd example");

	assert.equal(countNeighbours([[1, 1, 1],
								  [1, 1, 1],
								  [1, 1, 1]], 0, 2), 3, "Dense corner");

	assert.equal(countNeighbours([[0, 0, 0],
								  [0, 1, 0],
								  [0, 0, 0]], 1, 1), 0, "Single");

	console.log("Coding complete? Click 'Check' to review your tests and earn cool rewards!");
}