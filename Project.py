import random 

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

        maxDistance = 35
        playerDistance = 0
        MonsterDistance = -5
        PlayerDice = 0
        MonsterDice = -1
        turn = 0

        while playerDistance >= MonsterDistance and playerDistance < maxDistance:
            
            turn += 1

            while True:
                x = input("Press 'E' to roll the dice")
                if x.lower() == 'e':
                    print("You rolled the dice")
                    PlayerDice = random.randint(1, 5)
                    break
                else : 
                    print("Please enter a valid choice")
                    continue

            playerDistance += PlayerDice

            if turn >= 2 :
                MonsterDice = random.randint(2, 6)
                MonsterDistance += MonsterDice
            
            print (f"Turn : {turn}")
            print (f"Player's distance : {playerDistance}")
            print (f"Monster's distance : {MonsterDistance}")

        if playerDistance >= maxDistance:
            print("You have successfully escaped from the monster!")
        elif playerDistance < MonsterDistance:
            print("The monster caught up with you and you were defeated!")
    
    else:
        print("Please enter a valid choice!")
        right_access()


print("Hello")
print("You are being very dangerous.Please do your best to increase your chances your chances of survival")
explore()