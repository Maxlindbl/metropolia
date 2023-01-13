year = int(input("anna vuosiluku: "))
if year % 4 == 0 or year % 400 == 0:
    print("vuosi on karkausvuosi")
else:
    print("vuosi ei ole karkausvuosi")