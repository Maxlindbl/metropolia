import random
#arvotaan nopan numero
def noppa():
    value = random.randint(1,6)
    return value
#tulostetaan nopan nopan nro: jos 6 lopetetaan ohjelma
while True:
    number = noppa()
    print(f"sait {number}")
    if number == 6:
        break

