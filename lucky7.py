from deck import Deck
instructions = '''Learn how to play Lucky Seven! There are two players in this game, you and the computer. You will each have a hand of seven random cards.
Your goal is to put down a card you think is lower in value than your opponent. For example, if you have an 'A of Hearts' and your opponent has a
'K of Hearts' you win that round! The winner of that round gets a point and you deal a random card. Whoever gets to seven points first wins!
'''
player_score = 0
computer_score = 0
winning_score = 7

my_deck = Deck() #initialize deck
my_deck.shuffle() #shuffle deck
player_hand = my_deck.deal_card(7) #player deals 7 cards
computer_hand = my_deck.deal_card(7) #computer deals 7 cards
print(instructions)
print(player_hand)

def new_round():
    player_hand.remove(player_card) #player_card removed from player_hand
    player_hand.append(my_deck.deal_card(1)) #new card dealt and added to player_hand
    computer_hand.remove(computer_card) #computer_card removed from computer_hand
    computer_hand.append(my_deck.deal_card(1)) #new card dealth and added to computer_hand

while player_score < winning_score and computer_score < winning_score: #player score and computer score has to be lower than the winning score for the game to run
    print(f'Player score: {player_score} Computer score: {computer_score}') #Displays both players' scores
    player_selection = input('Select a card, number from 1 to 7: ') #Player selects a card to put down from their hand

    if player_selection == "quit" or player_selection == "q": #option to quit
        break
    elif player_selection == "restart" or player_selection == "r": #option to restart
        my_deck.reset() #resets the intiliazed deck
        print('Restarting...')
    elif int(player_selection) not in range(1,8): #if number chosen is not in the range
        print(f'Pick a valid card from {player_hand}')
    else:
        player_card = player_hand[int(player_selection)-1] #card position
        computer_card = min(computer_hand) #lowest value in the computer hand
        print(f'You played {player_card}')
        print(f'Computer plays {computer_card}')

        if player_card < computer_card: 
            player_score += 1 #player gets a point
            print('Player wins this round!')
            new_round()          
            print(f'You have {len(player_hand)} cards left: ', player_hand)

        elif player_card > computer_card:
            computer_score += 1 #computer gets a point
            print('Computer wins this round!')
            new_round()           
            print(f'You have {len(player_hand)} cards left: ', player_hand)

        elif player_card == computer_card:
            print("It's a tie!")
            new_round()
            print(f'You have {len(player_hand)} cards left: ', player_hand)
        
print(f'FINAL SCORES... Player wins: {player_score} Computer wins: {computer_score}')

