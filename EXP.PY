print("welcome to the trip distance")
distance =float(input("what was the total distance? (km or miles):"))
efficiency = float(input("what was the fuel efficiency? (km/l or mpg):"))
fuel_price = float(input("what was the fuel price? (liter/gallon):"))
num_people = int(input("how many people are sharing the cost?"))
total_fuel_needed = distance / efficiency
total_fuel_cost = total_fuel_needed * fuel_price
cost_per_person = total_fuel_cost / num_people
print("trip cost details:")
print("total fuel needed:", round(total_fuel_needed, 2))
print("total fuel cost:", round(total_fuel_cost, 2))
print("cost per person:", round(cost_per_person, 2))