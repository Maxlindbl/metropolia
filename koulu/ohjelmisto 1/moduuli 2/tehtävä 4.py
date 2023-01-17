#lasketaan numeroiden summa, tulo ja keskiarvo

#pyydetään käyttäjältä numerot
num1 = input("ensinmäinen numero: ")
num2 = input("toinen numero: ")
num3 = input("kolmas numero: ")
n1 = float(num1)
n2 = float(num2)
n3 = float(num3)
#summataan, kerrotaan ja lasketaan keskiarvo luvut
summa= str((n1 + n2 + n3))
tulo = str((n1 * n2 * n3))
ka = str(((n1 + n2 + n3) / 3))
print("lukujen summa on: " + summa + " lukujen tulo on: " + tulo +" lukujen keskiarvo on: " + ka)