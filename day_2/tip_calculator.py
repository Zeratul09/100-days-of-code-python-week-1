#If the bill was $150.00, split between 5 people, with 12% tip. 

#Each person should pay (150.00 / 5) * 1.12 = 33.6

#Format the result to 2 decimal places = 33.60

#Tip: There are 2 ways to round a number. You might have to do some Googling to solve this.💪

#Write your code below this line 👇

#Get the necessary inputs for the result: the bill, the perecntage of tip, and the amount of people.

print("Welcome to the tip calculator!")

bill = input("What was the total bill? ")
tip = input("What percentage tip would you like to give, 10, 12 or 15? ")
number_of_people = input("How many people to split the bill? ")


bill_as_float = float(bill.replace("$",""))
tip_as_float = float(tip)/100
number_of_people_as_int = int(number_of_people)

#Do the calculation and the round up of the result and print it

result = (bill_as_float / number_of_people_as_int) * (1 + tip_as_float)
rounded_result = round(result, 2)

#The format part makes sure that even if our result is 10.1 exactly, it will add a 0 to it.
rounded_result = "{:.2f}".format(rounded_result)

print(f"Each person should pay: ${rounded_result}")