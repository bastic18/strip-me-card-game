# Creator: Garfield Grant       
# Creator: Horraine Mccalla     
# COMP1127 project
# Main file for the project


import sys
import cards
from random import randrange
import adt_







def showGreeting():         # This function shows the main menu for the game 
    print ("*************************************************************")
    print ("*            WELCOME to Strip ME                            *")
    print ("*                                                           *")
    print ("*Rules of the game: Check the docs                          *")
    print ("*                                                           *")
    print ("*Game Play:                                                 *")
    print ("*-player 0: the computer                                    *")
    print ("*-player 1: you                                             *")
    print ("*-enter: play the top card and place on discard pile        *")
    print ("*-q: quit i.e stop playing the game                         *")
    print ("*                                                           *")
    print ("*                                                           *")
    print ("*                   Enjoy!!!!!!                             *")
    print ("*************************************************************")






# This is a dictionary containing pay cards
paycards= { "A":4,"K": 3, "Q": 2, "J":1}

# This function checks too see if a card is a paycard or not
def isPayCard(card):
    
    if card[1] in paycards:     # checks if a card is in the dictionary of paycards 
        return True
    else:
        return False


# This function get the rate of the paycard by accessing the paycards dictionary
def getCardRate(card):
    
    if isPayCard(card):             # if the card enter is a paycard it returns the corresponding rate of payment
        return paycards[card[1]]
    else:
        return 0


# This function place cards into a queue data structure
def fillHand(hand, cards):
    for each_card in cards:             # Adds each cards to a player add one at a time
        adt_.enqueue(hand,each_card)
    return hand


# This functions creates a deck and shuffles the card into two queues. Creating two pair of hands player 0 and player 1
def prepPlayers():
    deck= cards.new_Deck()
    deck= cards.shuffle(randrange(20,40),deck)          # call functions from the cards module to create and shuffle a new deck of cards


    deal_with_decks= cards.deal(deck,26,2)

    players_cards= deal_with_decks[0]
    players=[]
    for player_cards in players_cards:
        h1= fillHand(adt_.new_Queue(),player_cards)
        players.append(h1)                          # Adds the element to the back of the player queue data structure

    return players


#Takes card out of the queue, which is the players hand and places it in the discard pile
def placeCard(hand,pile):

    card= adt_.queue_Front(hand)
    adt_.dequeue(hand)
    adt_.push(pile,card)
    return (hand,pile)

        
        
def dpile():
    return adt_.stack_Contents(placeCard(hand,adt_.new_Stack()))



# This function display the card that was played, then update the player's hand and discard pile    
def playCard(current_player, hand, pile):
    
    
    x= print ("Player", current_player)
    

    played_card = placeCard(hand,pile)

    playcard_symbol=adt_.stack_Contents(played_card[1])[0][0]
    playcard_symbol2=adt_.stack_Contents(played_card[1])[0][1]
    playcard_symbol1=cards.getSuitIcon(playcard_symbol)
    print("played the", playcard_symbol1,playcard_symbol2)






#This function allows players to succesfully accept payment, add the cards to their queue(hand)
def takePayment(hand,pile):
    while not adt_.empty_Stack(pile):
        adt_.enqueue(hand, adt_.stack_Top(pile))
        adt_.pop(pile)

    return hand, pile




# Creates the game play. Use all the functions created earlier.

