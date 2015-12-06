from main import *
from logic import *
import pickle

def achievements(res):
    #loads the stats from a local file
    f = open("achievements.pickle","rb")
    stats = pickle.load(f)
    f.close()
    #1-games played, 2-games won 3-games lost 4 - games draw 5 - level
    if res == "won":
        #ups the stats
        stats[0]+=1
        stats[1]+=1
        stats[4]+=1
        print("You are level " + str(stats[4]))
    elif res == "lost":
        if int(stats[4]) >1 :
            stats[0]+=1
            stats[2]+=1
            stats[4]-=0.5
            print("You are level "+ str(stats[4]))
        if int(stats[4]) <= 1:
            stats[0]+=1
            print("You are still on level 1!")
    elif res == "draw":
        stats[0]+=1
        stats[3]+=1
        stats[4]+=0.5
        print("You are level " + str(stats[4]))
    #closes the stats file
    f = open("achievements.pickle","wb")
    pickle.dump(stats, f)
    f.close()
 
if __name__=="__main__":
    achievements("won")
