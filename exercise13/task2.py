from flask import Flask, render_template
import mysql.connector

app = Flask(__name__)

connection = mysql.connector.connect(
        host='127.0.0.1',
        port=3306,
        database='flight_game',
        user='root',
        password='053197',
        autocommit=True
    )


@app.route('/airport/<code>')
def get_airport(code):
    sql = ("select name, municipality from airport where ident= '" + code + "';")
    cursor = connection.cursor()
    cursor.execute(sql)
    info = cursor.fetchone()
    name = info[0]
    location = info[1]
    response = {"ICAO": code, "Name": name, "Location": location}
    return response


if __name__ == '__main__':
    app.run(use_reloader=True, host='127.0.0.1', port=5000)
