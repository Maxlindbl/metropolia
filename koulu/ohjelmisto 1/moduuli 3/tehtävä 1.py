len = input("Anna kuhan pituus senttimetreinnä: ")
if len <= str(36):
    print(f"Päästä kuha takaisin veteen. Kuha on {37 - int(len)} senttiä liian lyhyt")
else :
    print("Saat pitää kuhan")