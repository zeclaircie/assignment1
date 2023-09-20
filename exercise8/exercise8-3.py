import mysql.connector
from geopy import distance


def get_distance(code1, code2):
    query1 = f"select latitude_deg, longitude_deg from airport where ident = '{code1}';"
    #print(query1)
    query2 = f"select latitude_deg, longitude_deg from airport where ident = '{code2}';"
    #print(query2)
    cursor = connection.cursor()
    cursor.execute(query1)
    point1 = cursor.fetchone()
    cursor.execute(query2)
    point2 = cursor.fetchone()
    if len(point1) != 0 and len(point2) != 0:
        dst = distance.distance(point1, point2).km
        return dst




connection = mysql.connector.connect(
    host='127.0.0.1',
    port=3306,
    database='flight_game',
    user='root',
    password='053197',
    autocommit=True
)

code1 = input("Enter ICAO code of airport 1:")
code2 = input("Enter ICAO code of airport 2:")
try:
    print(f"The distance between them is {get_distance(code1, code2)} kilometers.")
except TypeError:
    print("One or both of the airport is unknown.")


