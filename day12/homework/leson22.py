#მოსწავლეს შემოატანინეთ სკოლის ტესტში მიღებული ნიშანი, თუ ეს მიღებული ნიშანი უდრის 10 - ს, მაგ შემთხვევაში მასწავლებელმა,
# მშობელთან შეაქოს მოსწავლე, თუ მიღებული ნიშანი უდრის 8 -ს ან 9 - ს, მაგ შემთხვევაში, მასწავლებელმა, მშობელს პატარა შენიშვნა მისცეს. 
#თუ მიღებული ქულა უდრის 5  - ს მაგ შემთხვევაში, მასწავლებელმა, მშობელს მისცეს შენიშვნა, 
#ხოლო თუ მიღებული ნიშანი ნაკლებია 5 ზე, მაგ შემთხვევაში, მასწავლებელმა გააგდოს მოსწავლე სკოლიდან

print("gamargoba me var mexute sajaro skolis direqtor")
user_nisani = int(input("ra nisani miigo tqvenma svilma gakvetilze?: "))




if user_nisani < 10:
    print("kargi bavsvia")
elif  user_nisani:
   print("zalian yocagi bavsvi gyavs")


   print("cota metia sawiro")
elif user_nisani  < 9:
    print("cota metia sawiro")

    print("")
elif  user_nisani < 8 :
    print("metia sawiro magali nisnistvis ")

    print("")
elif  user_nisani > 5 :
    print("seuzlia magram ar sveba zalian uyuradgebot aris")

elif  user_nisani < 5 :
    print("GAGDEBULI XAR SKOLIDAN")
