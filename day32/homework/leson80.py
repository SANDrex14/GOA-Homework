goa_is_the_best = ""

for index, char in enumerate(goa_is_the_best):
    if char == " ":
        goa_is_the_best = goa_is_the_best[:index] + " " + goa_is_the_best[index:]
        break

print(goa_is_the_best)


