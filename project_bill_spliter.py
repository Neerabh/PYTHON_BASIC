#split string method
import random
name=input("enter your names? by comma")

# split = name.split(", ")

# #to get total number in list
# num_items=len(name) 

# ran_choice=random.randint(0,num_items-1)
# payer=name[ran_choice]
# print("person who is going to pay is"+payer)


payer=random.choice(name)
print("person who is going to pay is"+payer)
