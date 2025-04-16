import random
print("Hello")
print("You are being very dangerous.Please do your best to increase your chances your chances of survival")
    
    
def explore():
    print("You are in a strange cave")
    print("You have two acesses in front of you,left or right!(Enter 'left' or'right')")
    choice = input().lower ()
    if choice =="left":
            print("You have entered the left access")
            left_access()
    elif choice =="right":
        print("You have entered the right access")
        right_access()
    else:
        print("Please enter a valid choice!")
        explore()

    def left_access():
        print("You have come to a treasure chest...")
    print("Do you want to open the treasure or not!(Enter 'y' or 'n')")
    choice = input().lower()
    if choice =='y':
        print("You opened the treasure chest and found a glittering bunch of gems!You won ah!")
    elif choice == 'n':
        print("You decided not to open the treasure chest,but the cave started to tremble...")
        print("Ceiling collapsed and you were buried under the stones.Game over!")
    else:
        print("Please enter a valid choice")
        left_access()

def right_access():
    print("You have met a monster...")
    print("Were you going to fight with the monster!(Enter 'y' or ' n ')")
    choice = input().lower()

    if choice =='y':
        print("You showed your weapon and engaged in a fierce battle with the monster...")
        if random.randint(0,1) == 0:
            print("You were so brave that you have killed the monster and won!")
        else:
            print("The monster was too strong.You have been defeated.Game over!")
   
    elif choice == 'n':
        print("You decided to run away but the monster have caught up...")
        print("Please enter a alid choice!")
        right_access()

import random
health = 100
stamina = 100
speed = 100

random_number=random.randrange(0.16)
print(random_number)
if random_number == random.randrange:
    while True:
        print(f"Current position: {0,15}")
    direction = input("Enter direction to move or 'exit' to quit: ").strip().lower()
    if direction == 'exit':
        print("Exiting the game. Goodbye!")