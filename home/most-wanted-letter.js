"use strict";

function mostWanted(data){
	data=data.toLowerCase();
	var t={};
	for(var e of data){
		if(e!=e.toUpperCase()){
			t[e]=t[e]||0;
			t[e]++;
		}
	}
	var r=0,sr;
	for(var k in t){
		if(t[k]>r || t[k]==r&&sr>k)r=t[k],sr=k;
	}
	return sr;
}

var assert = require('assert');

if (!global.is_checking) {
	assert.equal(mostWanted("Hello World!"), "l", "1st example");
	assert.equal(mostWanted("How do you do?"), "o", "2nd example");
	assert.equal(mostWanted("One"), "e", "3rd example");
	assert.equal(mostWanted("Oops!"), "o", "4th example");
	assert.equal(mostWanted("AAaooo!!!!"), "a", "Letters");
	console.log("Coding complete? Click 'Check' to review your tests and earn cool rewards!");
}