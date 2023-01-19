#kysytään vuotta ja lasketaan onko se karkausvuosi.
year = int(input("anna vuosiluku: "))
if year % 100 == 0:
    if year % 400 == 0:
        print("vuosi on karkausvuosi")
    else:
        print("vuoi ei ole karkausvuosi")
elif year % 4 == 0:
    print("vuosi on karkausvuosi")
else:
    print("vuosi ei ole karkausvuosi")