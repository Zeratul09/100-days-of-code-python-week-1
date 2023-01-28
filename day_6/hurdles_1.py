#This should be used on a site called reeborg's world (Hurdle 1 Challange)
#All functions here won't make any sense outside of: https://reeborg.ca/reeborg.html?lang=en&mode=python&menu=worlds%2Fmenus%2Freeborg_intro_en.json&name=Hurdle%201&url=worlds%2Ftutorial_en%2Fhurdle1.json

def turn_left():
def move():

#Copy the code starting below:

#Copy the code starting below:
#We define a function for "jumping" over a wall in the game:

def jump():
    move()
    turn_left()
    move()
    turn_right()
    move()
    turn_right()
    move()
    turn_left()

#We define a function for "turning right" in the game:

def turn_right():
    turn_left()
    turn_left()
    turn_left()


#The actual route:
#However, instead of calling the jump() function 6 times. Let's create a loop for it.

for step in range(6):
    jump()