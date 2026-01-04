cars = ["Toyota", "Honda", "Ford", "Chevrolet"]

# Accessing elements by index
first_car = cars[0]
second_car = cars[1]
last_car = cars[-1]

print("First car:", first_car)
print("Second car:", second_car)
print("Last car:", last_car)

# Slicing the list
first_two_cars = cars[0:2]
last_two_cars = cars[-2:]
print("First two cars:", first_two_cars)
print("Last two cars:", last_two_cars)

# Modifying elements
cars[2] = "Nissan"
print("Modified cars list:", cars)

# Adding elements
cars.append("BMW")
print("After appending BMW:", cars)

cars.insert(1, "Audi")
print("After inserting Audi at index 1:", cars)

# Removing elements
cars.remove("Honda")
print("After removing Honda:", cars)

popped_car = cars.pop()
print("Popped car:", popped_car)
print("After popping the last car:", cars)

# Length of the list
length = len(cars)
print("Number of cars in the list:", length)

# Iterating through the list
print("Cars in the list:")
for car in cars:
    print(car)

# Checking for existence
has_ford = "Ford" in cars
print("Is Ford in the list?", has_ford)

# Sorting the list
cars.sort()
print("Sorted cars list:", cars)

# Reversing the list
cars.reverse()
print("Reversed cars list:", cars)

# Copying the list
cars_copy = cars.copy()
print("Copied cars list:", cars_copy)

# Clearing the list
cars.clear()
print("Cleared cars list:", cars)
print("Cars list after clearing:", cars)

