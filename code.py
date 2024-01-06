import random
import os
import time

#making the game boards

#initializing required variables
NUM_ROWS = 5
NUM_COLS = 5
NUM_PLAYERS=2
visible_board = []
hidden_board=[]

turn=random.randint(0,NUM_PLAYERS-1)
player1_score=0
player2_score=0
game_over=False


#making the visible board that the players can see
for row in range(NUM_ROWS):
    row_list = []
    for col in range(NUM_COLS):
        row_list.append('#')
    visible_board.append(row_list)


#making hidden board that holds the actual cards and jokers
current_letter=ord('A')
num_squares=NUM_COLS*NUM_ROWS
cards=[]

for i in range(num_squares//2):
    if i==(num_squares//2)-1:
            cards.append('*')
            cards.append('*')
            break
    cards.append(chr(current_letter))
    cards.append(chr(current_letter).lower())
    current_letter+=1
    
if num_squares%2!=0:
    cards.append('*')


for row in range(NUM_ROWS):
    card_list = []
    for col in range(NUM_COLS):
        card_list.append('#')
    hidden_board.append(card_list)

for card in cards:
    while True:
        rand_index1=random.randint(0,len(hidden_board)-1)
        card_list = hidden_board[rand_index1]
        rand_index2=random.randint(0,len(card_list)-1)
        if hidden_board[rand_index1][rand_index2]=='#':
            hidden_board[rand_index1][rand_index2]=card
            break


while game_over==False:
    print('Player 1 score: ', player1_score)
    print('Player 2 score: ', player2_score)

    #printing the board in its initial stage
    letter=ord('A')
    for cols in range(NUM_COLS):
        print('   ' + chr(letter), end='')
        letter+=1
    print("\n +" + "---+" * NUM_COLS)

    for row in range(NUM_ROWS):
        print(str(row) + '|', end=' ')
        for col in range(NUM_COLS):
            print(visible_board[row][col] + ' | ', end='')
        print("\n +"+"---+"*NUM_COLS)

    
    #asking the player to input a coordinate and checking its validity
    while True:
        coordinate=input('Player '+str(turn+1)+': Enter a coordinate (e.g. B3): ' )
        if len(coordinate)==2:
            if ord(coordinate[0]) in range(ord('A'),letter) and int(coordinate[1]) in range(NUM_ROWS):
                #checking what card the player turned over
                row_index1=0
                col_index1=0
                for c in range(ord('A'),letter):
                    if c==ord(coordinate[0]):
                        break
                    col_index1+=1

                for r in range(NUM_ROWS):
                    if r==int(coordinate[1]):
                        break
                    row_index1+=1

                #checking whether the card has already been turned over
                if visible_board[row_index1][col_index1] == ' ':
                    print('This card has already been turned over. Please enter another coordinate.')
                else:
                    card1 = hidden_board[row_index1][col_index1]
                    visible_board[row_index1][col_index1] = card1
                    break
            else:
                print('Invalid coordinate entered. Please try again')
        else:
            print('Invalid coordinate entered. Please try again')

    #printing the board for the player to see
    letter=ord('A')
    for cols in range(NUM_COLS):
        print('   ' + chr(letter), end='')
        letter+=1

    print("\n +" + "---+" * NUM_COLS)

    for row in range(NUM_ROWS):
        print(str(row) + '|', end=' ')
        for col in range(NUM_COLS):
            print(visible_board[row][col] + ' | ', end='')
        print("\n +"+"---+"*NUM_COLS)

    
    #asking user to input coordinates of second card and checking its validity
    while True:
        new_coordinate=input('Player '+str(turn+1)+': Enter another coordinate: ' )
        if len(new_coordinate)==2:
            if ord(new_coordinate[0]) in range(ord('A'),letter) and int(new_coordinate[1]) in range(NUM_ROWS):
                row_index2=0
                col_index2=0

                for c in range(ord('A'),letter):
                    if c==ord(new_coordinate[0]):
                        break
                    col_index2+=1

                for r in range(NUM_ROWS):
                    if r==int(new_coordinate[1]):
                        break
                    row_index2+=1  

                #checking whether the card has already been turned over
                if visible_board[row_index2][col_index2] == ' ':
                    print('This card has already been turned over. Please enter another coordinate.')
                #checking whether the card was turned over in the previous turn    
                elif hidden_board[row_index2][col_index2]==card1:
                    print('You have already turned this card over in the previous turn. Please try again.')
                else:
                    card2 = hidden_board[row_index2][col_index2]
                    visible_board[row_index2][col_index2] = card2
                    break
            else:
                print('Invalid coordinate entered. Please try again')
        else:
            print('Invalid coordinate entered. Please try again')


    #checking what combination the 2 cards form and incrementing the scores accordingly

    #if both cards are jokers
    if card1=='*' and card2=='*':
        visible_board[row_index1][col_index1]=' '
        visible_board[row_index2][col_index2]=' '      
        if turn+1==1:
            player1_score+=1
        else:
            player2_score+=1

    #if one of the cards is a joker
    elif card1=='*' or card2=='*':
        for row in range(NUM_ROWS):
            for col in range(NUM_COLS): 
                if card1.isupper() and hidden_board[row][col].upper()==card1:
                    visible_board[row][col]=' '
                elif card1.islower() and hidden_board[row][col].lower()==card1:
                    visible_board[row][col]=' '
                elif card2.isupper() and hidden_board[row][col].upper()==card2:
                    visible_board[row][col]=' '
                elif card2.islower() and hidden_board[row][col].lower()==card2:
                    visible_board[row][col]=' '
                else:
                    pass
            visible_board[row_index1][col_index1]=' '
            visible_board[row_index2][col_index2]=' '
        if turn+1==1:
            player1_score+=2
        else:
            player2_score+=2

    #if none of the cards are jokers but both cards form a twin
    elif card1.upper()==card2 or card2.upper()==card1:
        visible_board[row_index1][col_index1]=' '
        visible_board[row_index2][col_index2]=' '
        if turn+1==1:
            player1_score+=1
        else:
            player2_score+=1

    #if no twin is formed
    else:
        letter=ord('A')
        for cols in range(NUM_COLS):
            print('   ' + chr(letter), end='')
            letter+=1

        print("\n +" + "---+" * NUM_COLS)

        for row in range(NUM_ROWS):
            print(str(row) + '|', end=' ')
            for col in range(NUM_COLS):
                print(visible_board[row][col] + ' | ', end='')
            print("\n +"+"---+"*NUM_COLS)

        time.sleep(2) # pause the program for 2 seconds

        #turning cards face down again
        for row in range(NUM_ROWS):
            for col in range(NUM_COLS):
                if visible_board[row][col]!=' ':
                    visible_board[row][col]='#'

        os.system("clear") # clears the screen
        turn=(turn+1)%2 #updating the turn variable to indicate that it is the next player's turn   

    #checking if more turns are possible  
    finished=True
    for row in range(NUM_ROWS):
        for col in range(NUM_COLS):
            if visible_board[row][col]!=' ':
                finished=False
                break
    if finished==True:
        print('GAME OVER')
        if player1_score>player2_score:
            print('Player 1 wins!')
        elif player2_score>player1_score:
            print('Player 2 wins!')
        else:
            print('Both players have equal scores.')

        print('Player 1 score:', player1_score)
        print('Player 2 score:', player2_score)
        game_over=True
