import mysql.connector


def get_airport(countrycode):
    query = (f"select airport.type, count(*) from airport "
             f"where iso_country = '{countrycode}' group by airport.type;")
    #print(query)
    cursor = connection.cursor()
    cursor.execute(query)
    airports = cursor.fetchall()
    #print(airports)
    return airports


connection = mysql.connector.connect(
    host='127.0.0.1',
    port=3306,
    database='flight_game',
    user='root',
    password='053197',
    autocommit=True
)

airportType = {
    "heliport": "heliport",
    "small_airport": "small airport",
    "closed": "closed airport",
    "seaplane_base": "seaplane base",
    "balloonport": "balloonport",
    "medium_airport": "medium airport",
    "large_airport": "large airport"
}

print("This program prints out airport information according to country code.")
country = input("Enter country code to see airport information:")
results = get_airport(country)
if len(results) == 0:
    print("No matching data.")
else:
    print("The country has:")
    for result in results:
        info = f"{result[1]} {airportType[result[0]]}(s)"
        print(info)

