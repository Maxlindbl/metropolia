number = int(input("anna luku: "))

if number == 1:
    print("luku ei ole alkuluku")
for i in range(2, number):
    if number % i == 0:
        print("luku ei ole alkuluku")
        break
else:
    print("luku on alkuluku")