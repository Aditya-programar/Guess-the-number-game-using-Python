from random import randint
num=randint(1,20)
number_of_guesses=1
print("Number of guesses is limited to only 9 times: ")
while (number_of_guesses<=9):
    guess_number = int(input("Guess the number :\n"))
    if guess_number<num:
        print("you enter less number please input greater number.\n")
    elif guess_number>num:
        print("you enter greater number please input smaller number.\n ")
    else:
        print("you won\n")
        print(number_of_guesses,"guesses were taken by you to guess the number")
        break
    print(9-number_of_guesses,"guesses left")
    number_of_guesses = number_of_guesses + 1

if(number_of_guesses>9):
    print("Game Over")