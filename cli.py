"""
-------------Intial File--------------

This is a file built by Jiminy Haynes before finalising the plan for the
TicTacToe game, it is a line based GUI and was made to test concepts
and understand the game mechanics better
"""

import time
import msvcrt
import os
os.system("mode con cols=50 lines=28")
def draw_board(box):
    print("-"*49)
    for count2 in range(0,3):
        for count in range(0,7):
            print("|{0}|{1}|{2}|".format(box[count2][0][count],box[count2][1][count],box[count2][2][count]))        
        print("-"*49)
        
def generate_X():
    x0=(" x           x ")
    x1=("   x       x   ")
    x2=("     x   x     ")
    x3=("       x       ")
    x4=("     x   x     ")
    x5=("   x       x   ") 
    x6=(" x           x ")
    x=[x0,x1,x2,x3,x4,x5,x6]
    return x

def generate_O():
    o0=("       x       ")
    o1=("     x   x     ")
    o2=("   x       x   ")
    o3=(" x           x ")
    o4=("   x       x   ")
    o5=("     x   x     ") 
    o6=("       x       ")
    o=[o0,o1,o2,o3,o4,o5,o6]
    return o

def generate_B():
    b0=("               ")
    b1=("               ")
    b2=("               ")
    b3=("               ")
    b4=("               ")
    b5=("               ") 
    b6=("               ")
    b=[b0,b1,b2,b3,b4,b5,b6]
    return b
box_x=generate_X()
box_o=generate_O()
box_b=generate_B()

def generate_board(board,command):
    
    #command 0 = player
    #command 1 = y axis
    #command 2 = x axis
    
    if command[0]=="x":
        board[command[1]][command[2]]=box_x
    elif command[0]=="o":
        board[command[1]][command[2]]=box_o
    draw_board(board)
    
def intial_generate_board():
    line1=[box_b,box_b,box_b]
    line2=[box_b,box_b,box_b]
    line3=[box_b,box_b,box_b]
    
    board=[line1,line2,line3]
    draw_board(board)
    return board


def get_user_move():
    valid=False
    while not valid:
        try:
            #user_move=int(input())
            user_move=int(msvcrt.getch())
            if user_move==7:
                move="a1"
            elif user_move==8:
                move="a2"
            elif user_move==9:
                move="a3"
            elif user_move==4:
                move="b1"
            elif user_move==5:
                move="b2"
            elif user_move==6:
                move="b3"
            elif user_move==1:
                move="c1"
            elif user_move==2:
                move="c2"
            elif user_move==3:
                move="c3"
            valid=True
        except ValueError:
            print("That's not a valid input!")
    return move

def generate_command(board,countplayer):
    while countplayer!=0:
        if countplayer//2==countplayer/2:
            print("Player Two (X)!")
            player="x"
        else:
            print("Player One (O)!")
            player="o"
        countplayer-=1
        valid=False
        while not valid:
            coord=get_user_move()
            
            if coord[0].lower()=="a":
                yaxis=0
            elif coord[0].lower()=="b":
                yaxis=1
            elif coord[0]=="c":
                yaxis=2
            else:
                print("FAIL")
            command=(player,yaxis,(int(coord[1])-1))
            valid=True        
            if board[command[1]][command[2]][0]!=("               "):
                print("That is not a valid move!")
                valid=False
        return command,countplayer

def generate_combos():
    combo1=["00","01","02"]
    combo2=["00","10","20"]
    combo3=["02","12","22"]
    combo4=["20","21","22"]
    combo5=["01","11","21"]
    combo6=["10","11","12"]
    combo7=["00","11","22"]
    combo8=["02","11","20"]
    combos=[combo1,combo2,combo3,combo4,combo5,combo6,combo7,combo8]
    return combos

def game_won(gamewon,combos,board):
    for count in range(0,8):
        
        if (
            board [int(combos[count][0][0])] [int(combos[count][0][1])] [0] == board [int(combos[count][1][0])] [int(combos[count][1][1])] [0] and
            board [int(combos[count][1][0])] [int(combos[count][1][1])] [0] == board [int(combos[count][2][0])] [int(combos[count][2][1])] [0] and
            board [int(combos[count][2][0])] [int(combos[count][2][1])] [0] == (" x           x ")):            

                gamewon=("Player 2",True)
            
        elif(
            board [int(combos[count][0][0])] [int(combos[count][0][1])] [0] == board [int(combos[count][1][0])] [int(combos[count][1][1])] [0] and
            board [int(combos[count][1][0])] [int(combos[count][1][1])] [0] == board [int(combos[count][2][0])] [int(combos[count][2][1])] [0] and
            board [int(combos[count][2][0])] [int(combos[count][2][1])] [0] == ("       x       ")):

                gamewon=("Player 1",True)
    
    return gamewon
def winstate(gamewon,board):
    draw_board(board)
    q=True
    print()
    print("{0} Has won!".format(gamewon[0]))
    time.sleep(3)
    return q

def losestate(board):
    draw_board(board)
    print()
    print("No one won!")
    time.sleep(3)
    q=True
    return q

def main():
    q=False
    countplayer=9
    combos=generate_combos()
    gamewon=("No One",False)
    board=intial_generate_board()
    print("Welcome to Tic Tac Pro!")
    while not q:
        if countplayer!=0:
            command,countplayer=generate_command(board,countplayer)
            generate_board(board,command)
            gamewon=game_won(gamewon,combos,board)
            print()
            if gamewon[1]==True:
                q=winstate(gamewon,board)
                
        else:
            gamewon=game_won(gamewon,combos,board)
            if gamewon[1]==True:
                q=winstate(gamewon,board)
            else:
                q=losestate(board)
    print("Thanks for playing!")
    time.sleep(3)
main()
