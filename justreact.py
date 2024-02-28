import sys
import random

playerchoice = input("Enter a value:\n1.For Rock.\n2.For Paper.\n3.For Scissors.\n")

player = int(playerchoice)

if player < 1 and player > 3:
    sys.exit("Please enter 1, 2 or 3")

computerchoice = random.choice("123")
computer = int(computerchoice)

print("")

print(f"Just React chose 🙌! {playerchoice}")
print(f"Python chose {computerchoice}")

print("")

print("game result".upper().center(16, "="))

if player == 1 and computer == 3:
    print("Just React You win Buddy! 🙌")

elif player == 2 and computer == 1:
    print("Just React You win Buddy! 🙌")

elif player == 3 and computer == 2:
    print("Just React You win Buddy! 🙌")

elif player == computer:
    print("Draw Tena 🙁")
    
else:
    print("Python wins! 🐍")