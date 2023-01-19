def value(gallon):
    ans = gallon * 3.78
    return ans

while True:
    gallon = float(input("anna gallonat: "))
    if gallon <= 0:
        break
    else:
        print(value(gallon))