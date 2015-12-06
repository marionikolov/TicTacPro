from main import *
from logic import *
import random

def askquestion():
    #possible questions
    #structure
    #0 - question
    #1 - answer 1
    #2 - answer 2
    #3+4 ""
    #5 - correct answer number
    questions = [
                    ["Who is now the American President?","Barrack Obama", "Sean Paul", "Michael Jordan", "Skepta", 1],
                    ["How many cheeks do you have?","2", "0", "3", "4", 1],
                    ["What goes up and never comes down?","Age", "Football", "Plane", "Rain", 1],
                    ["What is the square root of 144 equal?","12.5", "12", "1", "2", 2],
                    ["Who made Microsoft?","Bill Smith", "Bill Phil", "Bill Gates", "Bill Paul", 3],
                    ["What is half of 200?","150", "120", "100", "102", 3],
                    ["Which of the following is a soap (TV Programme)?","Power Rangers", "Eastenders", "BBC News", "MTV Base", 2],
                    ["How many legs does a spider have?","4", "6", "8", "10", 3],
                    ["What is the tallest animal in the world?","The giraffe", "Crocodile", "Bear", "Fox", 1]
                  ]
    #picks a random item from the list
    question = random.choice(questions)
    #removes last event
    pygame.event.clear()
    screen=pygame.display.set_mode((610, 650))
    questionmenu=pygame.image.load("images/menu/questionmenu.png")
    screen.blit(questionmenu,(0,0))
    #displays question + answers
    print(question[0],90,64)
    print(question[1],60,260)
    print(question[2],330,260)
    print(question[3],60,500)
    print(question[4],330,500)    
    q=False
    choice = 0
    while not q:
        pygame.display.flip()
        ev = pygame.event.get()
        for event in ev:
            if event.type == pygame.MOUSEBUTTONUP:
                pos = pygame.mouse.get_pos()
                #detect which option is chosen
                if pos[0] in range(28,280) and pos[1] in range(238,328):
                    choice=1
                elif pos[0] in range(308,558) and pos[1] in range(238,328):
                    choice=2
                elif pos[0] in range(28,280) and pos[1] in range(475,562):
                    choice=3
                elif pos[0] in range(308,558) and pos[1] in range(475,562):
                    choice=4
                if choice:
	                if choice==question[5]:
                            #if correct option is chosen then Bool1 is returned
	                    print("Correct! You go first!")
	                    time.sleep(2)
	                    return True
	                else:
                            #if correct option is not chosen then Bool2 is returned
	                    print("That's not correct! You go second.")
	                    time.sleep(2)
	                    return False

if __name__=="__main__":
    askquestion()
