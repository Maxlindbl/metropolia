import random
#nopan sivut luodaan käyttäjän pyynnön mukaan
def dice(value):
    random_number = random.randint(1,value)
    return random_number

#tulostetaan nopan arvo kunnes saadaan isoin silmäluku
value = int(input("montako sivua nopassa?: "))
while True:
    number = dice(value)
    print(f"sait {number}")
    if number == value:
        break
