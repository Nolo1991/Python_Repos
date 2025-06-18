city_flight = (input("Which city you flighting to:  "))

number_nights = int(input("Enter the number of nights you will be staying: "))
rental_days = int(input("Enter the number of days you want to rent a car: "))

def plane_cost(city_flight):
    if city_flight == "Paris":
        return 10000
    elif city_flight == "New York":
        return 1200
    elif city_flight == "Maurituus":
        return 1300
    else:
        return ("Please enter a valid City")


def hotel_cost(number_nights):
    cost = 500
    return number_nights * cost

def car_rental(rental_days):
    car_cost = 300
    return rental_days * car_cost

flight_price = plane_cost(city_flight)
hotel_price = hotel_cost(number_nights)
car_price = car_rental(rental_days)

print(f"City: {city_flight}")
print(f"Flight to {city_flight}: {flight_price}")
print(f"Hotel for {number_nights} nights: {hotel_price}")
print(f"Car rental for {rental_days} days: {car_price}")

