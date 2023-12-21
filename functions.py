carPortfolio = {
    "Chevrolet Tracker": 120,
    "Chevrolet Onix": 90,
    "Chevrolet Spin": 150,
    "Hyundai HB20": 85,
    "Hyundai Tucson": 120,
    "Fiat Uno": 60,
    "Fiat Mobi": 70,
    "Fiat Pulse": 130
}

rentedCar = {}

def menu():
    print("\nWhat do you want to do?")
    print("0 - Show portfolio | 1 - Rent car | 2 - Return car")


def showPortfolio(dic):
    print("=================")
    for index, (carName, value) in enumerate(dic.items()): 
        print(f"{[index]} {carName} - {value} / day")


def calculate(carCode, days):
    price = list(carPortfolio.values())
    currentPrice = price[carCode] * days
    return f"This will cost R$ {currentPrice}"

def removeCar(index):
    items = list(enumerate(carPortfolio.items()))
    carKey = items[index][1][0]
    carValue = items[index][1][1]
    carPortfolio.pop(carKey)
    rentedCar[carKey] = carValue
    print(f"Congratulations on renting the {carKey}!")

def returnCar(index):
    items = list(enumerate(rentedCar.items()))
    carKey = items[index][1][0]
    carValue = items[index][1][1]
    rentedCar.pop(carKey)
    carPortfolio[carKey] = carValue
    print(f"The {carKey} has been returned.")