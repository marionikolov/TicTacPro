from main import *

#0-board
#1-x
#2-o
#3-xwin
#4-owin

def print(text):
    """changes the print function to now print to the gui 'status bar' """
    pygame.draw.rect(screen, (0,0,0), (10,610,600,40), 0)
    font = pygame.font.Font(None, 32)
    textg = font.render(str(text), 4, (255, 255, 255))
    screen.blit(textg, (40,610))
    pygame.display.flip()
#normal images

def settingmenu():
    settingsmenu=pygame.image.load("images/menu/settings/settingsmenu.png")
    
    q=False
    while not q:
        screen.blit(settingsmenu,(0,0))
        pygame.display.flip()
        ev = pygame.event.get()
        for event in ev:
            if event.type == pygame.MOUSEBUTTONUP:
                pos = pygame.mouse.get_pos()
                if pos[0] in range(30,200) and pos[1] in range(160,300):
                    images=stylemenu()
                elif pos[0] in range(400,600) and pos[1] in range(160,300):
                    songmenu()
                elif pos[0] in range(23,204) and pos[1] in range(540,600):
                    try:
                        return images
                    except:
                        return None

def songmenu():
    songmenu=pygame.image.load("images/menu/settings/songmenu.png")
    screen.blit(songmenu,(0,0))
    pygame.display.flip()
    q=False
    while not q:
        ev = pygame.event.get()
        for event in ev:
            if event.type == pygame.MOUSEBUTTONUP:
                pos = pygame.mouse.get_pos()
        
                if pos[0] in range(30,200) and pos[1] in range(160,300):
                    print("Music Changed - Harder!")
                    pygame.mixer.music.load("music/harder.mp3")
                elif pos[0] in range(400,600) and pos[1] in range(160,300):
                    print("Music Changed - Lucky!")
                    pygame.mixer.music.load("music/lucky.mp3")
                elif pos[0] in range(30,200) and pos[1] in range(370,510):
                    print("Music Changed - Nostalgia!")
                    pygame.mixer.music.load("music/oldschool.mp3")
                elif pos[0] in range(400,600) and pos[1] in range(370,510):
                    print("Music Changed - Oh, Christmas Tree!")
                    pygame.mixer.music.load("music/christmas.mp3")
                elif pos[0] in range(23,204) and pos[1] in range(540,600): # Back button.
                    q=True
def stylemenu():
    stylesmenu=pygame.image.load("images/menu/settings/stylemenu.png")
    screen.blit(stylesmenu,(0,0))
    pygame.display.flip()
    q=False
    while not q:
        ev = pygame.event.get()
        for event in ev:
            if event.type == pygame.MOUSEBUTTONUP:
                pos = pygame.mouse.get_pos()
            #top left button
                
                if pos[0] in range(30,200) and pos[1] in range(160,300):
                    print("Board Loaded - Classic Board")
                    images=[
                    pygame.image.load("images/classic/board.png"),
                    pygame.image.load('images/classic/x.png'),
                    pygame.image.load('images/classic/o.png'),
                    pygame.image.load("images/classic/xwon.png"),
                    pygame.image.load("images/classic/owin.png")
                    ]
             
                elif pos[0] in range(400,600) and pos[1] in range(160,300):
                    print("Board Loaded - Test Board")
                    images=[
                    pygame.image.load("images/test/board.png"),
                    pygame.image.load('images/test/x.png'),
                    pygame.image.load('images/test/o.png'),
                    pygame.image.load("images/test/xwon.png"),
                    pygame.image.load("images/test/owin.png")
                    ]
                    
                elif pos[0] in range(30,200) and pos[1] in range(370,510):
                    print("Board Loaded - Christmas")
                    images=[
                    pygame.image.load("images/christmas/board.png"),
                    pygame.image.load('images/christmas/x.png'),
                    pygame.image.load('images/christmas/o.png'),
                    pygame.image.load("images/christmas/xwon.png"),
                    pygame.image.load("images/christmas/owin.png")
                    ]
                    
                elif pos[0] in range(400,600) and pos[1] in range(370,510):
                    print("Board Loaded - Mushroom")
                    images=[
                    pygame.image.load("images/mushroom/board.png"),
                    pygame.image.load('images/mushroom/x.png'),
                    pygame.image.load('images/mushroom/o.png'),
                    pygame.image.load("images/mushroom/xwon.png"),
                    pygame.image.load("images/mushroom/owin.png")
                    ]
                    
                elif pos[0] in range(23,204) and pos[1] in range(540,600):
                    try:
                        return images
                    except:
                        return None
                                   
if __name__=="__main__":
    settingmenu()
