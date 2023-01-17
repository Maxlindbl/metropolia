sex = input("Anna sukupuolesi: ")
hg = int(input("anna hemoglobiini arvosi (g/l): "))
#kyssytään sukupuolta sekä hemoglobiini arvoa. verrataan annettuja arvoja viitearvoihin
if sex == "nainen" or sex == "Nainen" or sex == "n" or sex == "N":
    if hg <= 117:
        print("hemoglibiinisi on alhainen")
    elif  hg >= 175:
        print("hemoglibiinisi on korkea")
    else:
        print("hemoglibiinisi on normaali")

if sex == "mies" or sex == "Mies" or sex == "m" or sex == "M":
    if hg <= 134:
        print("hemoglibiinisi on alhainen")
    elif  hg >=95:
        print("hemoglibiinisi on korkea")
    else:
        print("hemoglibiinisi on normaali")
#jos annetaan  väärät arvot.
else:
    print("väärä sukupuoli tai arvo")