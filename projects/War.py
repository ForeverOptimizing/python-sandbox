import random
WAR_CONST = 3
suits = ('Hearts', 'Diamonds', 'Spades', 'Clubs')
ranks = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace')
values = {'Two':2, 'Three':3, 'Four':4, 'Five':5, 'Six':6, 'Seven':7, 'Eight':8, 
            'Nine':9, 'Ten':10, 'Jack':11, 'Queen':12, 'King':13, 'Ace':14}

print(values['Two'])



class Card:
    def __init__(self,rank,suit):
        self.rank = rank
        self.suit = suit
        self.value = values[rank]

    def __str__(self):
        return f'{self.rank} of {self.suit}'


class Deck:
    def __init__(self):
        self.all_cards = []
        for suit in suits:
            for rank in ranks:
                self.all_cards.append(Card(rank,suit))

    def shuffle(self):
        random.shuffle(self.all_cards)

    def deal_one(self):
        return self.all_cards.pop()




class Player:
    def __init__(self,name):
        self.name = name
        self.all_cards = []

    def remove_one(self):
        return self.all_cards.pop()

    def add_cards(self,cards):
        if type(cards) != type([]):
            self.all_cards.append(cards)
        else:
            self.all_cards.extend(cards)


#     def __str__(self):
#         return f'{self.name} has {len(self.all_cards)} cards'
# class Player:
    
#     def __init__(self,name):
#         self.name = name
#         # A new player has no cards
#         self.all_cards = [] 
        
#     def remove_one(self):
#         # Note we remove one card from the list of all_cards
#         # We state 0 to remove from the "top" of the deck
#         # We'll imagine index -1 as the bottom of the deck
#         return self.all_cards.pop(0)
    
#     def add_cards(self,new_cards):
#         if type(new_cards) == type([]):
#             self.all_cards.extend(new_cards)
#         else:
#             self.all_cards.append(new_cards)
    
    
#     def __str__(self):
#         return f'Player {self.name} has {len(self.all_cards)} cards.'
    



#Initialize



# print("Spawning Players")
# name1 = input('What is the name of Player 1: \n')
# name2 = input('What is the name of Player 2: \n')

# P1 = Player(name1)
# P2 = Player(name2)
# print("Spawning Deck")
# mainDeck = Deck()
# print("Shuffling Deck")
# Deck.shuffle
# print("Giving players their cards")

# for x in range(26):
#     P1.add_cards(mainDeck.deal_one())
#     P2.add_cards(mainDeck.deal_one())


# game_on = True
# # Spawn Table

# while(game_on):
#     table = []

# # Each player deals one card onto the table
#     table.append(P1.remove_one)
#     table.append(P2.remove_one)
# # Display what cards are on the table




# Whoever has the higher value card gets to keep both cards



# Game Setup
player_one = Player("One")
player_two = Player("Two")

new_deck = Deck()
new_deck.shuffle()

for x in range(26):
    player_one.add_cards(new_deck.deal_one())
    player_two.add_cards(new_deck.deal_one())




# While game_on
round_num = 0
game_on = True

while (game_on):


    #player one lose
    if len( player_one.all_cards) == 0:
        print('Player One, is out of cards')
        print('Player Two Wins!')
        game_on = False
        break
    #player two lose
    if len( player_two.all_cards) == 0:
        print('Player Two, is out of cards')
        game_on = False
        print('Player One Wins!')
        break

    #round counter
    round_num += 1
    print(f'Round {round_num}')

    # New round start
    player_one_cards = []
    player_two_cards = []
    player_one_cards.append(player_one.remove_one())
    player_two_cards.append(player_two.remove_one())

    # While at_war
    at_war = True
    while (at_war):

        if player_one_cards[-1].value > player_two_cards[-1].value:
            player_one.add_cards(player_one_cards)
            player_one.add_cards(player_two_cards)
            at_war = False

        elif player_one_cards[-1].value < player_two_cards[-1].value:
            player_two.add_cards(player_one_cards)
            player_two.add_cards(player_two_cards)
            at_war = False

        else:
            print("WAR!!")
            if len(player_one.all_cards) < WAR_CONST:
                print('Player One Loses. Player Two Wins!')
                game_on = False
                at_war = False

            elif len(player_two.all_cards) < WAR_CONST:
                print('Player Two Loses. Player One Wins!')
                game_on = False
                at_war = False

            else:
                for _ in range(WAR_CONST):
                    player_one_cards.append(player_one.remove_one())
                    player_two_cards.append(player_two.remove_one())
                    


















