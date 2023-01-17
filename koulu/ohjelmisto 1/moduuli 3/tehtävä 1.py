#pyydetään pituutta ja verrataan onko lyhyempi vai pitempi kuin 37cm
len = input("Anna kuhan pituus senttimetreinnä: ")
if len <= str(36):
    print(f"Päästä kuha takaisin veteen. Kuha on {37 - int(len)} senttiä liian lyhyt")
else :
    print("Saat pitää kuhan")