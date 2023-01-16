values = []

while True:
    numbers = input("Anna luku tai kun haluat lopettaa paina enter: ")
    if numbers =="":
        break
    values.append(int(numbers))

values.sort(reverse=True)
for i in range(5):
    print(values[i])


