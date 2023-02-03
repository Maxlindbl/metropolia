import mysql.connector

def airports(icao):
    sql = "SELECT name, municipality FROM airport"
    sql += " WHERE ident='" + icao + "'"
    #print(sql)
    kursori = yhteys.cursor()
    kursori.execute(sql)
    tulos = kursori.fetchall()
    if kursori.rowcount >0 :
        for rivi in tulos:
            print(f"kenttä on nimeltään {rivi[0]}. ja se sijaitsee:  {rivi[1]}.")
    return

yhteys = mysql.connector.connect(
         host='localhost',
         port= 3306,
         database='flight_game',
         user='max',
         password='password',
         autocommit=True
         )
icao = input("Anna lentokentän icao koodi: ")
airports(icao)