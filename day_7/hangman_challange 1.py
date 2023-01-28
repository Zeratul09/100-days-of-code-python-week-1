#The way we will do this as that we will fork each code as the next part of the challange appears and also it's going to be a separate file.

#Step 1 

import random

word_list = ["aardvark", "baboon", "camel"]

#TODO-1 - Randomly choose a word from the word_list and assign it to a variable called chosen_word.
#We will use the random.choice function.

chosen_word = random.choice(word_list)

#TODO-2 - Ask the user to guess a letter and assign their answer to a variable called guess. Make guess lowercase.
#A simple input function with an added lower function.

guess = input("Guess a letter from A-Z: ").lower()

#TODO-3 - Check if the letter the user guessed (guess) is one of the letters in the chosen_word.

#When you write a for loop like this think of this way:
    #For each character (c, so index) in our word (in this case chosen_word as a string) check that IF the character in the word (the index) matches our guess then print "Right" else print "Wrong."
    #So basically, you first specify what are we going to index and then in this case what the index needs to do (match our guess)
for c in chosen_word:
    if c == guess:
        print("Right")
    else:
        print("Wrong")