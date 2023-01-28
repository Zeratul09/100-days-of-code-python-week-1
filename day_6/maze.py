# Lost in a maze

# Reeborg was exploring a dark maze and the battery in its flashlight ran out.

# Write a program using an if/elif/else statement so Reeborg can find the exit. The secret is to have Reeborg follow along the right edge of the maze, turning right if it can, going straight ahead if it can’t turn right, or turning left as a last resort.
# What you need to know

#     The functions move() and turn_left().
#     Either the test front_is_clear() or wall_in_front(), right_is_clear() or wall_on_right(), and at_goal().
#     How to use a while loop and if/elif/else statements.
#     It might be useful to know how to use the negation of a test (not in Python).

#This should be used on a site called reeborg's world (Hurdle 1 Challange)
#All functions here won't make any sense outside of: https://reeborg.ca/reeborg.html?lang=en&mode=python&menu=worlds%2Fmenus%2Freeborg_intro_en.json&name=Hurdle%201&url=worlds%2Ftutorial_en%2Fhurdle1.json

def turn_left():
def move():
def at_goal():
def front_is_clear():
def wall_in_front():
def wall_on_right():
def right_is_clear():

#Copy the code starting below:
#We define a function for "jumping" over a wall in the game:

def jump():
    turn_left()
    move()
    turn_right()
    move()
    turn_right()
    move()
    turn_left()

def turn_right():
    turn_left()
    turn_left()
    turn_left()

def avoid_wall():
    turn_left()
    move()
    turn_right()
    move()
    turn_right()
    move()
    turn_left()

#Let's define a new function called "high jump":

def high_jump():
    #We first create a varible to count our height, as we will have to get back to the ground to continue.
    h = 0

    #We first turn left to start our jump:
    turn_left()
    #If there is a wall on our right, we add 1 to our height and move higher in the air, and repeat until there is no wall on our right:
    while wall_on_right():
        h += 1
        move()
    #Then we turn right to start getting back to the ground:
    turn_right()
    move()
    #Now, we will have to land back onto the ground, so we will run a while loop and using the same height index:
    turn_right()
    while h != 0:
        h -= 1
        move()
    turn_left()



#The actual route:
#We will first set the condition for the while loop, so while it's not true it will do the following:
#**

while front_is_clear():
    move()
turn_left()

while not at_goal():
    if right_is_clear():
        turn_right()
        move()
    elif front_is_clear():
        move()
    else:
        turn_left()