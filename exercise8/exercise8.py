import mysql.connector


def get_airport(code):
    query = ("select airport.name, municipality from airport where ident = '" + code + "';")
    # print(query)
    cursor = connection.cursor()
    cursor.execute(query)
    airport = cursor.fetchone()
    try:
        info = f"{code} is {airport[0]}. It is located in {airport[1]}."
        print(info)
    except TypeError:
        print("Airport not found.")
    return


connection = mysql.connector.connect(
    host='127.0.0.1',
    port=3306,
    database='flight_game',
    user='root',
    password='053197',
    autocommit=True
)

print("This program looks up airport information from database.")
airport_code = input("Enter ICAO code:")
get_airport(airport_code)



