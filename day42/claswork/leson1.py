numbers = [1, -2, 3, -4, 5, -6, 7, -8, 9, -10]
positive_numbers = []
negative_numbers = []

for number in numbers:
    if number > 0:
        positive_numbers.append(number)
    elif number < 0:
        negative_numbers.append(number)

print("დადებითი რიცხვები: ", positive_numbers)
print("უარყოფითი რიცხვები: ", negative_numbers)