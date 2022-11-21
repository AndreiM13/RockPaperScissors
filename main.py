import random

paper = '''
    _______
---'   ____)____  
          ______)  
          _______)  
         _______)
---.__________)       

'''

rock = '''
    _______
---'   ____)  
      (_____)  
      (_____)  
      (____)
---.__(___)


'''

scissors = '''  
    _______
---'   ____)____  
          ______)  
       __________)  
      (____)
---.__(___)  
'''  

user = int(input("What do you choose? Type 0 for rock , 1 for papaer , 2 for scissors\n"))

computer = random.randint(0,2)

if user  == 0 and  computer == 0:

    print(f"{rock}\n")
    print(f"{rock}")
    print("It's a draw!")

elif user == 0 and computer == 1:

    print(f"{rock}\n")
    print(f"{paper}")
    print("You lose!")

elif user == 0 and computer == 2:

    print(f"{rock}\n")
    print(f"{scissors}")
    print("You win!")

elif user == 1 and computer == 0:

     print(f"{paper}\n")
     print(f"{rock}")
     print("You win!")

elif user == 1 and computer == 1:

    print(f"{paper}\n")
    print(f"{paper}")
    print("It's a draw!")

elif user == 1 and computer == 2:

    print(f"{paper}\n")
    print(f"{scissors}")
    print("You lose!")

elif user == 2 and computer == 0:

    print(f"{scissors}\n")
    print(f"{rock}")
    print("You lose!")

elif user == 2 and computer == 1:

    print(f"{scissors}\n")
    print(f"{paper}")
    print("You win!")

elif user == 2 and computer == 2:
    
    print(f"{scissors}\n")
    print(f"{scissors}")
    print("It's a draw!")

else:
    print("Try to enter 0,1 or 2!")










