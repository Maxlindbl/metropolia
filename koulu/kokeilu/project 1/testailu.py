leiviska = input("anna leiviskät: ")
naula = input("anna naulat: ")
luoti = input("anna luodit: ")

leiv = float(leiviska)*20
naul = (float(naula) + leiv) * 32
luot = (float(luoti) + naul) * 13.3
kg = luot / 1000
gramma = luot % 1000

print(int(kg))
print(int(gramma))