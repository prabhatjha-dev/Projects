# making rock,paper,scissor game
import random
print("Rock, Paper, Scissors ✊✋✌️")
choice=["Rock","Paper","Scissors"]
user_choice=input("choose Rock, Paper, or Scissors: ")

computer_choice=random.choice(choice)
print("you choose:",user_choice)
print("computer choose:",computer_choice)
if(user_choice==computer_choice):
    print("Match Draws")
elif(user_choice=="Scissors" and computer_choice=="Paper") or \
(user_choice=="Rock" and computer_choice=="Scissors")or \
(user_choice=="Paper" and computer_choice=="Rock"):
    print("You wins")
else:
    print("You lose")
