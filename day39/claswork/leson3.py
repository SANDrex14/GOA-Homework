number = int(input("შემოიტანე რიცხვი: "))
numbers_list = []

if number % 2 == 0: # ლუწია
    numbers_list.append("ლუწი")
else: # კენტია
    numbers_list.append("კენტი")

print(f"შენ შემოიტანე რიცხვი {number} და ეს რიცხვი არის {', '.join(numbers_list)}")



numbers = input("შემოიტანეთ რიცხვები გარკვეული სიად გამოყენებით ',': ").split(",")
numbers_list = []

for number in numbers:
    if int(number) % 2 == 0: # ლუწია
        numbers_list.append("ლუწი")
    else: # კენტია
        numbers_list.append("კენტი")

print(f"შენ შემოიტანე {', '.join(numbers)} და ეს რიცხვები არისააა: {', '.join(numbers_list)}")