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



#The actual route:
#However, instead of calling the jump() function 6 times. Let's create a while loop for it.
#We will first set the condition for the while loop, so while it's not true it will do the following:
while not at_goal():
    #If we hit a wall, we will use the avoid_wall function:
    if wall_in_front():
        jump()
    #If we can see that 2 squares are clear, we will move forward:
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
