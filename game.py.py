import random

while True:
    print("Rock-Paper-Scissors game \n Enter your choice \n 1 - Rock \n 2 - Paper \n 3 - Scissors \n")
    ch = int(input("Enter your choice: "))
    while ch > 3 or ch < 1:
        ch = int(input('Enter a valid choice: '))
    if ch == 1:
        ch_name = 'Rock'
    elif ch == 2:
        ch_name = 'Paper'
    else:
        ch_name = 'Scissors'
    print('User choice is:', ch_name)
    print("Now it's Computer's Turn...")
    comp_choice = random.randint(1, 3)
    if comp_choice == 1:
        comp_choice_name = 'Rock'
    elif comp_choice == 2:
        comp_choice_name = 'Paper'
    else:
        comp_choice_name = 'Scissors'
    print("Computer choice is:", comp_choice_name)
    if ch == comp_choice:
        result = "DRAW"
    elif (ch == 1 and comp_choice == 2) or (comp_choice == 1 and ch == 2):
        result = 'Paper'
    elif (ch == 1 and comp_choice == 3) or (comp_choice == 1 and ch == 3):
        result = 'Rock'
    elif (ch == 2 and comp_choice == 3) or (comp_choice == 2 and ch == 3):
        result = 'Scissors'
    if result == "DRAW":
        print("It's a tie!")
    elif result == ch_name:
        print("You win!")
    else:
        print("Computer wins!")
    print("Do you want to play again? (y/n)")
    ans = input()
    if ans == 'n':
        break
print("Thanks for playing!")
