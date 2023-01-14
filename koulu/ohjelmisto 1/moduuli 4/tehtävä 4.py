import random
num = random.randint(1,10)
while True:
    guess = int(input("arvaa luku: "))
    if guess == num:
        print("arvasit oikein")
        break
    elif guess <= num:
        print("liian pieni arvaus")
    elif guess >= num:
        print("liian iso arvaus")