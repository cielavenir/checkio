def checkio(data):
	t=[int(e) for e in data[0].split(':')]
	start=3600*t[0]+60*t[1]+t[2]
	t=[int(e) for e in data[1].split(':')]
	end=3600*t[0]+60*t[1]+t[2]
	diff=end-start
	d=data[2].split()
	d1=float(d[0])
	if d[1][0]=='m':
		d1*=60
	elif d[1][0]=='h':
		d1*=3600
	d2=float(d[3])
	if d[4][0]=='m':
		d2*=60
	elif d[4][0]=='h':
		d2*=3600
	end=int(start+diff*d2/(d1+d2))
	return '%02d:%02d:%02d'%(end//3600,end//60%60,end%60)

#These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == "__main__":
	assert checkio(['00:00:00', '00:00:15', '+5 seconds at 10 seconds']) == '00:00:10', 'First example'
	assert checkio(['06:10:00', '06:10:15', '-5 seconds at 10 seconds']) == '06:10:30', 'Second example'
	assert checkio(['13:00:00', '14:01:00', '+1 second at 1 minute']) == '14:00:00', 'Third example'
	assert checkio(['01:05:05', '04:05:05', '-1 hour at 2 hours']) == '07:05:05', 'Fourth example'
	assert checkio(['00:00:00', '00:00:30', '+2 seconds at 6 seconds']) == '00:00:22', 'Fifth example'