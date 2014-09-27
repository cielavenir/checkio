from collections import defaultdict
def find_word(_message):
	message=[''.join(f.lower() for f in e if f.isalpha()) for e in _message.split()]
	dic=defaultdict(float)
	cnt=defaultdict(int)
	for i in range(len(message)):
		cnt[message[i]]+=1
		for j in range(i+1,len(message)):
			factor=[]
			if message[i][0]==message[j][0]: factor.append(10)
			if message[i][-1]==message[j][-1]: factor.append(10)
			factor.append( min(len(message[i]),len(message[j]))*30.0 / max(len(message[i]),len(message[j])) )
			x=set(message[i])
			y=set(message[j])
			factor.append( len(x.intersection(y))*50.0 / len(x.union(y)) )
			dic[message[i]]+=sum(factor)
			dic[message[j]]+=sum(factor)
	result=''
	m=0
	for i in reversed(range(len(message))):
		if dic[message[i]]/cnt[message[i]]>m:
			m=dic[message[i]]/cnt[message[i]]
			result=message[i]
	return result

if __name__ == '__main__':
	assert find_word("Speak friend and enter.") == "friend", "Friend"
	assert find_word("Beard and Bread") == "bread", "Bread is Beard"
	assert find_word("The Doors of Durin, Lord of Moria. Speak friend and enter. "
					 "I Narvi made them. Celebrimbor of Hollin drew these signs") == "durin", "Durin"
	assert find_word("Aoccdrnig to a rscheearch at Cmabrigde Uinervtisy."
					 " According to a researcher at Cambridge University.") == "according", "Research"
	assert find_word("One, two, two, three, three, three.") == "three", "Repeating"