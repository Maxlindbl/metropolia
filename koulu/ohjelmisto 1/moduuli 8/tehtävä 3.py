import mysql.connector
from geopy.distance import geodesic as GD
def location_first(icao_first):
    sql = "SELECT latitude_deg, longitude_deg FROM airport"
    sql += " WHERE ident='" + icao_first + "'"
    #print(sql)
    cursor = connection.cursor()
    cursor.execute(sql)
    result = cursor.fetchall()
# mitä tehdään tuloksilla
    #print(result)
    return result

def location_second(icao_second):
    sql = "SELECT latitude_deg, longitude_deg FROM airport"
    sql += " WHERE ident='" +icao_second + "'"
    #print(sql)
    cursor = connection.cursor()
    cursor.execute(sql)
    result = cursor.fetchall()
# mitä tehdään tuloksilla
    #print(result)
    return result




connection = mysql.connector.connect(
         host='localhost',
         port= 3306,
         database='flight_game',
         user='max',
         password='password',
         autocommit=True
         )
icao_first = input("anna ensinmäisen kentän icao koodi: ")
icao_second = input("anna toisen kentän icao koodi: ")


location_first(icao_first)
location_second(icao_second)
print(f"kenttien välinen etäisyyss on {round(GD(location_first(icao_first),location_second(icao_second)).km,4)} km")