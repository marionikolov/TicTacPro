"""
============================== TicTacPro ==============================
FILE: offline1p.py
MODIFIED: 07/12/2015
STATUS: Complete
FILE DESCRIPTION:
The offline1p.py file is the one-player state that uses AI for deciding where
the computer should play according to the game difficulty.
"""

from main import *
from logic import *
from achievements import *
from AI import *
import random, time

def offline1p(difficulty, turn, images):
    """
    FUNCTION NAME: offline1p
    PARAMETERS: 3
                difficulty (string; mandatory): determines the gameplay of the computer using AI; the allowed values are "easy", "medium", "hard"
                turn (boolean; mandatory): determines who makes the first move; if True, the user goes first; if False, the computer goes first
                images (list; mandatory): passes in the list of images used to depict the board; this list is determined by the style setting in the settings menu
    FUNCTION DESCRIPTION:
        This is the main function that runs the offline single-player state of the game.
        It begins by defining the game window, drawing the empty game board and playing
        the background music. It then runs the main loop which is responsible for giving
        turns to the two players, validating those moves and deciding whether the game
        has been won or not.
        For the computer's moves, the loop goes through a sequence of functions that decide
        the most appropriate move according to the difficulty level. Look at AI.py for more
        details.
    """
    screen=pygame.display.set_mode((610, 650))
    pygame.mixer.music.play(-1)
    screen.blit(images[0],(0,0))
    used=[7,8,9,4,5,6,1,2,3]    # Defines the list of squares used to hold the players' moves.
    pygame.display.flip()
    count=0 # Initiates a count of the moves made in this instance of the game.
    isgamewon=(False,9)
    while count<9 and not isgamewon[0]: # Main loop.
        ev = pygame.event.get()
        for event in ev:
            print("")   # If there is an old message in the status bar, remove it.
            if turn:    # User's move.
                if event.type == pygame.MOUSEBUTTONUP:
                    pos = pygame.mouse.get_pos()
                    clicksound.play()
                    valid=validmove(pos,used)
                    if valid:
                        drawbox(turn,pos,used,images)
                        isgamewon=gamewon(used)
                        count+=1
                        if isgamewon[0]:
                            drawline(isgamewon[1],turn,images)
                            break
                        turn=not turn
                    else:
                        print("That is not a valid move.")
                        nosound.play()
            elif not turn:  # Computer's move.
                if difficulty == "easy":
                    pos = AItakeRandom(used)

                elif difficulty == "medium":
                    pos = None
                    while pos is None:
                        pos = AIwinNext(used)
                        if pos is not None:
                            break
                        pos = AIblockNext(used)
                        if pos is not None:
                            break
                        pos = AItakeRandom(used)

                elif difficulty == "hard":
                    pos = None
                    while pos is None:
                        pos = AIwinNext(used)
                        if pos is not None:
                            break
                        pos = AIblockNext(used)
                        if pos is not None:
                            break
                        pos = AItakeCorner(used)
                        if pos is not None:
                            break
                        pos = AItakeCentre(used)
                        if pos is not None:
                            break
                        pos = AItakeRandom(used)
                        
                valid=validmove(pos,used)
                if valid:
                    clicksound.play()
                    drawbox(turn,pos,used,images)
                    isgamewon=gamewon(used)
                    count+=1
                    if isgamewon[0]:
                        drawline(isgamewon[1],turn,images)
                        break
                    turn=not turn
                else:
                    pass

            if event.type == pygame.QUIT:   # Allows closing the game window with the X button.
                quitgame()

    if isgamewon[0]:
        if turn:
            winner="1"
            print("The winner is Player {0}!".format(winner))
            time.sleep(2)
            achievements("won")
        else:
            winner="2"
            print("The winner is Player {0}!".format(winner))
            time.sleep(2)
            achievements("lost")
    else:
        losersound.play()
        print("The game is a draw!")
        time.sleep(2)
        achievements("draw")
    pygame.mixer.music.fadeout(2000)
    time.sleep(2)

if __name__=="__main__":
    offline1p("hard", True, images)
