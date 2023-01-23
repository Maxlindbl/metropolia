import mysql.connector
def airports(country):
    sql = "SELECT type FROM airport"
    sql += " WHERE iso_country='" + country + "'"
    #print(sql)
    cursor = connection.cursor()
    cursor.execute(sql)
    result = cursor.fetchall()
    calc = {i: result.count(i) for i in result}
    print(calc)
    return





connection = mysql.connector.connect(
         host='localhost',
         port= 3306,
         database='flight_game',
         user='max',
         password='password',
         autocommit=True
         )

country = input("anna lentokentän maatunnus: ")
airports(country)