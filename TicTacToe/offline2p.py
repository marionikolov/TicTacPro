"""
============================== TicTacPro ==============================
FILE: Offline2p.py
MODIFIED: 15/11/2015
STATUS: Complete
FILE DESCRIPTION:
the Offline2p.py file is the 2 player offline state of the Tic Tac Toe game,
allowing 2 players to play against offline on a single system. 
"""

from main import *
from logic import *

def offline2p(images):
    """runs the offline 2 player iteration of the game"""
    #sets up the screen for running the offline2p gamemode
    screen=pygame.display.set_mode((610, 650))
    pygame.mixer.music.play(-1)
    screen.blit(images[0],(0,0))
    used=[7,8,9,4,5,6,1,2,3]
    pygame.display.flip()
    count=0
    turn = True
    isgamewon=(False,9)
    while count<9 and not isgamewon[0]:
        if turn:
            print("It is Player 1's turn.")
        else:
            print("It is Player 2's turn.")
        ev = pygame.event.get()
        for event in ev:
            #checks where you click
            if event.type == pygame.MOUSEBUTTONUP:
                pos = pygame.mouse.get_pos()
                valid=validmove(pos,used)
                if valid:
                    #if the input is in a valid position then it will run this code
                    clicksound.play()
                    drawbox(turn,pos,used,images)
                    isgamewon=gamewon(used)
                    count+=1
                    #isgamewon is a tuple (bool,string of "player 1" or 2"
                    if isgamewon[0]:
                        drawline(isgamewon[1],turn,images)
                        break
                    turn=not turn
                else:
                    nosound.play()
                    print("That is not a valid move.") 
            elif event.type == pygame.QUIT:
                quitgame()
    #this runs when the game is over, either the max number of moves have happened
    #or someone has won
    if isgamewon[0]:
        #works out who won, runs the corresponding code
        if turn:
            winner = "1"
            print("The winner is Player {0}!".format(winner))
        else:
            winner = "2"
            print("The winner is Player {0}!".format(winner))
    else:
        losersound.play()
        print("The game is a draw!")
        time.sleep(2)
        achievements("draw")
    pygame.mixer.music.fadeout(2000)
    time.sleep(2)
    
if __name__=="__main__":
    offline2p(images)
