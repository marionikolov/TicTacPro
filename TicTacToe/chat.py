from main import *
from logic import *
screen=pygame.display.set_mode((900, 650))
def main():
    pygame.draw.rect(screen, (0,100,120), [610, 0, 300, 700], 0)
    chat=[]
    displaystring=""
    turn=True
    while True:
        ev = pygame.event.get()
        for event in ev:
            if event.type == pygame.QUIT:
                raise SystemExit
            elif event.type == pygame.KEYDOWN:
                if event.key in range(97,123) or event.key in range(48,58):
                    displaystring+=str(chr(event.key))
                #enter
                elif event.key == 13:
                    chat.insert(0,("You",displaystring))
                    displaystring=""
                    drawlist(chat)
                #space
                elif event.key == 32:
                    displaystring+=" "
                #backspace
                elif event.key == 8:
                    displaystring=displaystring[:-1]

                    showinput(displaystring)
                
def showinput(string):
    string=(": "+string)
    pygame.draw.rect(screen, (0,100,120), [610, 600, 300, 700], 0)
    font = pygame.font.Font(None, 16)
    text = font.render(string, 4, (255, 255, 255))
    screen.blit(text, (620,610))
    pygame.display.flip()
    
def drawlist(chat):
    y=540
    if len(chat)>14: del chat[-1]
    pygame.draw.rect(screen, (0,100,120), [610, 0, 300, 700], 0)
    for each in chat:
        each=(str(each[0]) +": " + str(each[1]))
        if len(each)<47:
            font = pygame.font.Font(None, 16)
            chatstuff = font.render(each, 4, (255, 255, 255))
            screen.blit(chatstuff, (620,y))
            y-=40
        else:s
            print("Too long can't display!")
        pygame.display.flip()
if __name__=="__main__":
    main()
    
