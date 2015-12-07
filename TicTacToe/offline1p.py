from main import *
from logic import *
from achievements import *
from AI import *
import random, time

def offline1p(difficulty, turn, images):
    """runs the offline 1 player iteration of the game"""
    screen=pygame.display.set_mode((610, 650))
    pygame.mixer.music.play(-1)
    screen.blit(images[0],(0,0))
    used=[7,8,9,4,5,6,1,2,3]
    pygame.display.flip()
    count=0
    isgamewon=(False,9)
    while count<9 and not isgamewon[0]:
        ev = pygame.event.get()
        for event in ev:
            print("") # If there is an old message in the status bar, remove it.
            if turn:
                # user move
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
                        print(used)
                    else:
                        print("That is not a valid move.")
                        nosound.play()
            elif not turn:
                # AI's move
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

            if event.type == pygame.QUIT:
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
    offline1p("hard",True,images)
