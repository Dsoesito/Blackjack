from cmath import sin
import random

class Blackjack:
    def __init__(self, balance):
        #initiating all the values/strings/conditionals
        self.balance = balance
        self.bet = 0
        self.all_cards = []
        self.dealer_hand = []
        self.player_hand = []
        self.dealer_value_hidden = 0
        self.dealer_value = 0
        self.player_value = 0
        self.dealer_aces = 0
        self.player_aces = 0
        self.dealer_wins = False
        self.player_wins = False

    def build_deck(self):
        # building the deck
        suits = ('Hearts', 'Diamonds', 'Spades', 'Clubs')
        ranks = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace')
        for suit in suits:
            for rank in ranks:
                self.all_cards.append(rank + " of " + suit)
    
    def shuffle_deck(self):
        random.shuffle(self.all_cards)

    def deal_dealer(self):
        # dealing the card t dealer + fidning value of hand/number of aces
        single_card = self.all_cards.pop(-1)
        if "Two" in single_card:
            self.dealer_value += 2
        elif "Three" in single_card:
            self.dealer_value += 3
        elif "Four" in single_card:
            self.dealer_value += 4
        elif "Five" in single_card:
            self.dealer_value += 5
        elif "Six" in single_card:
            self.dealer_value += 6
        elif "Seven" in single_card:
            self.dealer_value += 7
        elif "Eight" in single_card:
            self.dealer_value += 8
        elif "Nine" in single_card:
            self.dealer_value += 9
        elif "Ten" in single_card or "Jack" in single_card or "Queen" in single_card or "King" in single_card:
            self.dealer_value += 10
        else:
            self.dealer_aces += 1
            self.dealer_value += 11
        self.dealer_hand.append(single_card)
        if self.dealer_aces > 0 and self.dealer_value > 21:
            self.dealer_aces -= 1
            self.dealer_value -= 10
        else:
            pass

    def deal_player(self):
        # dealing the card to player + fidning value of hand/number of aces
        single_card = self.all_cards.pop(-1)
        if "Two" in single_card:
            self.player_value += 2
        elif "Three" in single_card:
            self.player_value += 3
        elif "Four" in single_card:
            self.player_value += 4
        elif "Five" in single_card:
            self.player_value += 5
        elif "Six" in single_card:
            self.player_value += 6
        elif "Seven" in single_card:
            self.player_value += 7
        elif "Eight" in single_card:
            self.player_value += 8
        elif "Nine" in single_card:
            self.player_value += 9
        elif "Ten" in single_card or "Jack" in single_card or "Queen" in single_card or "King" in single_card:
            self.player_value += 10
        else:
            self.player_aces += 1
            self.player_value += 11
        self.player_hand.append(single_card)
        if self.player_aces > 0 and self.player_value > 21:
            self.player_aces -= 1
            self.player_value -= 10
        else:
            pass

    def single_dealer_val(self):
        # finding the value for the card that will be shown tod ealer
        if "Two" in self.dealer_hand[0]:
            self.dealer_value_hidden += 2
        elif "Three" in self.dealer_hand[0]:
            self.dealer_value_hidden += 3
        elif "Four" in self.dealer_hand[0]:
            self.dealer_value_hidden += 4
        elif "Five" in self.dealer_hand[0]:
            self.dealer_value_hidden += 5
        elif "Six" in self.dealer_hand[0]:
            self.dealer_value_hidden += 6
        elif "Seven" in self.dealer_hand[0]:
            self.dealer_value_hidden += 7
        elif "Eight" in self.dealer_hand[0]:
            self.dealer_value_hidden += 8
        elif "Nine" in self.dealer_hand[0]:
            self.dealer_value_hidden += 9
        elif "Ten" in self.dealer_hand[0] or "Jack" in self.dealer_hand[0] or "Queen" in self.dealer_hand[0] or "King" in self.dealer_hand[0]:
            self.dealer_value_hidden += 10
        else:
            self.dealer_value_hidden += 11

    def print_single_dealer(self):
        # printing single card from dealer hand
        print("Dealer's hand: \n" + self.dealer_hand[0] + "\n*hidden card*")
        print("Dealer value: " + str(self.dealer_value_hidden))

    def print_all_dealer(self):
        # showing the entire dealer's hand
        print("Dealer's hand: ")
        for i in range(len(self.dealer_hand)):
            print(self.dealer_hand[i])
        print("Dealer value: " + str(self.dealer_value))

    def print_all_player(self):
        # prnting the entire player's hand
        print("Player's hand: ")
        for i in range(len(self.player_hand)):
            print(self.player_hand[i])
        print("Player value: " + str(self.player_value))

    def check_bust(self):
        #checking of any player went bust
        if self.dealer_value > 21:
            print("\n\nPlayer wins!\n\n")
            self.balance += self.bet
            self.player_wins = True
        elif self.player_value > 21:
            print("\n\nDealer wins!\n\n")
            self.balance -= self.bet
            self.dealer_wins = True
        elif self.dealer_value == 21 and self.player_value == 21:
            print("\n\nPlayer wins!\n\n")
            self.balance += self.bet
            self.player_wins = True
        elif self.player_value > self.dealer_value:
            print("\n\nPlayer wins!\n\n")
            self.balance += self.bet
            self.player_wins = True
        else:
            print("\n\nDealer wins!\n\n")
            self.balance -= self.bet
            self.dealer_wins = True

    def clear(self):
        # clearing all values for new game, but keeping balance and deck the same
        self.bet = 0
        self.dealer_hand.clear()
        self.player_hand.clear()
        self.dealer_value_hidden = 0
        self.dealer_value = 0
        self.player_value = 0
        self.dealer_aces = 0
        self.player_aces = 0
        self.dealer_wins = False
        self.player_wins = False

    def initiate_game(self):
        # starting firs game
        self.build_deck()
        self.shuffle_deck()
        self.deal_dealer()
        self.deal_dealer()
        self.deal_player()
        self.deal_player()
        self.single_dealer_val()

    def initiate_new_game(self):
        # starting all games after the first one
        self.deal_dealer()
        self.deal_dealer()
        self.deal_player()
        self.deal_player()
        self.single_dealer_val()

    def play_game(self):
        # main game method
        play_on = True
        while self.balance > 0 and play_on == True:                 # intro ststent, assuming player want to play and has money
            player_stand = False
            print("\n" * 50)
            print("Welcome to Blackjack! \n")
            while self.dealer_wins == False and self.player_wins == False:
                print("Here is how much you have: " + str(self.balance))
                self.bet = input("\nHow much would you like to bet? \n")    # asking player how much they want to bet
                self.bet = int(self.bet)
                if self.bet > self.balance:                                 # if player bets too much
                    print("Please only bet what you have!")
                elif self.bet < 0:                                          # if player best less than zero
                    print("Please bet a positive amount!")
                elif self.bet == 0:                                         # if player bets zero
                    print("Please bet a valid amount!")
                else:                                                       # entering game, assuming player bets valid amount
                    print("\n" * 50)
                    self.print_single_dealer()                              # showing single dealer card
                    print("\n" * 2)
                    print("Current bet: " + str(self.bet))                  # current bet
                    print("\n" * 2)
                    self.print_all_player()                                 # showing players entire hand
                    while self.dealer_value < 21 and self.player_value < 21 and player_stand == False:
                        choice = input("\n\nWould you Hit or Stand? H or S: \n")        # aasking to hit or stand
                        choice = choice.upper()
                        if choice == "H":               # hit
                            print("\n" * 50)
                            self.deal_player()          # deal card to player
                            self.print_single_dealer()
                            print("\n" * 2)
                            print("Current bet: " + str(self.bet))
                            print("\n" * 2)
                            self.print_all_player()
                        elif choice == "S":             # stand
                            print("\n" * 50)
                            self.print_all_dealer()     # recap hands of both
                            print("\n" * 2)
                            print("Current bet: " + str(self.bet))
                            print("\n" * 2)
                            self.print_all_player()
                            player_stand = True
                    while self.dealer_value < 17 and self.player_value < 21: # assuming no one has won yet, enter loop
                        print("\n" * 50)
                        self.deal_dealer()                                   # keep dealing to dealer until either bust or win
                        self.print_all_dealer()
                        print("\n" * 2)
                        print("Current bet: " + str(self.bet))
                        print("\n" * 2)
                        self.print_all_player()
                    self.check_bust()
                if self.balance > 0:                                        # assuming player still has money, enter
                    print("Here is how much you have: " + str(self.balance))
                    playon = input("\nWould you like to keep playing? Y or N: \n")  # asking player to play again
                    playon = playon.upper()
                    if playon == "Y":                                               # keep playing
                        self.clear()                # clear table
                        player_stand = False
                        play_on = True
                        self.initiate_new_game()    # start new game
                        print("\n" * 50)
                    else:                                                           # player wants tos top
                        print("\n" * 50)
                        print("Here is how much you have: " + str(self.balance))
                        print("\n\nThanks for playing. Please come again!\n\n")     # farewell message
                        play_on = False
                else:
                    print("Sorry, your current balance is 0. Come back with more money!\n\n")   # player is broke

game = Blackjack(1000)
game.initiate_game()
game.play_game()
