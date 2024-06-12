goa = "Goa is the best"

new_goa = ""


for char in range(len(goa)):
    if goa[char] != " ":
        new_goa += goa[char]

print(new_goa)