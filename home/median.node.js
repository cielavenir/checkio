"use strict";

var comp=function(a,b){return a-b;}
var median=function(data){
	data.sort(comp);
	if(data.length%2)return data[data.length/2^0];
	return (data[data.length/2-1]+data[data.length/2])/2;
};

var assert = require('assert');

if(!global.is_checking){
	assert.equal(median([1, 2, 3, 4, 5]), 3, "1st example");
	assert.equal(median([3, 1, 2, 5, 3]), 3, "2nd example");
	assert.equal(median([1, 300, 2, 200, 1]), 2, "3rd example");
	assert.equal(median([3, 6, 20, 99, 10, 15]), 12.5, "4th example");
	console.log("Coding complete? Click 'Check' to review your tests and earn cool rewards!");
}