import math
z=0
def checkio(data):
	global z
	if z==0:
		z+=1
		return [0,0]
	elif z==1:
		z+=1
		return [1,7]
	elif z==2:
		z+=1
		return [7,9]
	coors=[e[-1] for e in data]
	a=[[int(round(math.hypot(0-i%10,0-i//10))),int(round(math.hypot(1-i%10,7-i//10))),int(round(math.hypot(7-i%10,9-i//10)))] for i in range(100)]
	for i,e in enumerate(a):
		if e==coors:
			return [i%10,i//10]

'''
10.times{|x0|
	10.times{|y0|
		10.times{|x|
			10.times{|y|
				if 10.times.flat_map{|i|10.times.map{|j|
					[Math.hypot(0-i,0-j).round,Math.hypot(x0-i,y0-j).round,Math.hypot(x-i,y-j).round]
				}}.uniq.size==100 then
					p [x0,y0,x,y]
				end
			}
		}
	}
}
=begin
[1, 7, 7, 9] # Let's use this
[2, 9, 7, 5]
[2, 9, 7, 6]
[5, 7, 9, 2]
[6, 7, 9, 2]
[7, 1, 9, 7]
[7, 5, 2, 9]
[7, 6, 2, 9]
[7, 9, 1, 7]
[9, 2, 5, 7]
[9, 2, 6, 7]
[9, 7, 7, 1]
=end
'''