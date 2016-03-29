from cardclass_irvingandtiffany import *
import time
#CURRENT TO DO LIST: 
# MAKE THE REVERSE FEATURE WORK: J

s = raw_input("Name?")
def shuffle_names(name):
	
	l = list(name)
	random.shuffle(l)
	result = ''.join(l)
	return result.title()

def crazy_eights():
	print "Welcome,",s," to... "
	a = """
		888888888888888
		8 Crazy Eights8
		888888888888888"""
	print a
	print "PLEASE TURN ON CAPS LOCK"
	
	def player_hand(player):
		for card in player.hand:
			print card
	deck = Deck()

	p1 = Player(s.title())
	p2 = Player(shuffle_names(s))
	p3 = Player(shuffle_names(s))
	p4 = Player(shuffle_names(s))

	deck.deal_cards(p1)
	deck.deal_cards(p3)
	deck.deal_cards(p2)
	deck.deal_cards(p4)
	print "Today's game is",random.choice(['our hero','Master','Mr.','Ms.']),p1.name +" vs",p2.name+" vs",p3.name+" vs",p4.name+"."
	time.sleep(3)
	
	def player_turn(player,top):
			fail = False
			################EVIL CARD CHECK########################
			if top.rank == "K":
				print "You have been skipped"
				top.rank = "k" #made the rank lower case to end the skipping. It is changed back to uppercase with .title() later on.
			elif top.rank == "Q":
				print "+2 cards for you."
				card1=random.choice(deck.cards)
				card2=random.choice(deck.cards)
				print card1,card2
				player.hand.append(card1)
				player.hand.append(card2)
				
				top.rank = "q" 
			######################################
			else:
				print player.name +"'s hand."
				player_hand(player)
				play = int(raw_input("Which card do you want to play? (1 - "+str(len(player.hand))+"). To pass, pick a card that can't be played.")) - 1
				if play > len(player.hand) - 1:
					print "That card does not exist. You must pass."
					player.hand.append(random.choice(deck.cards))
				else:
					playing_card = player.hand[play]
					if playing_card.suit == top.suit or playing_card.rank == top.rank.title(): #Just incase the last card has been skipped before.
						top = playing_card
						player.remove_card(playing_card)
						#crazy eights makes you change the suit if the card is an eight. Find an easy way to get this done.
						if top.rank == "8":
							deciding = True
							while deciding:
								change = raw_input("You played an 8! Change the suit! (Type first letter of the suit)")
								if change == "S":
									top.suit == "Spades"
									deciding = False
									
								elif change == "H":
									top.suit = "Hearts"
									deciding = False
								elif change == "D":
									top.suit = "Diamonds"
									deciding = False
								elif change == "C":
									top.suit = "Clubs"
									deciding = False
								else:
									print "Lets try this again."
								print "Suit has changed to",top.suit
					else:
						print "Cannot play that card. Therefore, you must pass."
						player.hand.append(random.choice(deck.cards))
						fail = True
					if fail:
						print "You tried to play",playing_card,"but it failed!"
					else:
						print "You played",playing_card
			return top
			
	def opponent_turn(opponent,top):
		print opponent.name,"has",len(opponent.hand),"cards left."
		find = False
		if top.rank == "K":
			print opponent.name,"has been skipped."
			top.rank = "k"
		if top.rank == "Q":
			print opponent.name,"gets +2 cards."
			opponent.hand.append(random.choice(deck.cards))
			opponent.hand.append(random.choice(deck.cards))
			top.rank = "q"
		else:
			while not find:
				choices = []
				for card in opponent.hand:
					if card.suit == top.suit or card.rank == top.rank.title():
						find = True
						choices.append(card)
				if find:
					play = random.choice(choices)
					top = play
					print opponent.name + " plays",play
					#crazy eights makes you change the suit if the card is an eight. Make the opponent do that randomly.
					if top.rank == "8": 
						top.suit = random.choice(["Clubs", "Diamonds", "Hearts", "Spades"])
						print opponent.name + " changed the suit to " + top.suit
					opponent.hand.remove(play)
				if not find:
					print opponent.name + " cannot play. " + opponent.name +" passes and picks up."
					opponent.hand.append(random.choice(deck.cards))
					
					find = True
		return top
	top = random.choice(deck.cards)

	alive = True
	while alive:
		print
		print "	   _____________________"
		print "		 Center Card"
		print top
		print "	   _____________________"

		
		
		top = player_turn(p1,top)
		#Computer(s)'s turn
		top = opponent_turn(p2,top)
		time.sleep(2)
		top = opponent_turn(p3,top)
		time.sleep(2)
		top = opponent_turn(p4,top)
		time.sleep(2)
		
		
		
		if len(p1.hand) == 0:
			alive = False
			print "You Win"
		elif len(p2.hand) == 0 or len(p3.hand) == 0 or len(p4.hand) == 0:
			print "You lose"
			alive = False
crazy_eights()