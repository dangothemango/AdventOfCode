class camel_hand:
	def __init__(self, line):
		line = line.split(' ')
		self.hand = line[0]
		self.bet = int(line[1])
		self.strength = self.get_hand_strength()

	def update_bet(self, mult):
		#print('old ', self.hand, self.bet)
		self.bet *= mult
		#print('new ', self.hand, self.bet)


	def get_hand_strength(self)->int:
		char_count = {}
		for char in self.hand:
		    if get_card_val(char) in char_count:
		        char_count[get_card_val(char)] += 1
		    else:
		        char_count[get_card_val(char)] = 1

		#THIS IS FINE BECAUSE NO STRAIGHTS IN THIS PROBLEM
		if len(char_count) == 1:
			return 6
		if len(char_count) == 2:
			if max(char_count.values()) == 3:
				return 4
			if max(char_count.values()) == 4:
				return 5
		if len(char_count) == 3:
			if max(char_count.values()) == 2:
				return 2
			return max(char_count.values())



		if len(char_count) == 5:
			return 0
		if max(char_count.values()) == 2:
			if len(char_count) == 3:
				return 2
			return 1
		if max(char_count.values()) == 3:
			if len(char_count) == 2:
				return 4
			else:
				return 3
		if max(char_count.values()) == 4:
			return 5


	def __lt__(self, other):
		if self.strength == other.strength:
			for i in range(5):
				if self.hand[i] != other.hand[i]:
					return get_card_val(self.hand[i]) < get_card_val(other.hand[i])
			return False
		return get_card_val(self.strength) < get_card_val(other.strength)


def get_card_val(card)->int:
	if card == 'T':
		return 10
	if card == 'J':
		return 11
	if card == 'Q':
		return 12
	if card == 'K':
		return 13
	if card == 'A':
		return 14
	return int(card)


def main():
    file = open('input.txt').read().strip()
    lines = file.split('\n')
    hands = [camel_hand(line) for line in lines]
    #print(x.hand for x in sorted(hands))
    i = 0
    total_winnings = 0
    for hand in sorted(hands):
    	i += 1
    	hand.update_bet(i)
    	total_winnings += hand.bet
    	print(i, hand.hand, hand.bet)
    bets = [x.bet for x in hands]
    print(sum(bets))
    return 0

if __name__ =='__main__':
    main()
