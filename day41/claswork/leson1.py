number = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
number_list = []

for i in range(len(number)):
    number_list.append(number[-i-1])

print(number_list)