print("Welcome to the tresure island.")
print("Your missin is to find the tresure.")
choice1 = input('You are at the crossroad, where do you want to go? type "left" or "right".').lower()
if choice1=="left":
 choice2 = input('You have come to lake.There is an island in the middle of lake.Type "wait" for a boat.Type "swim" to swim across.').lower()
 if choice2=="wait":
     choice3 = input("You arrive at the island unharmed.There ia a house with three doors.One red, one yellow and blue.Which door do you choose?").lower()
     if choice3=="red":
        print("It's a room full of fire.Game over.")
     elif choice3=="yellow":
        print("You found the tresure! You win!")
     elif choice3=="blue":
        print("you enter a room of beasts.Game over.")
     else:
        print("you choose a door that does not exixt.Game over.")  
 else:
    print("You are attacked by an angry trout. Game over.")
else:
    print("You fell into a hole. game over.")