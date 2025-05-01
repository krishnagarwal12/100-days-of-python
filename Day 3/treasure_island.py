print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.") 
l_or_r = input("You are at a crossroad.\nWhere do you want to go?\nLeft or right?\n")
l_or_r = l_or_r.lower()
if l_or_r=="left":
    w_or_s = input('You have come to a lake.\nThere is an island in the middle of the lake.\nType "wait" to wait for a boat or type "swim" to swim accross.\n')
    w_or_s = w_or_s.lower()
    if w_or_s == "wait":
        door = input("You arrive at the island unharmed.\nThere is a house with 3 doors.\nOne red, one yellow, one blue.\nWhich colour do you choose?\n")
        door = door.lower()
        if door=="red":
            print("Bumed by fire.\nGame over.")
        elif door=="yellow":
            print("You win!")
        elif door=="blue":
            print("Eaten by beasts.\nGame over.")
        else:
            print("Game over.")
    else:
        print("Attacked by trout.\nGame over.")
else :
    print("Fall into a hole.\nGame over.")
