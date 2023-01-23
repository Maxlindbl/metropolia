airports = {}
action = "ok"

def add():
    icao = input("syötä lentokentän icao koodi: ")
    name = input("Syötä lentokentän nimi: ")
    airports[icao] = name
    return
def search():
    search = input("syötä kentän icao koodi: ")
    if search in airports:
        print(f"icao {search} koodin kentän nimi on {airports[search]}")
    else:
        print("kenttää ei löytynyt")
    return


while action != "Lopeta":
    action = input("Haluatko syöttää uuden lentokentän (Syötä), hakea syötetyn lentokentän tiedot (hakea) vai lopettaa (Lopeta): ")
    if action == "syötä":
        add()
    elif action == "hakea":
        search()
    elif action == "Lopeta":
        print("kiitos ja näkemiin")
        break
    else:
        print("syötit väärän toiminnan, kokeile uudestaan")