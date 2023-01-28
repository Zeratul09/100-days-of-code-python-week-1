# 🚨 Don't change the code below 👇
student_heights = input("Input a list of student heights ").split()
for n in range(0, len(student_heights)):
  student_heights[n] = int(student_heights[n])
# 🚨 Don't change the code above 👆


#Write your code below this row 👇
#While the sum() and len() functions can make this challange easy, we are not allowed to use them.
#We will first create 2 new variables. One (i) for counting our index and two (total) for adding our items in the list together

i = 0
total = 0

#We are going to iterate over the list and updating our variables to the new value as we are going over it

for n in student_heights:
    total += n
    i += 1

#Just some testing, ignore.
# print(i)
# print(total)

#Finally, we are going to calculate our average and round it and print it.
average = round(total / i)
print(average)