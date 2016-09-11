// According to https://github.com/Bryukh-Checkio-Tasks/checkio-task-box-probability/blob/master/verification/tests.py ,
// max(step) is 11. So O(2^n) will work.

"use strict";
var dfs=function(b,w,prob,step){
	if(step==0)return prob*w/(w+b);
	if(b==0)return dfs(1,w-1,prob,step-1);
	if(w==0)return dfs(b-1,1,prob,step-1);
	return dfs(b-1,w+1,prob*b/(w+b),step-1)+dfs(b+1,w-1,prob*w/(w+b),step-1);
};

var boxProbability=function(marbles, step) {
	var b=0;
	var w=0;
	for(var c of marbles){
		if(c=='b')b++;
		if(c=='w')w++;
	}
	return dfs(b,w,1.0,step-1);
};

/*
self-checker is not optimized for float.
var assert = require('assert');

if (!global.is_checking) {
	assert.equal(boxProbability('bbw', 3), 0.48, "First");
	assert.equal(boxProbability('wwb', 3), 0.52, "Second");
	assert.equal(boxProbability('www', 3), 0.56, "Third");
	assert.equal(boxProbability('bbbb', 1), 0, "Fifth");
	assert.equal(boxProbability('wwbb', 4), 0.5, "Sixth");
	assert.equal(boxProbability('bwbwbwb', 5), 0.48, "Seventh");
	console.log("Coding complete? Click 'Check' to review your tests and earn cool rewards!");
}
*/