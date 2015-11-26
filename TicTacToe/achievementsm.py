from main import *
import pickle

achievements = {1:"Congratulations on your win. You are lever 1!", 2:"You are level 2"}
pickle_out = open("achievements.pickle","wb")
pickle.dump(achievements, pickle_out)
pickle_out.close()



def achievements(res):
    f = open()
    pickledlist = pickle.load(f)
    games = pickledlist[0]
    gameswon = pickledlist[1]
    gameslost = pickledlist[2]
    gamesdraw = pickledlist[3]
    ratio = pickledlist[4]

    games += 1
    if res == "won":
        gameslost += 1
        result = achievements[int(number_of_games)]
        print(str(result))
        print("Your game/ratio is " + str(number_of_games))
    elif res == "lost":
        gameslost += 1


        if number_of_games > 0 :
            number_of_games = int(number_of_games) - 1
            result = achievements[int(number_of_games)]
            print(result)
            print("Your game/ratio is " + str(number_of_games))
        if number_of_games <= 0:
            print("You are still on level 1!")
    elif res == "draw":
        gamesdraw += 1
        number_of_games = int(number_of_games) + 0
        result = achievements[int(number_of_games)]
        print(result)
        print("Your game/ratio is " + str(number_of_games))

    if games != 0:
        ratio = (gameswon - gameslost) / games
    else:
        ratio = 0



if __name__=="__main__":
    achievements()
