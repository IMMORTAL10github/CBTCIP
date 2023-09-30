
import random
actions=("rock","paper","scissor")
def computer():
        return random.randrange(len(actions))
def game():
        choice=input("enter 'yes' or 'y' if you want to play ....'no' or 'n' if you dont want to play: ").lower()
        if(choice=="yes" or choice=="y"):
            player1=input("enter rock/paper/scissor: ").lower()
            if player1 not in actions:
                print("wrong entry please enter rock/paper/scissor")
            else:
                player2=actions[computer()]
                print("computer entered:"+ player2)
                if(player1==player2):
                    print("....DRAW....")
                elif (player1=="rock" and player2=="scissor") or (player1=="paper" and player2=="rock") or (player1=="scissor" and player2=="paper"):
                    print("...YOU WIN...")
                else:
                    print("...COMPUTER WINS...")
            game()
        else:
            print("THANK YOU")

print("welcome to rock paper scissor game")
game()
