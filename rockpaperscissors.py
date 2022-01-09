import random
import time
a = 0
b = 0

def play(x,y):
    global a, b
    print("===================================================================================")
    plays = [0, 1, 2]
    time.sleep(0.5)
    names = ["Rock","Paper","Scissors"]
    print("Rock = 1, Paper = 2, Scissors = 3")
    pos = -1
    time.sleep(1)
    def choose():
        pos = int(input("Choose your number: "))-1
        return pos

    pos = choose()
    if pos > 2 or pos < 0:
        choose()
    else:
        comp_pos = random.choice(plays)

        if plays[pos] == 2 or plays[comp_pos] == 2:
            plays[0] = 3

        time.sleep(0.5)
        print("You :",names[pos])
        time.sleep(0.5)
        print("Computer :",names[comp_pos])
        time.sleep(1)

        if plays[pos] > plays[comp_pos]:
            print("You beat {} with {} !".format(names[comp_pos], names[pos]))
            x += 1
            a = x
        elif plays[pos] < plays[comp_pos]:
            print("You got beaten by {} with {}".format(names[comp_pos], names[pos]))
            y += 1
            b = y
        else:
            print("It's a tie between {0} and {0}".format(names[comp_pos]))

while True:
    try:
        time.sleep(0.5)
        play(a,b)
        print("You : {}, Computer : {}".format(a,b))
        time.sleep(1)
    except:
        a = 0
        b = 0
        print("===================================================================================")
        print("Running the program again")