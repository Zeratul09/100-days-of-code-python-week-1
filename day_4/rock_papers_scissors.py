rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

#Write your code below this line 👇

#We will import the random module for our work:
import random

#We write a short intro text and ask for an input
print("Welcome to the Rock, Paper, Scissors Game.")
select = input("Make your selection: Type '0' for Rock, '1' for Paper or '2' for Scissors. ")

#We convert our human input into a int and get our random value for our AI player
human_selection = int(select)
ai_selection = random.randint(0, 2)

#We set the picture for the output for our AI players based on if it's 0, 1 or 2
if ai_selection == 0:
    picture = rock
elif ai_selection == 1:
    picture = paper
elif ai_selection == 2:
    picture = scissors
else:
    exit()


#Let's write up all the possible combinations with rock:
if (human_selection == 0) and (ai_selection == 0):
    print(f"You've chose:\n {rock}\n The AI chose:\n {picture}\n It's a draw!")
elif (human_selection == 0) and (ai_selection == 1):
    print(f"You've chose:\n {rock}\n The AI chose:\n {picture}\n You've lost!")
elif (human_selection == 0) and (ai_selection == 2):
    print(f"You've chose:\n {rock}\n The AI chose:\n {picture}\n You've won!")
else:
    print("Your selection was invalid. Type '0' for Rock, '1' for Paper or '2' for Scissors.")

#Let's write up all the possible combinations with paper:
if (human_selection == 1) and (ai_selection == 0):
    print(f"You've chose:\n {paper}\n The AI chose:\n {picture}\n You've won!")
elif (human_selection == 1) and (ai_selection == 1):
    print(f"You've chose:\n {paper}\n The AI chose:\n {picture}\n It's a draw!")
elif (human_selection == 1) and (ai_selection == 2):
    print(f"You've chose:\n {paper}\n The AI chose:\n {picture}\n You've lost!")
else:
    print("Your selection was invalid. Type '0' for Rock, '1' for Paper or '2' for Scissors.")

#Let's write up all the possible combinations with scissors:
if (human_selection == 2) and (ai_selection == 0):
    print(f"You've chose:\n {scissors}\n The AI chose:\n {picture}\n You've lost!")
elif (human_selection == 2) and (ai_selection == 1):
    print(f"You've chose:\n {scissors}\n The AI chose:\n {picture}\n You've won!")
elif (human_selection == 2) and (ai_selection == 2):
    print(f"You've chose:\n {scissors}\n The AI chose:\n {picture}\n It's a draw!")
else:
    print("Your selection was invalid. Type '0' for Rock, '1' for Paper or '2' for Scissors.") 