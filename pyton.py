name = input("რომელ აკადემიაში სწავლობ:")       #davaleba (1)
if name == "GOA":
    print ("სწორ აკადემიაშ სწავლობ")
else: 
    print ("join GOA")     

#------------------------------------------------------------------------

price = 4200 
game = int(input ("how much money do you have: "))   #davaleba (2)
if game >= price: 
    print ("კი შენ გყოფნის ფული")
else: 
    print ("შენ არ გუოფნის ფული")

#------------------------------------------------

num = int(input("შეიყავენ შენი ციფრი: "))         #davaleba (3)

if num >= 5:
    print(num *2)
else:
    print("ok")

#--------------------------------------------

num = int(input("შემოიტანე რიცხვი:"))           #davaleba (4)

ticket = 10

if num <5:
    total_price = num * ticket
else:
    discount_price = ticket * 0.7
    total_price = num * discount_price
print(total_price)

#--------------------------------------------

num1 = int(input("შეიყანე რიცხვი1: "))         #davaleba (5)

num2 = int(input("შეიყანე რიცხვი2: "))

what_you_need = input("choose corecrt(+,-,/,): ")

if what_you_need == "+":
    result = num1 + num2
elif what_you_need == "":
    result = num1 * num2
elif what_you_need == "/":
   result = num1 // num2
elif what_you_need == "-":
    result = num1 - num2
else:
    result = "incortect"

print("პასუხი: ",result)































