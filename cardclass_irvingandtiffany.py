
import random

class Card(object):

    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank

    def __str__(self):
        if self.rank != "10":
            card = """
            __________
            |        |
            |   """+self.rank+"""    |
            | """+self.suit+"""|
            |        |
            |________|"""
            return card
        else:
            card = """
            __________
            |        |
            |  """+self.rank+"""    |
            | """+self.suit+"""|
            |        |
            |________|"""
            return card

class Deck(object):
    
    def __init__(self):
        suit_names = ["Clubs", "Diamonds", "Hearts", "Spades"]
        rank_names = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]
        
        self.cards = []
        for suit in suit_names:
            for rank in rank_names:
                card = Card(suit,rank)
                self.cards.append(card)
                           

    def add_card(self, card):
        self.cards.append(card)

    def remove_card(self, card):
       
        self.cards.remove(card)
    def deal_cards(self,person):
        t = 7
        while t != 0:
            person.hand.append(self.cards[random.randint(0,len(self.cards) - 1)])
            t -= 1

    def shuffle(self):
       
        random.shuffle(self.cards)

class Player(object):
    def __init__(self,name):
        self.name = name
        self.hand = []
        self.card_count = len(self.hand)
    
    def remove_card(self,card):
        self.hand.remove(card)
    
    # def add_card(self, card):
    #     for card in cards: