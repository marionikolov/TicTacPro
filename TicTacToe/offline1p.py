from main import *
from logic import *
import random

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
                    else:
                        print("That is not a valid move.")
                        nosound.play()
            elif not turn:
                # AI's move
                if difficulty == "easy":
                    pos = (random.randint(10,600), random.randint(10,600))
                elif difficulty == "medium":
                    #add code here, V
                    print("medium")
                elif difficulty == "hard":
                    #add code here, V
                print("hard")
                valid=validmove(pos,used)
                time.sleep(0.5)
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
    if isgamewon:
        if turn: winner="1"
        else: winner="2"
        print("The Winner is Player {0}!".format(winner)) 
    else: losersound.play(),print("No One Won!")
    pygame.mixer.music.fadeout(2000)
    time.sleep(2)
    

if __name__=="__main__":
    offline1p("easy",True,images)
