i = 1
while i <= 5:
    if input("käyttäjätunnus: ") == "python" and input("salasana: ") == "rules":
        print("tervetuloa")
        break
    elif i > 5:
        break
    i = i + 1
