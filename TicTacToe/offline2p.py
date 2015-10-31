from main import *
from logic import *

def offline2p():
    """runs the offline 2 player iteration of the game"""
    screen=pygame.display.set_mode((610, 650))
    pygame.mixer.music.play(-1)
    x=pygame.image.load('x.png')
    o=pygame.image.load('o.png')
    screen.blit(board,(0,0))
    used=[7,8,9,4,5,6,1,2,3]
    pygame.display.flip()
    turn=True
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
                    drawbox(o,x,turn,pos,used)
                    isgamewon=gamewon(used)
                    count+=1
                    if isgamewon[0]:
                        drawline(isgamewon[1],turn)
                        break
                    turn=not turn
                else:
                    nosound.play()
                    print("NO") 
            elif event.type == pygame.QUIT:
                quitgame()
    if isgamewon[0]:
        if turn: winner="1"
        else: winner="2"
        print("The Winner is Player {0}!".format(winner))
    else: losersound.play(),print("No One Won!")
    pygame.mixer.music.fadeout(2000)
    quitgame()
    
if __name__=="__main__":
    offline2p()
