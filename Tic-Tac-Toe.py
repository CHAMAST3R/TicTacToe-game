import random

def display_board(board):
    print("\n" * 100)
    
    print(board[7] + ' || '+board[8]+' || '+board[9])
    print('-----------')
    print(board[4] + ' || '+board[5]+' || '+board[6])
    print('-----------')
    print(board[1] + ' || '+board[2]+' || '+board[3])

    print('\n')

def player_input():
    marker = ""
    
    #Loop til the input meets conditions
    while marker !='X' and marker != 'O':
        #Ask for input
        marker=input('Player 1 please pick a marker: X or O: ').upper()
    
    #Store Player1 marker
    player1=marker
    
    #Assign resultant marker to Player2
    if player1 =='X':
        player2='O'
    else:
        player2='X'
    #Return the valiues as Tuple    
    return (player1,player2)

def place_marker(board, marker, position):
     board[position]=marker

def win_check(board, mark):
    return ((board[7]==mark and board[8]==mark and board[9]==mark) or
    (board[4]==mark and board[5]==mark and board[6]==mark) or
    (board[1]==mark and board[2]==mark and board[3]==mark) or
    (board[7]==mark and board[4]==mark and board[1]==mark) or
    (board[8]==mark and board[5]==mark and board[2]==mark) or
    (board[9]==mark and board[6]==mark and board[3]==mark) or
    (board[7]==mark and board[5]==mark and board[3]==mark) or
    (board[9]==mark and board[5]==mark and board[1]==mark))

def choose_first():
    player1=0
    player2=0
    
    while player1==player2:
        player1=random.randint(1,5)
        player2=random.randint(1,5)
    
    #print (player1,player2)
    
    if player1>player2:
        return'Player 1'
    else:
        return'Player 2'

def space_check(board, position):
    return board[position]==' '

def full_board_check(board):
    count=0
    
    for mk in board[1:10]:
        if mk==' ':
            count+=1
    if count ==0:
        #print('T')
        return True
    else:
        #print('F')
        return False

def player_choice(board):
    
    position=0
    #Take input and check if free 
    while position not in range(1,10) or not space_check(board,position):
        position=int(input('Please pick your position, choose from 1-9'))
    
    return position

def replay():
    
    play=str(input('Would you like to play again? (Y/N)')).upper()
    
    if play=='Y':
        return True
    else:
        False

#Main Code
print('Welcome to Tic Tac Toe!')

#while True:
while True:
    # Set the game up here
    
    #Create the board
    theBoard=[' ']*10
    
    player1_marker,player2_marker=player_input()
    turn=choose_first()
    print(turn+ ' will start first')
    
    play_game=str(input('Would you like to begin? (Y/N)')).upper()
    
    if play_game=='Y':
        game_on=True
    else:
        game_on=False
        break
    
   #while game_on:
    while game_on:
        if turn=='Player 1':
            
            #Player 1 Turn
            display_board(theBoard)
            position=player_choice(theBoard)
            place_marker(theBoard,player1_marker,position)
            display_board(theBoard)
            
             #Check win
            if win_check(theBoard,player1_marker):
                print('Player 1 has won!!')
                break
            else:
                turn='Player 2'
            
            #Check board full
            if full_board_check(theBoard):
                print('The board is full')
                print('The game is TIED')
                break
            
            
        else:
        # Player2's turn.
            display_board(theBoard)
            position=player_choice(theBoard)
            place_marker(theBoard,player2_marker,position)
            display_board(theBoard)
            
             #Check win
            if win_check(theBoard,player1_marker):
                print('Player 2 has won!!')
                break
            else:
                turn='Player 1'
            
            #Check board full
            if full_board_check(theBoard):
                print('The board is full')
                print('The game is TIED')
                break

    if not replay():
        break

