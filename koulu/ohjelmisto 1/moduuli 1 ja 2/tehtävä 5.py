leiviska = input("anna leiviskät: ")
naula = input("anna naulat: ")
luoti = input("anna luodit: ")

naul = float(leiviska)*20
luot = (float(naula) + naul) * 32
gramma = (float(luoti) + luot) * 13.3

kg = int(gramma / 1000)
gr = int(gramma % 1000)

print("sinulla on " + str(kg) + " kiloa ja " + str(gr) + " grammaa")
