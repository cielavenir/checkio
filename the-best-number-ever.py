class BF:
	buffer=[0]*9999
	ptr=0
	def execute(self,s):
		ret=''
		i=0
		while i<len(s):
			if s[i]=='>': self.ptr+=1
			elif s[i]=='<': self.ptr-=1
			elif s[i]=='+': self.buffer[self.ptr]+=1
			elif s[i]=='-': self.buffer[self.ptr]-=1
			elif s[i]=='.': ret+=chr(self.buffer[self.ptr])
			elif s[i]==',': pass #getchar
			elif s[i]=='[':
				if self.buffer[self.ptr]: ret+=self.execute(s[i+1:])
				marker=1
				while marker:
					if s[i+1]=='[': marker+=1
					if s[i+1]==']': marker-=1
					i+=1
			elif s[i]==']':
				if self.buffer[self.ptr]: i=-1
				else: return ret
			i+=1
		return ret

checkio=lambda:int(BF().execute(
	'The answer to the ultimate question of life, the universe, and everything is "++++++++[>>>>>>>++++++<<<<<<<-]>>>>>>>++++.--."'
))

print(checkio())