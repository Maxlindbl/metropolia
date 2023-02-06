import mysql.connector
from flask import Flask, request, jsonify

app = Flask(__name__)
app.config['JSON_SORT_KEYS'] = False

def get_airport_data(icao):
    sql = "SELECT name, municipality FROM airport"
    sql += " WHERE ident='" + icao + "'"
    #print(sql)
    kursori = yhteys.cursor()
    kursori.execute(sql)
    tulos = kursori.fetchall()


    return tulos

yhteys = mysql.connector.connect(
         host='localhost',
         port= 3306,
         database='flight_game',
         user='max',
         password='password',
         autocommit=True
         )


@app.route("/kenttä/<icao>")
def answer(icao):
    airport_data = get_airport_data(icao)
    if airport_data is not None:
        response = {
            "ICAO": icao,
            "Name": airport_data[0][0],
            "Municipality": airport_data[0][1]
        }
        return jsonify(response)
    else:
        return jsonify({"error": "No data found for ICAO code " + icao})

if __name__ == "__main__":
    app.run(use_reloader=True, host = '127.0.0.1', port=3000)



