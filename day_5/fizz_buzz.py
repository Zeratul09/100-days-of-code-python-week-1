#Write your code below this row 👇

#Write up the for loop for the range and the modulo checks.
#Start with the least likely outcome that modulo 3 and 5 == 0 is true.
#Then modulo 3 == 0 or modulo 5 == 0 is true.
#Finally, if neither is true print out the number.

for number in range(1, 101):
    if (number % 3 == 0) and (number % 5 == 0):
        print("FizzBuzz")
    elif number % 3 == 0:
        print("Fizz")
    elif number % 5 == 0:
        print("Buzz")
    else:
        print(number)