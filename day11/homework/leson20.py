#2)მომხარებელს შემოატანინეთ მშობლების ასაკი, დედის და მამის ასაკი, შემდეგ თუ დედის ასაკი მეტი იქნება მამის ასაკზე
#        დაგვიბეჭდოს რომ დედა დიდი მამაზე, თუ პირიქით მამის ასაკი მეტი იქნება დედის ასაკზე მაგ შემთხვევაში დაგვიბეჭდოს 
#        რომ მამა დიდია დედაზე. მინიშნება დაგჭირდებათ (if)

print("tu gainteresebs dadasheni ufro didia tu mamasheni")
print("upasuxe qvemot mocemul kitxvebs:) ")
user_kitxva = input("tanaxma xar: ")

user_age1 = input("semoiyvane dedis asaki: ")
user_age2 = input("semoiyvane mamis asaki: ")

if user_age1 > user_age2:
    print("dedasheni ufro didia mamashenze")

if user_age1 < user_age2:
    print("mamasheni ufro didia dedashenze")
    