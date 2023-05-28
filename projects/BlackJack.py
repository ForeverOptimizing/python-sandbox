# 
# Blackjack 12/07/21
# 

# ERROR LINE 281 "bingo undefined" when doing max bet leaving bankroll at 0     |10/22/22





# Declare Global Variables

suits = ('Hearts','Diamonds','Spades','Clubs')
ranks = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace')
values = {'Two':2, 'Three':3, 'Four':4, 'Five':5, 'Six':6, 'Seven':7, 'Eight':8,
         'Nine':9, 'Ten':10, 'Jack':10, 'Queen':10, 'King':10, 'Ace':11}
BANKROLL = 2000.00
# Import methods
import random

# Create Classes
# Good
class Card:
    def __init__(self,suit,rank):
        self.suit = suit
        self.rank = rank
        self.value = values[rank]

    def __str__(self):
        return f'{self.rank} of {self.suit}'

# Good
class Deck:
    def __init__(self):
        self.all_cards = []
        for suit in suits:
            for rank in ranks:
                self.all_cards.append(Card(suit,rank))

    def __str__(self):
        return f'{len(self.all_cards)} cards in deck'

    def shuffle(self):
        random.shuffle(self.all_cards)

    def deal_one(self):
        return self.all_cards.pop()

    def add_cards(self,cards):
        if type(cards) != type([]):
            self.all_cards.append(cards)
        else:
            self.all_cards.extend(cards)


class Bank:
    def __init__(self,init_value):
        self.init_value = init_value
        self.bankroll = init_value

    def __str__(self):
        return f'You have: ${self.bankroll}'

    # Returns amount of money used in bet
    def bet(self):
        keep_going = True
        while(keep_going):
            try: 
                money = float(input(f"Your current Bankroll is: ${self.bankroll}\nHow much would you like to bet?\n"))
                if money <= self.bankroll:
                    self.bankroll -= money
                    print(f'Bet of ${money} accepted\n')
                    return money
                else:
                    print(f'Your bet exceeds your bankroll. Please try again.')
            except:
                print('Please try again.')

    def add_winnings(self,winnings):
        self.bankroll += winnings



# Variable Declaration


new_bank = Bank(BANKROLL)


# Create Functions

# GOOD (Returns value)
def deal_cards_dealer():
    # Give Dealer 2 Cards
    dealer_hand.append(new_deck.deal_one())
    dealer_hand.append(new_deck.deal_one())
    # Print name of one card
    print(f'Dealer is showing {dealer_hand[0]}\n')
    # Determine if dealer has blackjack
    dsum = 0
    dsum += dealer_hand[0].value
    dsum += dealer_hand[1].value
    return dsum

# GOOD (Returns value)
def deal_cards_player():
    # give player two cards
    player_hand.append(new_deck.deal_one())
    player_hand.append(new_deck.deal_one())
    # Print names of the cards
    print(f'Your hand: {player_hand[1]} | {player_hand[0]}')
    # Print Value of the hand
    sum = 0
    sum += player_hand[0].value
    sum += player_hand[1].value
    if sum == 22:
        sum -= 10
    print(f'Value: {sum}')
    # Return value of hand
    return sum


def player_hit():
    player_ace = False
    # Adds card to players hand
    player_hand.append(new_deck.deal_one())
    # Prints all cards in player's hand
    print('Your hand:')
    sum = 0
    for card in player_hand:
        print(card)
        if card.value == 11:
            player_ace = True
        if (sum > 21) and (player_ace == True):
            sum -= 10
            player_ace = False
        sum += card.value

    
    # Check for player Ace and decrease by 10 if over 21
    # if (sum > 21) and (player_ace == True):
    #     sum -= 10
    #     player_ace = False
    # Prints value of player's hand
    print(f'Value: {sum}')
    # Returns value of player's hand
    return sum