"""  
def strip_me():
    showGreeting()
    players=prepPlayers()

    player0=players[0]
    player1=players[1]
    discardpile= adt_.new_Stack()
    
    

    
    print ("Checking to see if you are human: Press Enter")
    ans= input ()
    while not ans== 'q':
        print ("Play (Enter); quit (q, then enter)")
        ans= input ()
        if ans=='q':
            print ( "You quit the game before it ended, so there is no result,bye")
        else:
            if  adt_.empty_Queue(player0)== True      :
                print( "player 1 winner" )
        
                break
            elif  adt_.empty_Queue(player1)== True :
                print( "Player 0 winner")
                break

            else:
                amount1, amount2,turn=0,0,0
                if turn==0:
                    while not turn==1:
                        playCard(1,player1,discardpile)
                        h1=isPayCard(adt_.stack_Top(discardpile))
                        amount1=getCardRate(adt_.stack_Top(discardpile))
                        if h1== False:
                            turn= 1
                        else:
                            while not amount1==0:
                                if amount1==4:
                                    playCard(0,player0,discardpile)
                                    
                                    amount2=getCardRate(adt_.stack_Top(discardpile))
                                    if amount2>0:
                                        turn =0
                                        break
                                    amount1 = amount1 - 1
                                    
                                if amount1==3:
                                    playCard(0,player0,discardpile)
                                    
                                    amount2=getCardRate(adt_.stack_Top(discardpile))
                                    if amount2>0:
                                        turn =0
                                        break
                                    amount1 = amount1 - 1
                                if amount1==2:
                                    playCard(0,player0,discardpile)
                                    
                                    amount2=getCardRate(adt_.stack_Top(discardpile))
                                    if amount2>0:
                                        turn =0
                                        break
                                    amount1 = amount1 - 1
                                if amount1==1:
                                    playCard(0,player0,discardpile)
                                    
                                    amount2=getCardRate(adt_.stack_Top(discardpile))
                                    if amount2>0:
                                        turn =0
                                        break
                                    amount1 = amount1 - 1
                                    
                                takePayment(player1,discardpile)
                                
                                print ("The full payment was made. Player 1 claimed the discard pile")
                                turn==0
                      
                    

                if turn ==1:
                    while not turn==0:
                        playCard(0,player0,discardpile)
                        h2=isPayCard(adt_.stack_Top(discardpile))
                        amount2=getCardRate(adt_.stack_Top(discardpile))
                        if h2== False:
                            turn= 0
                        else:
                            while not amount2==0:
                                if amount2==4:
                                    playCard(1,player1,discardpile)
                                    
                                    amount1=getCardRate(adt_.stack_Top(discardpile))
                                    if amount1>0:
                                        turn =0
                                        break
                                    amount2 = amount2 - 1
                                if amount2==3:
                                    playCard(1,player1,discardpile)
                                    
                                    amount1=getCardRate(adt_.stack_Top(discardpile))
                                    if amount1>0:
                                        turn =0
                                        break
                                    amount2 = amount2 - 1
                                if amount2==2:
                                    playCard(1,player1,discardpile)
                                    
                                    amount1=getCardRate(adt_.stack_Top(discardpile))
                                    if amount1>0:
                                        turn =0
                                        break
                                    amount2 = amount2 - 1
                                if amount2==1:
                                    playCard(1,player1,discardpile)
                                    
                                    amount1=getCardRate(adt_.stack_Top(discardpile))
                                    if amount1>0:
                                        turn =0
                                        break
                                    amount2 = amount2 - 1
                            
                                takePayment(player0,discardpile)
                                
                                print( "The full payment was made. Player 0 claimed the discard pile")

                                turn=1


            
# This function begins game play               
strip_me()                

"""
def strip_me():
    showGreeting()
    playershand=prepPlayers()
    discardpile= adt_.new_Stack()
    who_to_play=1

    def prompt():
        print ("Play (Enter); quit (q, then enter)")

    def quitprompt():
        print ( "You quit the game before it ended, so there is no result,bye")

    def playgame(current_player, will_paying):
        card_in_hand= playershand[current_player] # creates a hand of cards for the players


        if  adt_.empty_Queue(card_in_hand) and current_player==  1:  # base case where it checks if the players hands which are queue data structure is empty, then it returns the winner 
                print( "player 0 winner" )
                sys.exit(0)
        
        elif  adt_.empty_Queue(card_in_hand) and current_player == 0 : # base case where it checks if the players hands which are queue data structure is empty, then it returns the winner
                print( "Player 1 winner")
                sys.exit(0)             # exit the code using the system module 
        playCard(current_player,card_in_hand,discardpile)       # A  card is played using this function. The first card is played here 
        playedcard= adt_.stack_Top(discardpile) # gets the card at the top of the discardpile

        if isPayCard(playedcard):           
            value=getCardRate(playedcard)

            for x in range(value):          # using the rate of the card, makes the other player pay accordingly, however if the player plays a paycard it switches again 
                if current_player==1:
                    next_payingplayer=0
                else:
                    next_payingplayer=1
                    
                outcome=playgame(next_payingplayer, True )
                if outcome:
                    return True

            takePayment(card_in_hand,discardpile)           # the person that wins the round collect the cards in the discardpile 
            print ("The full payment was made. Player",current_player,"claimed the discard pile")
        

            if current_player==1:
    
                prompt()        # prompt the user before he plays to quit the game or continue
                ans= input()
                if ans=='q':
                    quitprompt()             # prompt the user that he or she as quit the game
                    sys.exit(0)
            playgame(current_player,False)          # recursively calls back the current_player so that players start to play again after payments have been made by a player

            
        elif will_paying:
            return False
        else:
            if current_player==1:               # This code also intercahnge which player plays acoording to the card play and who collected the discardpile
                future_player=0
            else:
                future_player=1
                prompt()                    # prompt the user before he plays to quit the game or continue
                ans= input()
                if ans=='q':
                    quitprompt()     # prompt the user that he or she as quit the game
                    sys.exit(0)
            playgame(future_player,False)

    prompt()# prompt the user before he plays to quit the game or continue
    ans= input()

    if ans== 'q':
        quitprompt()             # prompt the user that he or she as quit the game
    else:
        playgame(who_to_play, False)





strip_me()

                



