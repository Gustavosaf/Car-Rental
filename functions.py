car_portfolio = {
    "Chevrolet Tracker": 120,
    "Chevrolet Onix": 90,
    "Chevrolet Spin": 150,
    "Hyundai HB20": 85,
    "Hyundai Tucson": 120,
    "Fiat Uno": 60,
    "Fiat Mobi": 70,
    "Fiat Pulse": 130
}

rented_car = {}

def menu():
    print("What do you want to do?\n")
    print("0 - Show portfolio | 1 - Rent car | 2 - Return car | 3 - Exit program")


def show_portfolio(dictionary, show_values):
    print("=================\n")
    for index, (car_name, car_value) in enumerate(dictionary.items()): 
        if show_values:
            print(f"{[index]} {car_name} - {car_value} / day")
        else:
            print(f"{[index]} {car_name}")


def calculate(car_code, days):
    car_value = list(car_portfolio.values())
    current_price = car_value[car_code] * days
    return f"This will cost R$ {current_price}"


def remove_car(index):
    items = list(enumerate(car_portfolio.items()))
    car_key_selected = items[index][1][0]
    car_value_selected = items[index][1][1]
    car_portfolio.pop(car_key_selected)
    rented_car[car_key_selected] = car_value_selected 
    print(f"Congratulations on renting the {car_key_selected}!")


def return_car(index, current_price): #current_price
    items = list(enumerate(rented_car.items()))
    car_key_selected = items[index][1][0]
    car_value_selected = items[index][1][1]
    rented_car.pop(car_key_selected)
    car_portfolio[car_key_selected] = car_value_selected
    print(f"The {car_key_selected} has been returned and it {current_price}.")