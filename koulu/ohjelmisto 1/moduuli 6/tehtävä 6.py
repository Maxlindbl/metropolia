import math
def pizza(size, price):
    area = math.pi * (size / 2) ** 2 / 1000
    value = area / price
    return value

size1 = int(input("anna ekan pizzan halkaisija: "))
price1 = int(input("annan ekan pizzan hinta: "))
size2 = int(input("anna toisen pizzan halkaisija: "))
price2 = int(input("anna toisen pizzan hinta: "))

pizza1 = pizza(size1, price1)
pizza2 = pizza(size2, price2)

if pizza1 > pizza2:
    print("eka pizza on parempi")
    print(pizza1, pizza2)
else:
    print("toinen pizza on parempi")
    print(pizza1, pizza2)

