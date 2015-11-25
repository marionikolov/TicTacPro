from main import *
from logic import *

def offline2p(turn,images):
    """runs the offline 2 player iteration of the game"""
    screen=pygame.display.set_mode((610, 650))
    pygame.mixer.music.play(-1)
    screen.blit(images[0],(0,0))
    used=[7,8,9,4,5,6,1,2,3]
    pygame.display.flip()
    count=0
    isgamewon=(False,9)
    while count<9 and not isgamewon[0]:
        #every other time this ramdomises
        ev = pygame.event.get()
        for event in ev:
            if event.type == pygame.MOUSEBUTTONUP:
                pos = pygame.mouse.get_pos()
                valid=validmove(pos,used)
                if valid:
                    clicksound.play()
                    drawbox(turn,pos,used,images)
                    isgamewon=gamewon(used)
                    count+=1
                    if isgamewon[0]:
                        #(bool,"PLayer 2")
                        drawline(isgamewon[1],turn,images)
                        break
                    turn=not turn
                else:
                    nosound.play()
                    print("NO") 
            elif event.type == pygame.QUIT:
                quitgame()
    if isgamewon[0]:
        if turn:
            winner = "1"
            achievements("won")
        else:
            winner = "2"
            achievements("lost")
        print("The Winner is Player {0}!".format(winner))
    else:
        achievements("draw")
        losersound.play()
        print("No One Won!")
    pygame.mixer.music.fadeout(2000)
    time.sleep(2)
    
if __name__=="__main__":
    offline2p(True,images)
