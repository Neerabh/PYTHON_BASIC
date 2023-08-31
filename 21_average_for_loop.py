# 🚨 Don't change the code below 👇
student_heights = input("Input a list of student heights ").split()
for n in range(0, len(student_heights)):
  student_heights[n] = int(student_heights[n])
# 🚨 Don't change the code above 👆

# total=sum(student_heights)
# students=len(student_heights)
# average=round(total/students)
# print(average)

#this is how sum function work by for loop
total=0
for height in student_heights:
  total+=height

#how len function work
students=0
for student in student_heights:
  students+=1

average=round(total/student)
print(average)

