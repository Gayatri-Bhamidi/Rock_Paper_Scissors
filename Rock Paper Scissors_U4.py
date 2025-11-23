import random

rock = print("""
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
""")

paper = print("""
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
""")

scissors = print("""
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
""")

user_choice = int(input("Choose: type 0 for rock, 1 for paper, 2 for scissors \n"))

computer_choice = random.randint(0, 2)
print("computer choice =" , computer_choice)

if user_choice == 0 and computer_choice == 2:
    print("You win!!")
    
elif computer_choice == 0 and user_choice == 2:
    print("You loose!")
    
elif computer_choice > user_choice:
    print("You loose!!")
    
elif computer_choice == user_choice:
    print("It's a draw")
    
else:
    print("enter a valid number")