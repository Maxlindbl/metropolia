#kysytään hyttiluokkaa. verrataan annettuihin luokkiin ja tulostetaan selitys luokasta
clas = input("anna hyttiluokkasi: ")

if clas == "LUX" or clas == "lux":
    print("LUX on parvekkeellinen hytti yläkannella.")
elif clas == "A" or clas == "a":
    print("A on ikkunallinen hytti autokannen yläpuolella.")
elif clas == "B" or clas == "b":
    print("B on ikkunaton hytti autokannen yläpuolella.")
elif clas == "C" or clas == "b":
    print("C on ikkunaton hytti autokannen alapuolella.")
else:
    print("virheellinen luokka")