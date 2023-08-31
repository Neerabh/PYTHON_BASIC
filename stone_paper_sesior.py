import random
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

image=[rock,paper,scissors]

user_choice = int(input("what do you want to choose? 0 stone , 1 paper ,2 sesior.  \n"))

if user_choice>=3 or user_choice<0:
  print("you enter in valid number")

else:
  print(image[user_choice])
  
  computer_choice=random.randint(0,2) 
  print("computer_choice:")
  print(image[computer_choice])
  
  if user_choice == 0 and computer_choice == 2:
    print("you win")
    
  elif computer_choice==0 and user_choice==2:
    print("you loose")
  
  elif user_choice>computer_choice:
    print("you win")
    
  elif computer_choice>user_choice:
    print("you loose")
    
  elif computer_choice==user_choice:
    print("it is a draw")
  