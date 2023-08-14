import random
choose=['rock','paper','scissor']
user_choice=input("Enter rock,paper,scissor to play the game: ").lower()
computer_choice=random.choice(choose)
print(f"Computer choice is {computer_choice}")
print(f"Your choice is {user_choice}")
if user_choice==computer_choice:
    print("It's draw")
elif user_choice=='rock':
    if computer_choice=='paper':
        print("YOU LOOSE!!")
    elif computer_choice=='scissor':
        print("YOU WIN!!")
elif user_choice=='paper':
    if computer_choice=='rock':
        print("YOU WIN!!")
    elif computer_choice=='scissor':
        print("YOU LOOSE!!")
elif user_choice=='scissor':
    if computer_choice=='rock':
        print("YOU LOOSE!!")
    elif computer_choice=='paper':
        print("YOU WIN!!")
else:
    print("Invalid choice")
