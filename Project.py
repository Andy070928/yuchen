print("Hello")
print("You are being pursued by a stalker.Please do your best to increase your chances your chances of survival")
print("You must ensure your health points,your staming points and you mental sanity points")

health = 100 
stamina = 100


mentalsanity = 100
print("Ps: if you health and stamina are less than 20,you will not able to run faster 0though you choose the fast speed")
while True:
    choice = input(health,stamina,mentalsanity)
    if choice == health: 
        print("the healthy decreased", health)    
    elif choice == stamina:
        print("the stamina decreased",stamina)
    elif choice == mentalsanity:
        print("the mentalsanity decreased",mentalsanity)
        
