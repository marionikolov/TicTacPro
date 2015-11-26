from main import *
from logic import *
import pickle
global number_of_games
global games_won
global games_lost
global games_draw
global reputation
number_of_games=0
games_won=0
games_lost=0
game_draw=0
reputation=0
def achievements(res):
    achievements = {1:"Congratulations on your win. You are lever 1!", 2:"You are level 2"}
    pickle_out = open("doc.pickle","wb")
    pickle.dump(achievements, pickle_out)
    pickle_out.close()
    
    if res == "won":
        global number_of_games
        number_of_games = int(number_of_games) + 1
        global games_won
        games_won = int(games_won) + 1
        global reputation
        reputation = int(reputation) + 1
        print(achievements[int(reputation)])
        print("Your game/ratio is " + str(number_of_games))
    elif res == "lost":
        if number_of_games >0 :
            global game_lost
            number_of_games = int(number_of_games) + 1
            games_lost = int(games_lost) + 1
            print("Your game/ratio is " + str(number_of_games))
        if number_of_games <= 0:
            print("You are still on level 1!")
    elif res == "draw":
        number_of_games = int(number_of_games) + 1
        games_draw = int(games_draw) + 1
        print("Your game/ratio is " + str(number_of_games))


if __name__=="__main__":
    achievements("won")
