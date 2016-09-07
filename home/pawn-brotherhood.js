"use strict";

function safePawns(data){
	var safe={}
	for(var e of data){
		safe[String.fromCharCode(e.charCodeAt(0)-1)+String.fromCharCode(e.charCodeAt(1)+1)]=1;
		safe[String.fromCharCode(e.charCodeAt(0)+1)+String.fromCharCode(e.charCodeAt(1)+1)]=1;
	}
	var r=0;
	for(var e of data)if(safe[e])r++;
	return r;
}

var assert = require('assert');

if (!global.is_checking) {
	assert.equal(safePawns(["b4", "d4", "f4", "c3", "e3", "g5", "d2"]), 6, "First");
	assert.equal(safePawns(["b4", "c4", "d4", "e4", "f4", "g4", "e5"]), 1, "Second");
	console.log("Coding complete? Click 'Check' to review your tests and earn cool rewards!");
}