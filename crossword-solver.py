from collections import defaultdict
import random

def dfs(d):
	global data
	if d==len(lst): return data
	i,j,k,z=lst[d]
	a=[data[i+z%2*_k][j+z//2*_k] for _k in range(k)]
	if all(a[_k]!='.' for _k in range(k)):
		_i=0
		while _i<len(words[k]):
			if a==words[k][_i]: break
			_i+=1
		if _i<len(words[k]) and wordflags[k][_i]: return None
		wordflags[k][_i]=True
		if dfs(d+1): return data
		wordflags[k][_i]=False
		return None
	for _i,e in enumerate(words[k]):
		if not wordflags[k][_i] and all(a[_k]=='.' or a[_k]==e[_k] for _k in range(k)):
			wordflags[k][_i]=True
			for _k in range(k):data[i+z%2*_k][j+z//2*_k]=e[_k]
			if dfs(d+1): return data
			for _k in range(k):data[i+z%2*_k][j+z//2*_k]=a[_k]
			wordflags[k][_i]=False

def solver(_data,_words):
	global words,wordflags,data,lst
	#init word list
	words=defaultdict(list)
	wordflags={}
	for e in _words:
		if len(e) not in wordflags: wordflags[len(e)]=defaultdict(bool)
		words[len(e)].append(list(e))
	for e in words: random.shuffle(words[e])
	#detect word area
	data=[list(e) for e in _data]
	flags=[[0]*len(data[i]) for i in range(len(data))]
	for i in range(len(data)):
		for j in range(len(data[i])):
			flags[i][j]=-1 if data[i][j]=='X' else 0
	_lst=[]
	for i in range(len(flags)):
		for j in range(len(flags[i])):
			if flags[i][j]>=0:
				#vertical
				if flags[i][j]&1==0 and i<len(flags)-1 and flags[i+1][j]>=0:
					k=0
					while i+k<len(flags) and flags[i+k][j]>=0:
						flags[i+k][j]|=1
						k+=1
					_lst.append((i,j,k,1))
				#horizontal
				if flags[i][j]&2==0 and j<len(flags[i])-1 and flags[i][j+1]>=0:
					k=0
					while j+k<len(data[i]) and flags[i][j+k]>=0:
						flags[i][j+k]|=2
						k+=1
					_lst.append((i,j,k,2))
	#_lst=sorted(_lst,key=lambda e:-e[2])
	#lst should be sorted by "connectivity"
	lst=[_lst.pop(0)]
	while _lst:
		newlst=[]
		i=len(_lst)-1
		while i>=0:
			if any(
				_lst[i][3]==2 and _i<=_lst[i][0]<_i+k and _lst[i][1]<=j<_lst[i][1]+_lst[i][2]
				if z==1 else
				_lst[i][3]==1 and j<=_lst[i][1]<j+k and _lst[i][0]<=_i<_lst[i][0]+_lst[i][2]
				for _i,j,k,z in lst
			):
				newlst.append(_lst.pop(i))
			i-=1
		lst+=newlst
	for e in lst: print(e)
	return [''.join(e) for e in dfs(0)]

if __name__ == '__main__':
	import string
	ERROR_TYPE = (False, "The result must be a list/tuple of strings")
	ERROR_SIZE = (False, "The result must have the same size as input data")
	ERROR_TEMPLATE = (False, "Your result is not look like the original crossword")
	ERROR_UNFILLED = (False, "I see the empty cell in your result")
	ERROR_TYPE_CELL = (False, "Cells should contains lowercase ascii letters or 'X'")
	F_ERROR_REPEATED = lambda w: (False, "Found repeated words '{}'".format(w))
	F_ERROR_UNKNOWN = lambda w: (False, "The word '{}' is not from the dictionary".format(w))
	WORDS = ['act', 'age', 'air', 'arm', 'art', 'ask', 'bad', 'bag', 'bar', 'bat', 'bed', 'bet', 'bid', 'big', 'bit', 'box', 'boy', 'bug', 'bus', 'buy', 'can', 'cap', 'car', 'cat', 'cow', 'cry', 'cup', 'cut', 'dad', 'day', 'dig', 'dog', 'dot', 'due', 'ear', 'eat', 'egg', 'end', 'eye', 'fan', 'fat', 'fee', 'few', 'fix', 'fly', 'fun', 'gap', 'gas', 'god', 'guy', 'hat', 'hit', 'ice', 'job', 'key', 'kid', 'lab', 'law', 'lay', 'leg', 'let', 'lie', 'lip', 'log', 'low', 'man', 'map', 'mix', 'mom', 'mud', 'net', 'oil', 'one', 'pay', 'pen', 'pie', 'pin', 'pop', 'pot', 'put', 'raw', 'red', 'rip', 'row', 'rub', 'run', 'sad', 'sea', 'set', 'sex', 'she', 'sir', 'sky', 'son', 'sun', 'tap', 'tax', 'tea', 'tie', 'tip', 'toe', 'top', 'try', 'two', 'use', 'war', 'way', 'web', 'win', 'yo', 'area', 'army', 'baby', 'back', 'bake', 'ball', 'band', 'bank', 'base', 'bath', 'bear', 'beat', 'beer', 'bell', 'belt', 'bend', 'bike', 'bill', 'bird', 'bite', 'blow', 'blue', 'boat', 'body', 'bone', 'book', 'boot', 'boss', 'bowl', 'burn', 'cake', 'call', 'calm', 'camp', 'card', 'care', 'case', 'cash', 'cell', 'chip', 'city', 'club', 'clue', 'coat', 'code', 'cold', 'cook', 'copy', 'cost', 'crew', 'dare', 'dark', 'data', 'date', 'dead', 'deal', 'dear', 'debt', 'deep', 'desk', 'diet', 'dirt', 'dish', 'disk', 'door', 'drag', 'draw', 'drop', 'dump', 'dust', 'duty', 'ease', 'east', 'edge', 'exam', 'exit', 'face', 'fact', 'fall', 'farm', 'fear', 'feed', 'feel', 'file', 'fill', 'film', 'fire', 'fish', 'flow', 'fold', 'food', 'foot', 'form', 'fuel', 'gain', 'game', 'gate', 'gear', 'gene', 'gift', 'girl', 'give', 'glad', 'goal', 'gold', 'golf', 'good', 'grab', 'hair', 'half', 'hall', 'hand', 'hang', 'harm', 'hate', 'head', 'heat', 'hell', 'help', 'hide', 'high', 'hire', 'hold', 'hole', 'home', 'hook', 'hope', 'host', 'hour', 'hunt', 'hurt', 'idea', 'iron', 'item', 'join', 'joke', 'jump', 'jury', 'keep', 'kick', 'kill', 'kind', 'king', 'kiss', 'knee', 'lack', 'lady', 'lake', 'land', 'lead', 'life', 'lift', 'line', 'link', 'list', 'load', 'loan', 'lock', 'long', 'look', 'loss', 'love', 'luck', 'mail', 'main', 'make', 'male', 'mall', 'many', 'mark', 'mate', 'math', 'meal', 'meat', 'meet', 'men', 'mess', 'milk', 'mind', 'mine', 'miss', 'mode', 'mood', 'most', 'move', 'nail', 'name', 'neat', 'neck', 'news', 'nose', 'note', 'oven', 'pace', 'pack', 'page', 'pain', 'pair', 'park', 'part', 'pass', 'past', 'path', 'peak', 'pick', 'pipe', 'plan', 'play', 'poem', 'poet', 'pool', 'post', 'pull', 'push', 'quit', 'race', 'rain', 'rate', 'read', 'rent', 'rest', 'rice', 'rich', 'ride', 'ring', 'rise', 'risk', 'road', 'rock', 'role', 'roll', 'roof', 'room', 'rope', 'ruin', 'rule', 'rush', 'safe', 'sail', 'sale', 'salt', 'sand', 'save', 'seat', 'self', 'sell', 'ship', 'shoe', 'shop', 'shot', 'show', 'sick', 'side', 'sign', 'sing', 'sink', 'site', 'size', 'skin', 'slip', 'snow', 'sock', 'soft', 'soil', 'song', 'sort', 'soup', 'spot', 'star', 'stay', 'step', 'stop', 'suck', 'suit', 'swim', 'tale', 'talk', 'tank', 'task', 'team', 'tear', 'tell', 'term', 'test', 'text', 'till', 'time', 'tone', 'tool', 'tour', 'town', 'tree', 'trip', 'tune', 'turn', 'type', 'unit', 'user', 'vast', 'verb', 'verb', 'verb', 'view', 'wait', 'wake', 'walk', 'wall', 'wash', 'wave', 'wear', 'week', 'west', 'wife', 'will', 'wind', 'wine', 'wing', 'wish', 'wood', 'word', 'work', 'wrap', 'yard', 'year', 'zone', 'abuse', 'actor', 'adult', 'agent', 'alarm', 'anger', 'angle', 'apple', 'aside', 'award', 'basis', 'beach', 'being', 'bench', 'birth', 'black', 'blame', 'blank', 'blind', 'block', 'blood', 'board', 'bonus', 'brain', 'brave', 'bread', 'break', 'brick', 'brief', 'broad', 'brown', 'brush', 'buddy', 'bunch', 'buyer', 'cable', 'candy', 'carry', 'catch', 'cause', 'chain', 'chair', 'chart', 'check', 'cheek', 'chest', 'child', 'claim', 'class', 'clerk', 'click', 'clock', 'cloud', 'coach', 'coast', 'count', 'court', 'cover', 'crack', 'craft', 'crash', 'crazy', 'cream', 'cross', 'curve', 'cycle', 'dance', 'death', 'delay', 'depth', 'devil', 'doubt', 'draft', 'drama', 'dream', 'dress', 'drink', 'drive', 'drunk', 'earth', 'entry', 'equal', 'error', 'essay', 'event', 'fault', 'field', 'fight', 'final', 'floor', 'focus', 'force', 'frame', 'front', 'fruit', 'funny', 'glass', 'glove', 'grade', 'grand', 'grass', 'great', 'green', 'group', 'guard', 'guess', 'guest', 'guide', 'habit', 'heart', 'heavy', 'hello', 'honey', 'horse', 'hotel', 'house', 'human', 'hurry', 'ideal', 'image', 'issue', 'joint', 'judge', 'juice', 'knife', 'laugh', 'layer', 'leave', 'level', 'light', 'limit', 'local', 'lunch', 'major', 'march', 'match', 'maybe', 'media', 'metal', 'might', 'minor', 'model', 'money', 'month', 'motor', 'mouse', 'mouth', 'movie', 'music', 'nasty', 'nerve', 'night', 'noise', 'north', 'novel', 'nurse', 'offer', 'order', 'other', 'owner', 'paint', 'panic', 'paper', 'party', 'pause', 'peace', 'phase', 'phone', 'photo', 'piano', 'piece', 'pitch', 'pizza', 'place', 'plane', 'plant', 'plate', 'point', 'pound', 'power', 'press', 'price', 'pride', 'print', 'prior', 'prize', 'proof', 'punch', 'queen', 'quiet', 'quote', 'radio', 'raise', 'range', 'ratio', 'reach', 'reply', 'river', 'rough', 'round', 'royal', 'salad', 'scale', 'scene', 'score', 'screw', 'sense', 'serve', 'shake', 'shame', 'shape', 'share', 'shift', 'shine', 'shirt', 'shock', 'shoot', 'silly', 'skill', 'skirt', 'sleep', 'slice', 'slide', 'smile', 'smoke', 'solid', 'sound', 'south', 'space', 'spare', 'speed', 'spell', 'spend', 'spite', 'split', 'sport', 'spray', 'staff', 'stage', 'stand', 'start', 'state', 'steak', 'steal', 'stick', 'still', 'stock', 'store', 'storm', 'story', 'strip', 'study', 'stuff', 'style', 'sugar', 'sweet', 'swing', 'table', 'taste', 'teach', 'theme', 'thing', 'title', 'today', 'tooth', 'topic', 'total', 'touch', 'tough', 'towel', 'tower', 'track', 'trade', 'train', 'trash', 'treat', 'trick', 'truck', 'trust', 'truth', 'twist', 'uncle', 'union', 'upper', 'usual', 'value', 'video', 'virus', 'visit', 'voice', 'watch', 'water', 'weird', 'wheel', 'while', 'white', 'whole', 'woman', 'world', 'worry', 'worth', 'young', 'youth', 'abroad', 'access', 'action', 'active', 'advice', 'affair', 'affect', 'agency', 'amount', 'animal', 'annual', 'answer', 'appeal', 'aspect', 'assist', 'attack', 'author', 'basket', 'battle', 'beyond', 'bitter', 'border', 'boring', 'bother', 'bottle', 'bottom', 'branch', 'breast', 'breath', 'bridge', 'budget', 'button', 'camera', 'cancel', 'cancer', 'candle', 'career', 'carpet', 'chance', 'change', 'charge', 'choice', 'church', 'client', 'closet', 'coffee', 'collar', 'common', 'cookie', 'corner', 'county', 'couple', 'course', 'cousin', 'credit', 'damage', 'dealer', 'debate', 'degree', 'demand', 'design', 'desire', 'detail', 'device', 'dinner', 'divide', 'doctor', 'double', 'drawer', 'driver', 'editor', 'effect', 'effort', 'employ', 'energy', 'engine', 'escape', 'estate', 'excuse', 'expert', 'extent', 'factor', 'family', 'farmer', 'father', 'female', 'figure', 'finger', 'finish', 'flight', 'flower', 'formal', 'friend', 'future', 'garage', 'garden', 'gather', 'ground', 'growth', 'guitar', 'handle', 'health', 'height', 'horror', 'impact', 'income', 'injury', 'insect', 'inside', 'invite', 'island', 'jacket', 'junior', 'ladder', 'lawyer', 'leader', 'league', 'length', 'lesson', 'letter', 'listen', 'living', 'manner', 'market', 'master', 'matter', 'medium', 'member', 'memory', 'method', 'middle', 'minute', 'mirror', 'mobile', 'moment', 'mother', 'muscle', 'nation', 'native', 'nature', 'nobody', 'normal', 'notice', 'number', 'object', 'office', 'option', 'orange', 'parent', 'people', 'period', 'permit', 'person', 'phrase', 'player', 'plenty', 'poetry', 'police', 'policy', 'potato', 'priest', 'profit', 'prompt', 'public', 'purple', 'reason', 'recipe', 'record', 'refuse', 'region', 'regret', 'relief', 'remote', 'remove', 'repair', 'repeat', 'report', 'resist', 'resort', 'result', 'return', 'reveal', 'review', 'reward', 'safety', 'salary', 'sample', 'scheme', 'school', 'screen', 'script', 'search', 'season', 'second', 'secret', 'sector', 'senior', 'series', 'shower', 'signal', 'silver', 'simple', 'singer', 'single', 'sister', 'source', 'speech', 'spirit', 'spread', 'spring', 'square', 'stable', 'status', 'strain', 'street', 'stress', 'strike', 'string', 'stroke', 'studio', 'stupid', 'summer', 'survey', 'switch', 'system', 'tackle', 'target', 'tennis', 'thanks', 'theory', 'throat', 'ticket', 'tongue', 'travel', 'unique', 'visual', 'volume', 'wealth', 'weight', 'window', 'winner', 'winter', 'wonder', 'worker', 'writer', 'yellow', 'ability', 'account', 'address', 'advance', 'airline', 'airport', 'alcohol', 'analyst', 'anxiety', 'anybody', 'arrival', 'article', 'article', 'attempt', 'average', 'balance', 'bedroom', 'benefit', 'bicycle', 'brother', 'cabinet', 'capital', 'channel', 'chapter', 'charity', 'chicken', 'classic', 'climate', 'clothes', 'college', 'combine', 'comfort', 'command', 'comment', 'company', 'complex', 'concept', 'concern', 'concert', 'consist', 'contact', 'contest', 'context', 'control', 'convert', 'counter', 'country', 'courage', 'culture', 'current', 'deposit', 'diamond', 'disease', 'display', 'drawing', 'economy', 'emotion', 'evening', 'example', 'extreme', 'failure', 'feature', 'feeling', 'finance', 'finding', 'fishing', 'forever', 'fortune', 'freedom', 'funeral', 'garbage', 'general', 'grocery', 'hearing', 'highway', 'history', 'holiday', 'housing', 'husband', 'illegal', 'impress', 'initial', 'kitchen', 'leading', 'leather', 'lecture', 'library', 'machine', 'manager', 'maximum', 'meaning', 'meeting', 'mention', 'message', 'minimum', 'mission', 'mistake', 'mixture', 'monitor', 'morning', 'natural', 'network', 'nothing', 'officer', 'opening', 'opinion', 'outcome', 'outside', 'package', 'parking', 'partner', 'passage', 'passion', 'patient', 'pattern', 'payment', 'penalty', 'pension', 'physics', 'picture', 'plastic', 'present', 'primary', 'private', 'problem', 'process', 'produce', 'product', 'profile', 'program', 'project', 'promise', 'purpose', 'quality', 'quarter', 'reading', 'reality', 'recover', 'regular', 'release', 'request', 'reserve', 'resolve', 'respect', 'respond', 'revenue', 'routine', 'savings', 'science', 'scratch', 'section', 'service', 'session', 'setting', 'shelter', 'society', 'speaker', 'special', 'station', 'stomach', 'storage', 'stretch', 'student', 'subject', 'success', 'support', 'surgery', 'suspect', 'teacher', 'tension', 'thought', 'tonight', 'tourist', 'traffic', 'trainer', 'trouble', 'variety', 'vehicle', 'version', 'village', 'warning', 'weather', 'wedding', 'weekend', 'welcome', 'western', 'whereas', 'witness', 'working', 'writing', 'accident', 'activity', 'addition', 'ambition', 'analysis', 'anything', 'anywhere', 'argument', 'attitude', 'audience', 'baseball', 'bathroom', 'birthday', 'building', 'business', 'calendar', 'campaign', 'category', 'champion', 'chemical', 'computer', 'conflict', 'constant', 'contract', 'creative', 'currency', 'customer', 'database', 'daughter', 'decision', 'delivery', 'designer', 'director', 'disaster', 'discount', 'distance', 'district', 'document', 'election', 'elevator', 'emphasis', 'employee', 'employer', 'engineer', 'entrance', 'estimate', 'evidence', 'exchange', 'exercise', 'external', 'familiar', 'feedback', 'football', 'function', 'guidance', 'homework', 'hospital', 'incident', 'increase', 'industry', 'instance', 'interest', 'internal', 'internet', 'judgment', 'language', 'location', 'magazine', 'marriage', 'material', 'medicine', 'midnight', 'mortgage', 'mountain', 'national', 'negative', 'occasion', 'official', 'opposite', 'ordinary', 'original', 'painting', 'patience', 'personal', 'physical', 'platform', 'pleasure', 'politics', 'position', 'positive', 'possible', 'practice', 'presence', 'pressure', 'priority', 'progress', 'property', 'proposal', 'purchase', 'quantity', 'question', 'reaction', 'register', 'relation', 'relative', 'republic', 'research', 'resident', 'resource', 'response', 'sandwich', 'schedule', 'security', 'sentence', 'shopping', 'shoulder', 'software', 'solution', 'specific', 'standard', 'stranger', 'strategy', 'strength', 'struggle', 'surprise', 'surround', 'swimming', 'sympathy', 'teaching', 'tomorrow', 'training', 'upstairs', 'vacation', 'valuable', 'weakness', 'advantage', 'afternoon', 'agreement', 'apartment', 'assistant', 'associate', 'attention', 'awareness', 'beautiful', 'beginning', 'boyfriend', 'breakfast', 'brilliant', 'candidate', 'challenge', 'character', 'chemistry', 'childhood', 'chocolate', 'cigarette', 'classroom', 'committee', 'community', 'complaint', 'condition', 'confusion', 'criticism', 'departure', 'dependent', 'dimension', 'direction', 'economics', 'education', 'effective', 'emergency', 'equipment', 'extension', 'following', 'guarantee', 'highlight', 'historian', 'implement', 'inflation', 'influence', 'inspector', 'insurance', 'intention', 'interview', 'knowledge', 'landscape', 'marketing', 'necessary', 'newspaper', 'objective', 'operation', 'passenger', 'pollution', 'potential', 'president', 'principle', 'procedure', 'professor', 'promotion', 'reception', 'recording', 'reference', 'secretary', 'selection', 'sensitive', 'signature', 'situation', 'somewhere', 'spiritual', 'statement', 'structure', 'substance', 'telephone', 'temporary', 'tradition', 'variation', 'vegetable', 'yesterday', 'appearance', 'assignment', 'assistance', 'assumption', 'atmosphere', 'background', 'collection', 'commercial', 'commission', 'comparison', 'conclusion', 'conference', 'confidence', 'connection', 'definition', 'department', 'depression', 'difference', 'difficulty', 'discipline', 'discussion', 'efficiency', 'employment', 'enthusiasm', 'equivalent', 'excitement', 'experience', 'expression', 'foundation', 'friendship', 'girlfriend', 'government', 'importance', 'impression', 'indication', 'individual', 'inevitable', 'initiative', 'inspection', 'investment', 'leadership', 'literature', 'management', 'membership', 'obligation', 'particular', 'percentage', 'perception', 'permission', 'philosophy', 'population', 'possession', 'preference', 'profession', 'protection', 'psychology', 'reflection', 'reputation', 'resolution', 'restaurant', 'revolution', 'specialist', 'suggestion', 'technology', 'television', 'transition', 'university', 'advertising', 'alternative', 'application', 'appointment', 'association', 'celebration', 'combination', 'comfortable', 'competition', 'concentrate', 'consequence', 'description', 'development', 'engineering', 'environment', 'examination', 'explanation', 'grandfather', 'grandmother', 'imagination', 'improvement', 'independent', 'information', 'instruction', 'interaction', 'maintenance', 'measurement', 'negotiation', 'opportunity', 'performance', 'personality', 'perspective', 'possibility', 'preparation', 'recognition', 'replacement', 'requirement', 'supermarket', 'temperature', 'championship', 'construction', 'contribution', 'conversation', 'distribution', 'independence', 'introduction', 'manufacturer', 'organization', 'presentation', 'professional', 'refrigerator', 'relationship', 'satisfaction', 'significance', 'communication', 'consideration', 'entertainment', 'establishment', 'international', 'understanding', 'administration', 'recommendation', 'representative', 'responsibility', 'transportation']
	def find_word(grid, row, col):
		word = ""
		while col < len(grid[row]) and grid[row][col] != "X":
			word += grid[row][col]
			col += 1
		return word
	def checker(func, template):
		result = func(template, WORDS)
		for e in result: print(e)
		# types check
		if not isinstance(result, (tuple, list)):
			return ERROR_TYPE
		if not all(isinstance(row, str) for row in result):
			return ERROR_TYPE
		# size check
		if (len(result) != len(template) or
				any(len(result[i]) != len(template[i]) for i in range(len(template)))):
			return ERROR_SIZE
		# template, letters and filled check
		for i, row in enumerate(result):
			for j, ch in enumerate(row):
				if ch == "X":
					if template[i][j] != "X":
						return ERROR_TEMPLATE
				elif ch == ".":
					return ERROR_UNFILLED
				elif ch in string.ascii_lowercase:
					if template[i][j] != "." and template[i][j] != ch:
						return ERROR_TEMPLATE
				else:
					return ERROR_TYPE_CELL
		# words checking
		used_words = set()
		rotated_result = ["".join(row) for row in zip(*result)]
		words = []
		for k, row in enumerate(template):
			for m, symb in enumerate(row):
				if symb == "X":
					continue
				if (k == 0 or template[k - 1][m] == "X") and (k < len(template) - 1 and template[k + 1][m] == "."):
					words.append(find_word(rotated_result, m, k))
				if (m == 0 or template[k][m - 1] == "X") and (m < len(template[k]) - 1 and template[k][m + 1] == "."):
					words.append(find_word(result, k, m))
		for w in words:
			if w in used_words:
				return F_ERROR_REPEATED(w)
			used_words.add(w)
			if w not in WORDS:
				return F_ERROR_UNKNOWN(w)
		return True, "Great!"
	result, message = checker(solver, ['.XXX.', '...X.', '.X.X.', '.....'])
	assert result, "1: " + message
	result, message = checker(solver, ['X.XX', '....', 'X.XX', 'X...', 'XXX.', '....', 'XXX.'],)
	assert result, "2: " + message
	result, message = checker(solver, ['...XXXXXX', '.XXX.X...', '.....X.XX', 'XXXX.X...',
									   'XX...X.XX', 'XX.XXX.X.', 'X......X.', 'XX.X.XXX.', 'XXXX.....'],)
	assert result, "3: " + message
	result, message = checker(solver, [
		"XXXXXXXbXXXXXcX",
		"lXteachingXXXaX",
		"aXoXXXXkXXX.XlX",
		"youXXXXeXXX..m.",
		"XXrXX.XXX.X.XXX",
		"X.i...XXX......",
		"XXsXX.X.X.XXX.X",
		"XXtechnologyX.X",
		"XXXXXXX.X.X.XXX",
		"X.XXXtotalX...X",
		"X.X.X.X.XXX.X.X",
		"X.....XXX.....X",
		"XXX.X.XXX.X.X.X",
		"....XXXXX.XXX.X",
		"XXXXXXXXX.XXXXX"],)
	assert result, "4: " + message
	result, message = checker(solver, [
		'....X.X.X.X....', '.XXXX.X.X.X.XX.', '......X.X....X.', 'XX.XX.X.X.XXXX.', '.X.XX........X.', '...XX.XXXXX.XXX',
    	'.XXXX.X.XXX....', '....X....XXXX.X', 'XXX.XXX.XXXXX.X', 'XXX.XX......X.X', '..XXXXXXX.X.XXX', 'X.XX......X....',
    	'X.XXX.X.X.X.X.X', 'X.....X...XXX.X', 'XXXXXXX.X.X...X'],)
	assert result, "5: " + message
	result, message = checker(solver,  [
		'......X.XXXXX.X.....', 'X.XXXXX.XXX.X.X.X.XX', 'X.X.....XXX...X....X', 'X.X.XXXXX.X.XXX.XXXX',
    	'......XXX...X......X', 'XXX.X.X.X.XXX.X.XX.X', '....X.....XX.....X.X', 'XXX.XXX.XXXXX.XXXXXX',
    	'....XXX.X.X.X.....X.', 'XXX.XX......X.XXXXX.', 'XXX.XXXXX.X.X.XXXXX.', '....XX....X.........',
    	'XXXXXXX.XXX.XXXX.XXX', 'XXXX....XX.....X...X', 'X.XXX.X.XXXXX.XX.XXX', 'X.XX..X.......XX....',
    	'X.XXX.X.X.X.X.XX.X.X', 'X.....XXX.X.XXXXXX.X', 'X.X.X.X.....XXX....X', 'X.X.XXXXXXXXXXXXXX.X'],)
	assert result, "6: " + message