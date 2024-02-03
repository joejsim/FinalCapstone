# Give the user the destination options
cities = ["Paris", "Berlin", "New York", "Madrid"]
print(cities)

# Ask the user to select a location from the list
while True:
    city_flight = input("Select which city you want to fly to from the list above: ").capitalize().strip()
    if city_flight in cities:
        break
    else:
        print("We do not fly here. Please enter a city we fly to")

# Get the mumber of nights the user will be staying at the hotel and deal with user not entering a positive whole number of nights
while True:
    try:
        num_nights = float(input("How many nights will you be staying at the hotel? "))
        if num_nights >= 0 and num_nights % 1 == 0:  # Check if it's a whole number
            break
        else:
            print("Please enter a whole number of nights (no decimals) greater than or equal to 0")
    except ValueError:
        print("Please enter a whole number of nights greater than or equal to 0")

# Now get the number of days the user wants to rent a car for
while True:
    try:
        rental_days = float(input("How many days will you be hiring a car for? "))
        if rental_days >= 0 and rental_days % 1 == 0:
            break
        else:
            print("Please enter a whole number of days greater than or equal to 0")
    except ValueError:
        print("Please enter a whole number of days greater than or equal to 0")

# Create a function that works out the cost of the hotel
def hotel_cost(x):
    return 108*x

# Create a function that works out the cost of the flight. This is dependent on where the user chooses to go to.
def plane_cost(x):
    if x == "Paris":
        return 200
    elif x == "Berlin":
        return 160
    elif x == "New York":
        return 600
    else :
        return 190
   
        
# Create a function that works out the cost of the car rental
def car_rental(x):
    return 30*x

# Create a function that works out the total cost of the holiday
def holiday_cost(hotel_cost,plane_cost,car_rental):
    return hotel_cost+plane_cost+car_rental


# Now print the details
print(f"The hotel will cost £{hotel_cost(num_nights)}, the plane ticket will cost £{plane_cost(city_flight)} and the car will cost £{car_rental(rental_days)}.")
print(f"This comes to a total of £{holiday_cost(hotel_cost(num_nights),plane_cost(city_flight),car_rental(rental_days))}")
