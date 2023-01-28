# What you need to know

#     The functions move() and turn_left().
#     The condition at_goal() and its negation.
#     How to use a while loop.

# Your program should also be valid for world Hurdles 1.

#This should be used on a site called reeborg's world (Hurdle 1 Challange)
#All functions here won't make any sense outside of: https://reeborg.ca/reeborg.html?lang=en&mode=python&menu=worlds%2Fmenus%2Freeborg_intro_en.json&name=Hurdle%201&url=worlds%2Ftutorial_en%2Fhurdle1.json

def turn_left():
def move():
def at_goal():

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
#However, instead of calling the jump() function 6 times. Let's create a while loop for it.


while not at_goal():
    jump()

#If it makes it more readable, you can write it as "while at_goal != True:"
#So both for and while loops are similar however the difference is:
#If you want to iterate over something like a list ("do something to each item"), or "for numbers in range(a,b)" go for a for loop.
#If you want to run something over and over until a condition becomes true or false, go for a while loop. One note to this if the conditiion is never met, then this will become an infinite loop. If you don't know why are you in an infinite loop, just print out it's condition.
