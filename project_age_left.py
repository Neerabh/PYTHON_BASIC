# 🚨 Don't change the code below 👇
age = input("What is your current age? ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

age_as_int=int(age)

year_remain = 90 - age_as_int
days_remain = year_remain * 365
week_remain = year_remain * 52
months_remain = year_remain * 12

message=f"you have {days_remain} days ,{weeks_remain} weeks , and {months_remain} months left "
print(message)