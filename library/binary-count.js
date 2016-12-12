"use strict";

function binaryCount(number){
	return number?number%2+binaryCount(number/2^0):0;
/*
	var r=0;
	for(;number;number=number/2^0)r+=number%2;
	return r;
*/
}

var assert = require('assert');

if (!global.is_checking) {
	assert.equal(binaryCount(4), 1);
	assert.equal(binaryCount(15), 4);
	assert.equal(binaryCount(1), 1);
	assert.equal(binaryCount(1022), 9);
	console.log("Coding complete? Click 'Check' to review your tests and earn cool rewards!");
}
