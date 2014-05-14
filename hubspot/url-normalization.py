from struct import pack
import re

def perform_escape(seq):
	s=seq[1:]
	n=int(seq[1:],16)
	if 0x2d==n or 0x2e==n or 0x30<=n<=0x39 or 0x41<=n<=0x5a or 0x5f==n or 0x61<=n<=0x7a or 0x7e==n:
		return pack('H',n).decode('utf-16').lower()
	else:
		return seq.upper()

def checkio(url):
	url=re.sub(r'(%[0-9a-fA-F]{2})',lambda match: perform_escape(match.group(1)),url.lower())
	url=re.sub(r':80/','/',url)
	url=re.sub(r':80$','',url)
	url=re.sub(r'/([^/]+)/\.\.','',url)
	url=re.sub('\./','',url)
	return url

if __name__ == '__main__':
	assert checkio("Http://Www.Checkio.org") == \
		"http://www.checkio.org", "1st rule"
	assert checkio("http://www.checkio.org/%cc%b1bac") == \
		"http://www.checkio.org/%CC%B1bac", "2nd rule"
	assert checkio("http://www.checkio.org/task%5F%31") == \
		"http://www.checkio.org/task_1", "3rd rule"
	assert checkio("http://www.checkio.org:80/home/") == \
		"http://www.checkio.org/home/", "4th rule"
	assert checkio("http://www.checkio.org:8080/home/") == \
		"http://www.checkio.org:8080/home/", "4th rule again"
	assert checkio("http://www.checkio.org/task/./1/../2/././name") == \
		"http://www.checkio.org/task/2/name", "5th rule"
	print('First set of tests done')