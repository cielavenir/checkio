"use strict";

var clockAngle=function(s){
	var a=s.split(':').map(Number);
	var h=(30*a[0]+a[1]/2)%360;
	var m=a[1]*6;
    return Math.min(360-Math.abs(h-m),Math.abs(h-m));
};

var assert = require('assert');

if (!global.is_checking) {
	assert.equal(clockAngle("02:30"), 105, "02:30");
	assert.equal(clockAngle("13:42"), 159, "13:42");
	assert.equal(clockAngle("01:42"), 159, "01:42");
	assert.equal(clockAngle("01:43"), 153.5, "01:43");
	assert.equal(clockAngle("00:00"), 0, "Zero");
	assert.equal(clockAngle("12:01"), 5.5, "Little later");
	assert.equal(clockAngle("18:00"), 180, "Opposite");
	console.log("Coding complete? Click 'Check' to review your tests and earn cool rewards!");
}
