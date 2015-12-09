"""
============================== TicTacPro ==============================
FILE: firstgo.py
MODIFIED: 07/12/2015
STATUS: Complete
FILE DESCRIPTION:
	The firstgo.py file is used for deciding who the first person to make a move
	is by asking an educational question. It is used only for offline single-player
	games and online games.
"""

from main import *
from logic import *
import random

def askquestion():
    questions = [
["Who is now the American President?","Barrack Obama", "Sean Paul", "Michael Jordan", "Skepta", 1],
["How many cheeks do you have?","2", "0", "3", "4", 4],
["What goes up and never comes down?","Age", "Football", "Plane", "Rain", 1],
["What is the square root of 144 equal?","12.5", "12", "1", "2", 2],
["Who made Microsoft?","Bill Smith", "Bill Phil", "Bill Gates", "Bill Paul", 3],
["What is half of 200?","150", "120", "100", "102", 3],
["Which of the following is a soap (TV Programme)?","Power Rangers", "Eastenders", "BBC News", "MTV Base", 2],
["How many legs does a spider have?","4", "6", "8", "10", 3],
["What is the tallest animal in the world?","The giraffe", "Crocodile", "Bear", "Fox", 1]
                  ]	# Structure of list: 0 - question, 1 - option 1, 2 - option 2, 3 - option 3, 4 - option 4, 5 - index of correct answer
    question = random.choice(questions)
    pygame.event.clear()	# Remove all events in list. Prevents conflicts.
    screen=pygame.display.set_mode((610, 650))
    questionmenu=pygame.image.load("images/menu/questionmenu.png")
    screen.blit(questionmenu,(0,0))
    print(question[0],80,100)	# Display question.
    print(question[1],100,300)	# Display answers.
    print(question[2],350,300)
    print(question[3],110,440)
    print(question[4],350,440)    
    q=False
    choice = 0
    while not q:
        pygame.display.flip()
        ev = pygame.event.get()
        for event in ev:
            if event.type == pygame.MOUSEBUTTONUP:
                
                pos = pygame.mouse.get_pos()
                
                if pos[0] in range(85,275) and pos[1] in range(275,365):	# Detect which answer is selected.
                    choice=1
                    
                elif pos[0] in range(335,275) and pos[1] in range(525,365):
                    choice=2
                    
                elif pos[0] in range(85,410) and pos[1] in range(275,500):
                    choice=3
                    
                elif pos[0] in range(308,410) and pos[1] in range(525,500):
                    choice=4
                    
                if choice:
	                if choice==question[5]:	# Compare the user's answer to the correct answer.
	                    print("Correct! You go first!")
	                    time.sleep(2)
	                    return True
	                else:
	                    print("That's not correct! You go second.")
	                    time.sleep(2)
	                    return False
            elif event.type == pygame.QUIT:
                quitgame() 
                
if __name__=="__main__":
    askquestion()
