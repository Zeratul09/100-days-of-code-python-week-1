# 🚨 Don't change the code below 👇
student_scores = input("Input a list of student scores ").split()
for n in range(0, len(student_scores)):
  student_scores[n] = int(student_scores[n])
print(student_scores)
# 🚨 Don't change the code above 👆

#Write your code below this row 👇
#While the min() and max() functions can make this challange easy, we are not allowed to use them.
#We will first create a new variable called "highest_value" which will serve as our comparison tool for the items in the list

highest_value = 0

#We are going to iterate over in our list and compare each item to our current highest value. If it's greater than the current score then it will update it's value
#If it's not, it will continue to the next item in the list.

for score in student_scores:
    if score > highest_value:
        highest_value = score

#Finally, we will print out our result as required:
print(f"The highest score in the class is: {highest_value}")