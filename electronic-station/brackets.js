"use strict";

var brackets=function(x){
	var m={'(':')','{':'}','[':']'};
	var s=[];
	for(var e of x){
		if('({['.indexOf(e)>=0)s.push(m[e]);
		if(')}]'.indexOf(e)>=0 && (!s.length||s.pop()!=e))return false;
	}
    return !s.length;
};

var assert = require('assert');

if (!global.is_checking) {
	assert.equal(brackets("((5+3)*2+1)"), true, "Simple");
	assert.equal(brackets("{[(3+1)+2]+}"), true, "Different types");
	assert.equal(brackets("(3+{1-1)}"), false, ") is alone inside {}");
	assert.equal(brackets("[1+1]+(2*2)-{3/3}"), true, "Different operators");
	assert.equal(brackets("(({[(((1)-2)+3)-3]/3}-3)"), false, "One is redundant");
	assert.equal(brackets("2+3"), true, "No brackets, no problem");
	console.log("Coding complete? Click 'Check' to review your tests and earn cool rewards!");
}