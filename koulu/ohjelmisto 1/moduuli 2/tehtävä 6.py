import random
#luodaan käyttäjälle 2 uniikkia koodia
fnro1 = str(random.randint(0,9))
fnro2 = str(random.randint(0,9))
fnro3 = str(random.randint(0,9))
snro1 = str(random.randint(1,6))
snro2 = str(random.randint(1,6))
snro3 = str(random.randint(1,6))
snro4 = str(random.randint(1,6))

fcode = fnro1 + fnro2 + fnro3
scode = snro1 + snro2 + snro3 +snro4
print("sinun ensinmäinen koodisi on: " + fcode + " sinun toinen koodisi on: " + scode)
