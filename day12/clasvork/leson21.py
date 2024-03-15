#1) მომხმარებელს შემოატანინეთ ტესტში მიღებული ქულა, თუ ქულა მეტია 90 - ზე და ნაკლებია 100 - ზე 
    #მაგ შემთხვევაში დაპრინტეთ, თქვენ დაგიფინანსდებათ სწავლა სრულიად. თუ მიღებული ქულა მეტია 70 - ზე და  
    #ნაკლებია 80 - ზე მაგ შემთხვევაში დაპრინტეთ, თქვენ დაგიფინანსდებათ სწავლა 1500 ლარით, თუ მიღებული ქულა მეტია 40 -  ზე და ნაკლებია 70 - ზე 
    #მაგ შემთხვევაში დაპრინტეთ, თქვენ დაგიფინანსდებათ სწავლა 500 ლარტით, ხოლო თუ მიღებული ქულა ნაკლებია 40 ზე, მაგ შემტხვევაში დაპრინტეთ, 
    #ტქვენ არ დაგიფინანსდებათ სწავლის პროცესი (edited)





print("seni nisnebis gamotvlit gaigeb caabare tu ara")

user_kitxva = int(input("ra miige: "))


if user_kitxva > 90 and user_kitxva < 100:
    print("tqven dagipinansdat swavla srulad")

elif user_kitxva :
    print(" tqven dagipinansdat swavla srulad")


    print("tqven dagipinansdat swavla 1 500 larit")
elif user_kitxva > 80 and user_kitxva < 90:
    print("tqven dagipinansdat swavla 1 500 larit")


    print("tqven dagipinansdat swavla 1 000 larit")
elif user_kitxva  > 70 and user_kitxva < 80:
    print("yocag")


    print("tqven dagipinansdat swavla 500 larit")
elif user_kitxva  > 60 and user_kitxva < 70:
    print("kargia")


    print("tqven dagipinansdat swavla 200 larit")
elif user_kitxva  < 50 and user_kitxva > 60:
    print("araushavs gamoasworeb")


    print("tqveni dapinanseba ver miiget:)")
else:
    print("shemdegshi gamoasworeb")