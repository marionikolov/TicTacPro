from main import *
from logic import *
import random

def askquestion():
    questions = [["Whats 1+1?","2","6","59","3",1]]
    question = random.choice(questions)
    screen=pygame.display.set_mode((610, 650))
    questionmenu=pygame.image.load("images/menu/questionmenu.png")
    screen.blit(questionmenu,(0,0))
    print(question[0],90,64)
    print(question[1],60,260)
    print(question[2],330,260)
    print(question[3],60,500)
    print(question[4],330,500)    
    q=False
    while not q:
        pygame.display.flip()
        ev = pygame.event.get()
        for event in ev:
            if event.type == pygame.MOUSEBUTTONUP:
                pos = pygame.mouse.get_pos()
                if pos[0] in range(28,280) and pos[1] in range(238,328):
                    choice=1
                elif pos[0] in range(308,558) and pos[1] in range(238,328):
                    choice=2
                elif pos[0] in range(28,280) and pos[1] in range(475,562):
                    choice=3
                elif pos[0] in range(308,558) and pos[1] in range(475,562):
                    choice=4
                if choice==question[5]:
                    print("Correct! You go first!")
                    time.sleep(2)
                    return True
                else:
                    print("That's not correct! You go second.")
                    time.sleep(2)
                    return False

if __name__=="__main__":
    askquestion()
