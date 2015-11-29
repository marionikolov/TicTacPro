from main import *
from logic import *
import pickle

def achievements(res):
    #achievements = {1:"Congratulations on your win. You are lever 1!", 2:"You are level 2"}
    pickle_out = open("doc.pickle","wb")
    stats=[0,0,0,0,0]
    pickle.dump(stats, pickle_out)
    #1-games played, 2-games won 3-games lost 4 - games draw 5 - level

    if res == "won":
        stats[0]+=1
        stats[1]+=1
        stats[4]+=1
        print("You are level " + str(int(stats[4])))
    elif res == "lost":
        if int(stats[4]) >1 :
            stats[0]+=1
            stats[2]+=1
            stats[4]-=0.5
            print("You are level "+ str(int(stats[4])))
        if int(stats[4]) <= 1:
            stats[0]+=1
            print("You are still on level 1!")
    elif res == "draw":
        stats[0]+=1
        stats[3]+=1
        stats[4]+=0.5
        print("You are level " + str(int(stats[4])))


        
if __name__=="__main__":
    achievements("won")
