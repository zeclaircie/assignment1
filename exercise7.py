# ask user for the month and output the corresponding season
seasonIndex = ((3, 4, 5), (6, 7, 8), (9, 10, 11), (12, 1, 2))
seasons = ("Spring", "Summer", "Autumn", "Winter")
try:
    month = int(input("What's the month? Enter integers 1-12."))
    if 1 <= month <= 12:
        for i, index in enumerate(seasonIndex):
            if month in index:
                season = f"It is {seasons[i]}."
                print(season)
    else:
        print("Invalid input.")
except ValueError:
    print("Invalid input.")

# enter names, check names, and print names
names = set()
try:
    while True:
        inputName = input("Enter a name, or enter a space to exit.")
        if inputName == " ":
            break
        if inputName in names:
            print("Existing name!")
        else:
            print("New name! Adding to name list.")
            names.add(inputName)
    print("The names are:")
    for name in names:
        print(name)
except ValueError:
    print("Invalid input.")


# fetching and storing airport data
airports = {
    "LOWW": "Vienna Airport",
    "EBBR": "Brussels Airport",
    "EKCH": "Copenhagen Airport",
    "EETN": "Tallinn Airport",
    "EFHK": "Helsinki Airport",
    "EFRO": "Rovaniemi Airport",
    "LFPG": "Paris Charles de Gaulle Airport"
}


def add_airport():
    ICAO = input("Enter the ICAO code:")
    airport = input("Enter the airport name:")
    airports[ICAO] = airport
    print(f"Airport {ICAO} has been added to the database.")
    return airport


def check_airport():
    try:
        ICAO = input("Enter the ICAO code:")
        found = airports[ICAO]
        print(f"Airport found: {found}")
    except KeyError:
        print("The airport has not been added to the database yet.")


while True:
    toDo = input("Enter number to continue:\n"
                 "1. Enter a new airport\n"
                 "2. Fetch airport information\n"
                 "3. Quit\n")
    if toDo == "1":
        add_airport()
    elif toDo == "2":
        check_airport()
    elif toDo == "3":
        break
    else:
        print("Please enter a valid number!")
        break



