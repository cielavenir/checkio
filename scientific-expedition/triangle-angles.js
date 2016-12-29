"use strict";

var angle=function(a,b,c){return Math.round( 180*Math.acos((a*a+b*b-c*c)/2.0/a/b)/Math.PI );}
var solve=function(x){return x[0]+x[1]<=x[2] ? [0,0,0] : [0,1,2].map(function(i){return angle(x[(i+0)%3],x[(i+1)%3],x[(i+2)%3]);}).sort(function(a,b){return a<b?-1:a>b?1:0;});}
var triangleAngles=function(a,b,c){return solve([a,b,c]);}

var assert = require('assert');

if (!global.is_checking) {
	assert.equal(triangleAngles(4, 4, 4), [60, 60, 60], "All sides are equal");
	assert.equal(triangleAngles(3, 4, 5), [37, 53, 90], "Egyptian triangle");
	assert.equal(triangleAngles(2, 2, 5), [0, 0, 0], "It's can not be a triangle");
	console.log("Coding complete? Click 'Check' to review your tests and earn cool rewards!");
}