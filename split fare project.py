def split_fare(fare, passengers, feature_cost):

    share = fare/passengers
    print(f"Splitting the ${fare} fare between {passengers} passengers...")

    shared_cost = share + feature_cost
    print(f"Adding a ${feature_cost} feature cost...")
    return shared_cost


fare_cost = 118
passengers = 4
feature_cost = 0.7

shared_cost = split_fare(fare_cost, passengers, feature_cost)

print(f"Each pays: ${shared_cost}")

