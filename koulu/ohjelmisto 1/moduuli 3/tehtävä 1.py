len = input("Anna kuhan pituus senttimetreinnä: ")
dif= 37 - int(len)
if len <= str(36):
    print("Päästä kuha takaisin veteen kuha on " + str(dif) + " senttiä liian lyhyt")
else :
    print("Saat pitää kuhan")