cars = ['bmw', 'audi', 'toyota', 'subaru']
cars.sort()
print(cars)
car_type = ['bmw', 'audi', 'toyota', 'subaru']
car_type.sort(reverse = True)
print(car_type)

vehicle_type = ['bmw', 'audi', 'toyota', 'subaru']
print("\nHere is the original list:")
print(vehicle_type)
print("\nHere is the sorted list:")
print(sorted(vehicle_type))
print("\nHere is the original list again:")
print(vehicle_type)

#printing a list in the reverse order
vehicle_type.reverse()
print(vehicle_type)

numbers = list(range(1,11))
even_numbers = list(range(2,11,2))
print(numbers)
print(even_numbers)
