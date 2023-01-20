names = set()

while True:
    name = input("anna nimi: ")
    if name == "":
        break
    if name in names:
        print("aiemmin syötetty nimi")
    else:
        print("uusi nimi")
        names.add(name)

print("antamasi nimet:")
for i in names:
    print(i)