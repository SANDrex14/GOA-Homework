# ფუნქცია, რომელიც აბრუნებს ორნიშნა რიცხვებს ციფრების სიაში გადაყვანილია
def split_two_digits(num):
    return [int(digit) for digit in str(num)]
    
numbers = []   # ცარიელი სია

# მანამ, რაც მომხმარებელს შემოტანილია რიცხვები
while True:
    num = input("შეიყვანეთ რიცხვი: ")
    
    # შევავსოთ ცარიელ სია რიცხვებით
    if num == "":
        break
    
    # რიცხვი გადაყვანილი იქნება ორნიშნა რიცხვებში
    digits = split_two_digits(int(num))
    if len(digits) == 2:
        numbers.append(digits)

print(f"შეტყობინება: სიაშია შექმნილი {len(numbers)} ცალი ორნიშნა რიცხვი: {numbers}")
