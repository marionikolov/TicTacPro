from main import *
import pickle

achievements = {1:"Congratulations on your win. You are lever 1!", 2:"You are level 2"}
pickle_out = open("achievements.pickle","wb")
pickle.dump(achievements, pickle_out)
pickle_out.close()



def achievements(res):
    number_of_games = 0
    
    if res == "won":
        number_of_games = int(number_of_games) + 1
        result = achievements[int(number_of_games)]
        print(result)
        print("Your game/ratio is " + str(number_of_games))
    elif res == "lost":
        if number_of_games >0 :
            number_of_games = int(number_of_games) - 1
            result = achievements[int(number_of_games)]
            print(result)
            print("Your game/ratio is " + str(number_of_games))
        if number_of_games <= 0:
            print("You are still on level 1!")
    elif res == "draw":
        number_of_games = int(number_of_games) + 0
        result = achievements[int(number_of_games)]
        print(result)
        print("Your game/ratio is " + str(number_of_games))


if __name__=="__main__":
    achievements()
