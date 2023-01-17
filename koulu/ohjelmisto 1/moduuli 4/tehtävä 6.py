import math
#lasketaan pi:n likiarvo kokeilemalla eri lukuja osuvatko ympyrän vai neliön sisään
import random
i = 0
k = 0
numbers = int(input("anna arvioitavien pisteiden määrä: "))
#arvotaan numerot
while i <= numbers:
    x = random.uniform(-1,1)
    y = random.uniform(-1,1)
#lasketaan suorittaako luvut yhtälön
    calc = float(x**2+y**2<=1)
    i = i + 1
    if calc == True:
        k = k + 1
#verrataan osuneiden lukujen ja yrityssten määrää

ans = (4 * k) / i

print(f"piin likiarvo on : {ans}")