def dealer_turn():
    # Prints dealers current cards
    # Determine if ace is in possession
    # If under 16 draw another card
    # keep drawing until above 16
    # print cards in dealer's hand
    # print value of cards
    # return value of cards
    dealer_ace = False
    print(f'Dealer has: {dealer_hand[0]} | {dealer_hand[1]}')
    sum = dealer_hand[0].value + dealer_hand[1].value
    for card in dealer_hand:
        if card.value == 11:
            dealer_ace = True
    dhitting = True
    while(dhitting):
        if sum > 16 and dealer_ace == False:
            dhitting = False
        elif sum > 21 and dealer_ace == True:
            sum -= 10
            dealer_ace = False
        elif sum < 17:
            dealer_hand.append(new_deck.deal_one())
            print(f'Dealer draws: {dealer_hand[-1]}')
            sum += dealer_hand[-1].value
            if dealer_hand[-1].value == 11:
                dealer_ace = True
        else:
            dhitting = False

    print(f"Dealer's hand is valued at: {sum}")
    return sum




game_on = True
while(game_on):

    dealer_hand = []
    player_hand = []
    player_sum = 0
    dealer_sum = 0
    player_busted = False
    dealer_busted = False
    # player_ace = False
    # dealer_ace = False
    current_bet = 0
    player_blackjack = False

    # Create a deck of 52 cards
    new_deck = Deck()
    # Shuffle the deck
    new_deck.shuffle()
    # Ask the player for their bet
    # Make sure that the Player's bet does not exceed their available chips
    current_bet = new_bank.bet()
    # Deal two cards to the Dealer and two cards to the Player
    # Show only one of the Dealer's cards, the other remains hidden
    # Show both of the Player's cards
    dealer_sum = deal_cards_dealer()
    player_sum = deal_cards_player()

    # Fixes case of two aces
    if player_sum == 22:
        player_hand[0].value = 1
    elif player_sum == 21:
        player_blackjack = True
        current_bet *= 2.5
        print('Player has BlackJack!')
        print(f"Player wins! ${current_bet}")
        new_bank.add_winnings(current_bet)
        print(f"Current Bankroll {new_bank.bankroll}")

    # Ask the Player if they wish to Hit, and take another card
    # If the Player's hand doesn't Bust (go over 21), ask if they'd like to Hit again
    hitting = True
    if player_blackjack:
        hitting = False
    elif dealer_sum == 21 and player_sum != 21:
        print("Dealer has Blackjack. Dealer wins")
        hitting = False
        player_busted = True
    elif dealer_sum == 21 and player_sum == 21:
        hitting = False
    else:
        pass

    while hitting:
        if dealer_sum == 21 and player_sum < dealer_sum:
            print(f'Dealer has BlackJack. Dealer wins.')
            hitting = False
        try:
            response = int(input('Would you like to hit?:\n1) Yes\n2) No\n'))
            if response == 1:
                player_sum = player_hit()
                if player_sum > 21:
                    print('BUSTED YOU LOSE\n')
                    player_busted = True
                    hitting = False
            elif response == 2:
                hitting = False
            else:
                print('Invalid response')
        except:
            print('Invalid response')

    # If a Player Stands, play the Dealer's hand. The dealer will always Hit until the Dealer's value meets or exceeds 17
    if player_busted == False and player_blackjack == False:
        dealer_sum = dealer_turn()
        if dealer_sum > 21:
            dealer_busted = True
        # Determine the winner and adjust the Player's chips accordingly
        if player_sum > dealer_sum or dealer_busted == True:
            current_bet *= 2
            new_bank.add_winnings(current_bet)
            print(f"Player Wins! You have won ${current_bet}")
        elif dealer_sum > player_sum:
            print(f"You have lost. Current Bankroll is: ${new_bank.bankroll}")
        else:
            print("PUSH")
            new_bank.add_winnings(current_bet)
            print(f"Current Bankroll is: ${new_bank.bankroll}")
        


    # Ask the Player if they'd like to play again
    if new_bank.bankroll > 0:
        bingo = True
    else:
        print("Out of money fella, better luck next time.")
        game_on = False
    while(bingo):
        try:
            play_again = int(input('Would you like to play again?\n1) Yes\n2) No\n'))
            if play_again == 1:
                bingo = False
            elif play_again == 2:
                print(f'Coward! Your bankroll is at ${new_bank.bankroll}')
                game_on = False
                bingo = False
            else:
                print('Invalid response')
        except:
            print('Invalid response')












