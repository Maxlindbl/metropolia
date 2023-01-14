numbers = []
while True:
    num = input("anna luku. lopettaaksesi laita tyhjä luku: ")
    if num == "":
        print(f"suurin lukusi on {max(numbers)} pienin lukusi on {min(numbers)}")
        break
    numbers.append(num)
