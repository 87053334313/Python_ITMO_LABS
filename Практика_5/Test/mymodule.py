def createName(myname):
    return str(myname)
id=1;
def createName():
    global id
    string="player"
    str_id=str(id)
    string+=str_id

    id=id + 1;
    return string;
import random
import time

win_1=0;
win_2=0;

def WhoWin(win__1,win__2,player1,player2):
    if(win_1>win_2):
        print("Pobedil",player1)
    else:
        if(win_2>win_1):
            print("Pobedil",player2)
        else:
            print("Nich'ya")


def SamaIgra(player1):
    print( player1," throws cub")
    time.sleep(2)
    n1 = random.randint(1,6)
    print( player1,"throwed cub",'vipalo = ',n1)
    return n1;
def Igra_SkokBroskov(brosok,player_1,player_2):
    for i in range(brosok):
        n1=SamaIgra(player_1)
        n2=SamaIgra(player_2)
        if(n1>n2):
            global win_1
            win_1+=1;
        elif(n2>n1):
            global win_2
            win_2+=1;
        else:
            1==1
    else:
        print('Konets programmi')
        WhoWin(win_1,win_2,player_1,player_2)



