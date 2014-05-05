def cow_say(str):
	line=''
	length=-1
	lines=[]
	a=str.split()
	if str[0]==' ': a=['']+a
	if str[-1]==' ': a.append('')
	for e in a:
		if length+1+len(e)>39:
			lines.append(line)
			line=''
			length=-1
		line+=' '+e
		length+=1+len(e)
	lines.append(line)
	length=max(len(e) for e in lines)
	ret="\n"+' '+'_'*(length+1)+"\n"
	for i,e in enumerate(lines):
		ret+=('<' if len(lines)==1 else '/' if i==0 else '\\' if i==len(lines)-1 else '|')+('%-*s'%(length,e)+' ')+('>' if len(lines)==1 else '\\' if i==0 else '/' if i==len(lines)-1 else '|')+"\n"
	ret+=' '+'-'*(length+1)+"\n"
	return ret+r'''        \   ^__^
         \  (oo)\_______
            (__)\       )\/\
                ||----w |
                ||     ||
'''

if __name__ == '__main__':
	expected_cowsay_one_line = r'''
 ________________
< Checkio rulezz >
 ----------------
        \   ^__^
         \  (oo)\_______
            (__)\       )\/\
                ||----w |
                ||     ||
'''
	expected_cowsay_two_lines = r'''
 ________________________________________
/ A                                      \
\ longtextwithonlyonespacetofittwolines. /
 ----------------------------------------
        \   ^__^
         \  (oo)\_______
            (__)\       )\/\
                ||----w |
                ||     ||
'''
	expected_cowsay_many_lines = r'''
 _________________________________________
/ Lorem ipsum dolor sit amet, consectetur \
| adipisicing elit, sed do eiusmod tempor |
| incididunt ut labore et dolore magna    |
\ aliqua.                                 /
 -----------------------------------------
        \   ^__^
         \  (oo)\_______
            (__)\       )\/\
                ||----w |
                ||     ||
'''
	cowsay_one_line = cow_say('Checkio rulezz')
	assert cowsay_one_line == expected_cowsay_one_line, 'Wrong answer:\n%s' % cowsay_one_line
	cowsay_two_lines = cow_say('A longtextwithonlyonespacetofittwolines.')
	assert cowsay_two_lines == expected_cowsay_two_lines, 'Wrong answer:\n%s' % cowsay_two_lines
	cowsay_many_lines = cow_say('Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do '
		'eiusmod tempor incididunt ut labore et dolore magna aliqua.')
	assert cowsay_many_lines == expected_cowsay_many_lines, 'Wrong answer:\n%s' % cowsay_many_lines