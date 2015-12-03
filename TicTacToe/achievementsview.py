from main import *
from logic import *
import pickle

def achievementsview():
    pygame.event.clear()
    screen=pygame.display.set_mode((610, 650))
    achievementsmenu=pygame.image.load("images/menu/settings/achievementsmenu.png")
    screen.blit(achievementsmenu,(0,0))

    f = open("achievements.pickle","rb")
    stats = pickle.load(f)
    f.close()

    print("Games played ...................................... " + str(stats[0]),70,140)
    print("Games won .......................................... " + str(stats[1]),70,200)
    print("Games lost ........................................... " + str(stats[2]),70,260)
    print("Games drawn ...................................... " + str(stats[3]),70,320)
    print("You are level " + str(stats[4]),200,380)

    q=False
    while not q:  
        pygame.display.flip()
        ev = pygame.event.get()
        for event in ev:
            if event.type == pygame.MOUSEBUTTONUP:
                pos = pygame.mouse.get_pos()
                if pos[0] in range(23,204) and pos[1] in range(540,600):
                    try:
                        return images
                    except:
                        return None

if __name__ == "__main__":
    achievementsview()
