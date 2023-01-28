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

#https://www.draw.io/?lightbox=1&highlight=0000ff&edit=_blank&layers=1&nav=1&title=Treasure%20Island%20Conditional.drawio#Uhttps%3A%2F%2Fdrive.google.com%2Fuc%3Fid%3D1oDe4ehjWZipYRsVfeAx2HyB7LCQ8_Fvi%26export%3Ddownload

#Write your code below this line 👇

#We will close the program each time we make the selection that leads to "Game Over." And also to stop the program running unnecesarily.
#We check step 1 from the flow chart:

step_1 = input('You\'ve arrived at a crossroeads. Do you want to go "left" or "right"? ')

if step_1.lower() == "right":
    print("You've fell into a hole. Game Over.")
    exit()
elif step_1.lower() == "left":
    print("You've avoided the hazard and continued on your journey.")
else:
    print("You've fell into a hole. Game Over.")
    exit()

#We check step 2 from the flow chart:

step_2 = input('You\'ve arrived at a lake which has an island on the middle. Type "swim" to swim across or "wait" to wait for a boat. ')

if step_2.lower() == "swim":
    print("You got attacked by a trout. Game Over.")
    exit()
elif step_2.lower() == "wait":
    print("After a while, a boat has arrived and you've hopped on it.")
else:
    print("You got attacked by a trout. Game Over.")
    exit()

#We check step 3 from the flow chart:

step_3 = input('You\'ve arrived at a building near the docks.\nThe building has 3 colored doors.\nWill you choose the "red", the "blue" or the "yellow" one? ')

if step_3.lower() == "red":
    print("It's a room full of fire. You've got burned by fire. Game Over.")
    exit()
elif step_3.lower() == "blue":
    print("It's a dark room with a lot of growling. You've been eaten by beasts. Game Over.")
    exit()
elif step_3.lower() == "yellow":
    print("You open a door with a room full of glimmering treasure. You Win!")
else:
    print("Game Over.")
    exit()