import random
import sys
print("Welcome to Rock, Paper, scissor Game")
ties=0
win=0
loss=0
def result():
    print("Number of games won= ",win)
    print("Number of games lost = ",loss)
    print("number of games tie = ",ties)
while True:
    
    while True:
        select=input("r- rock,p-paper,s-scissor,q-quit") 
        if select=='q':
            sys.exit()
        elif select=='r' or select=="s" or select=='p':
            break
        else:
            print("Select the options between r,p,s,q")
    if select=='r':
        print("Rock versus...")
    elif select=="p":
        print("Paper versus...")
    elif select=="s":
        print("Scissor versus...")
    
    comp_choice=random.randint(1,3)
    if comp_choice==1:
        choice='r'
        print("Rock")
    elif comp_choice==2:
        choice='p'
        print("paper")
    elif comp_choice==3:
        choice='s'
        print("Scissor")
    if select==choice:
        print("it's a tie")
        ties+=1
        result()
    elif select=="r" and choice=="p":
        print("you lost")
        loss+=1
        result()
    elif select=='r' and choice=='s':
        print("you won")
        win+=1
        result()
    elif select=='p' and choice=='r':
        print("you won")
        win+=1
        result()
    elif select=="p" and choice=="s":
        print("you lost")
        loss+=1
        result()
    elif select=='s' and choice=='p':
        print("you won")
        win+=1
        result()
    elif select=="s" and choice=="r":
        print("you lost")
        loss+=1
        result()
    
    


    
