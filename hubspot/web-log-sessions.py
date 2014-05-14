from datetime import datetime,timedelta
def checkio(log_text):
	log={}
	for e0 in log_text.split():
		a=e0.split(';;')
		time=datetime(*[int(e) for e in a[0].split('-')])
		user=a[1].lower()
		domain=a[2].split('/')[2]
		domain='.'.join(domain.split('.')[-2:])
		if (user,domain) not in log: log[(user,domain)]=[]
		log[(user,domain)].append(time)
	result=[]
	for k,v in log.items():
		t=v[0]
		idx=0
		for i in range(1,len(v)):
			if v[i]-v[i-1]>timedelta(seconds=1800):
				result.append((k[0],k[1],(v[i-1]-t).seconds+1,i-idx))
				t=v[i]
				idx=i
		result.append((k[0],k[1],(v[-1]-t).seconds+1,len(v)-idx))
	return '\n'.join(';;'.join(str(f) for f in e) for e in sorted(result))

if __name__ == '__main__':
	assert (checkio(
"""2013-01-01-01-00-00;;Name;;http://checkio.org/task
2013-01-01-01-02-00;;name;;http://checkio.org/task2
2013-01-01-01-31-00;;Name;;https://admin.checkio.org
2013-01-01-03-00-00;;Name;;http://www.checkio.org/profile
2013-01-01-03-00-01;;Name;;http://example.com
2013-02-03-04-00-00;;user2;;http://checkio.org/task
2013-01-01-03-11-00;;Name;;http://checkio.org/task""")
==
"""name;;checkio.org;;661;;2
name;;checkio.org;;1861;;3
name;;example.com;;1;;1
user2;;checkio.org;;1;;1"""), "Example"