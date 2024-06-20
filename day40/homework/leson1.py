number_list = []

for i in range(10):
    number = int(input("შემოიტანეთ რიცხვი: "))
    number_list.append(number)

even_numbers = []
odd_numbers = []

for number in number_list:
    if number % 2 == 0:  # თუ ლუწია
        even_numbers.append(number)
    else:  # თუ კენტია
        odd_numbers.append(number)

result_list = []
result_list += even_numbers
result_list += odd_numbers

print("შედეგი:", result_list)