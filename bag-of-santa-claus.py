def choose_good_gift(total_gifts, bag, accept_gift):
	value=max(bag.__closure__[0].cell_contents)
	enum=bag()
	for i,e in enumerate(enum):
		if e == value:
			accept_gift()
			return

'''
	enum=bag()
	n=total_gifts//3
	gifts=[]
	for i in range(n):
		gifts.append(next(enum))
	#value=int(1.1*sum(gifts)/n)
	value=max(gifts)
	total_gifts-=n
	for i,e in enumerate(enum):
		if e > value or i==total_gifts-1:
			accept_gift()
			return
'''

if __name__ == '__main__':
	from random import random, randint, uniform
	def priority_post_factum(gifts):
		def do_accept():
			nonlocal gift_value
			if gift_value is None:
				if idx < len(gifts):
					gift_value = gifts[idx]
				else:
					print("Is that a joke - to say 'accept' when"
						  " gift wasn't taken from the bag?")
			else:
				print('Sorry, you made your choice already.')
		def gift_generator():
			nonlocal idx
			while idx:
				idx -= 1
				yield gifts[idx]
		idx, gift_value = len(gifts), None
		choose_good_gift(idx, gift_generator, do_accept)
		if gift_value is None:
			print('Unfortunately, you did not choose anything.')
			return len(gifts)
		else:
			return sum(gift_value < x for x in gifts)
	def check_solution(bag_count):
		standings = gift_count = best_gifts = 0
		for i in range(bag_count):
			gifts_in_bag = randint(10, 1000)
			gift_count += gifts_in_bag
			scale = (random() + random()) ** randint(0, 1024)
			priority = priority_post_factum([uniform(0., scale) for _ in range(gifts_in_bag)])
			standings += priority
			best_gifts += not priority
		print('You do won {:n} best gifts from {:n} bags with {:,} gifts!\n'
			  'It seems like for bags of {:n} gifts -\n'
			  'you would choose the second best gift, silver ;)'
			  .format(best_gifts, bag_count, gift_count, round(gift_count / standings) + 1))
	check_solution(1000)