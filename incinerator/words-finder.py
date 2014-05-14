import bisect
def checkio(text, words):
	se=[]
	lower=text.lower()
	for e in words.lower().split():
		l_orig=-1
		while True:
			try:
				l_orig=l_orig+1+lower[l_orig+1:].index(e)
			except ValueError:
				break
			l=l_orig
			r=l+len(e)-1
			#perform "range problem (painting wall)"
			right_idx=bisect.bisect_left(se,(l,0)) #l <= se[right_idx][0]
			if right_idx!=0:
				left_idx=right_idx-1
				if l<=se[left_idx][1]: # overlap with left
					l=se[left_idx][0]
					r=max(r,se[left_idx][1])
					se.pop(left_idx)
					right_idx-=1
			while right_idx<len(se) and se[right_idx][0]<=r: # overlap with right
				r=max(r,se[right_idx][1])
				se.pop(right_idx)
			se.insert(right_idx,(l,r))
	for e in reversed(se):
		text=text[:e[0]]+'<span>'+text[e[0]:e[1]+1]+'</span>'+text[e[1]+1:]
	return text

if __name__ == '__main__':
	assert (checkio("This is only a text example for task example.", "example") ==
			"This is only a text <span>example</span> for task <span>example</span>."), "Simple test"
	assert (checkio("Python is a widely used high-level programming language.", "pyThoN") ==
			"<span>Python</span> is a widely used high-level programming language."), "Ignore letters cases, but keep original"
	assert (checkio("It is experiment for control groups with similar distributions.", "is im") ==
			"It <span>is</span> exper<span>im</span>ent for control groups with s<span>im</span>ilar d<span>is</span>tributions."), "Several subwords"
	assert (checkio("The National Aeronautics and Space Administration (NASA).", "nasa  THE") ==
			"<span>The</span> National Aeronautics and Space Administration (<span>NASA</span>)."), "two spaces"
	assert (checkio("Did you find anything?", "word space tree") ==
			"Did you find anything?"), "No comments"
	assert (checkio("Hello World! Or LOL", "hell world or lo") ==
			"<span>Hello</span> <span>World</span>! <span>Or</span> <span>LO</span>L"), "Contain or intersect"