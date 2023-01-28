# What you need to know

    # The functions move() and turn_left().
    # The conditions front_is_clear() or wall_in_front(), at_goal(), and their negation.
    # How to use a while loop and an if statement.

# Your program should also be valid for world Hurdles 1.

#This should be used on a site called reeborg's world (Hurdle 1 Challange)
#All functions here won't make any sense outside of: https://reeborg.ca/reeborg.html?lang=en&mode=python&menu=worlds%2Fmenus%2Freeborg_intro_en.json&name=Hurdle%201&url=worlds%2Ftutorial_en%2Fhurdle1.json

def turn_left():
def move():
def at_goal():
def front_is_clear():
def wall_in_front():
def wall_on_right():

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
while not at_goal():
    #If we hit a wall, we will use the high_jump function which should account for any type of wall:
    if wall_in_front():
        high_jump()
    #If we can see that nothing is in the front we move forward:
    elif front_is_clear:
        move()
    #If we see that a wall is coming (so in the next square) we will jump over it: (We reworked our jump function)
    #else:
    #    jump()

#Another solution is to modify the jump function so that it doesn't move foward first but instead tries jumping over right away.

#If it makes it more readable, you can write it as "while at_goal != True:"
#So both for and while loops are similar however the difference is:
#If you want to iterate over something like a list ("do something to each item"), or "for numbers in range(a,b)" go for a for loop.
#If you want to run something over and over until a condition becomes true or false, go for a while loop. One note to this if the conditiion is never met, then this will become an infinite loop. If you don't know why are you in an infinite loop, just print out it's condition.


#And one more note this one, that as the tutor (Angela Yu) said that this can be completed with 24 lines of code, if I remove everything that is unnecessary it's exactly 24 lines of code:

# def turn_right():
#     turn_left()
#     turn_left()
#     turn_left()

# def high_jump():
#     i = 0
#     turn_left()
#     while wall_on_right():
#         i += 1
#         move()
#     turn_right()
#     move()
#     turn_right()
#     while i != 0:
#         i -= 1
#         move()
#     turn_left()

# while not at_goal():
#     if wall_in_front():
#         high_jump()
#     elif front_is_clear:
#         move()

#You can also solve the "high jump" without using an index and just using the front_is_clear() function on the site.