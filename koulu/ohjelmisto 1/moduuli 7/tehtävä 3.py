airports = {}
action = "ok"
while action != "Lopeta":
    action = input("Haluatko syöttää uuden lentokentän (Syötä), hakea syötetyn lentokentän tiedot (hakea) vai lopettaa (Lopeta): ")
    if action == "syötä":
        icao = input("syötä lentokentän icao koodi: ")
        name = input("Syötä lentokentän nimi: ")
        airports[icao] = name
    elif action == "hakea":
        search = input("syötä kentän icao koodi: ")
        if search in airports:
            print(f"icao {search} koodin kentän nimi on {airports[search]}")
        else:
            print("kenttää ei löytynyt")
    else:
        print("syötit väärän toiminnan, kokeile uudestaan")


