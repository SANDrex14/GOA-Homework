correct_number = 7

guess = int(input("Guess a number between 1 and 10: "))

while guess != correct_number:
    guess = int(input("Incorrect! Try again: "))

print("Congratulations, you guessed the number", correct_number)