fruits = ("apple", "banana", "cherry")  # A tuple containing three fruit names

# Accessing elements in the tuple
first_fruit = fruits[0]  # Accessing the first element
second_fruit = fruits[1]  # Accessing the second element
last_fruit = fruits[-1]  # Accessing the last element
print("First fruit:", first_fruit)
print("Second fruit:", second_fruit)
print("Last fruit:", last_fruit)

# Attempting to modify an element in the tuple (will raise an error)
try:
    fruits[0] = "orange"  # This will raise a TypeError
except TypeError as e:
    print("Error:", e)      

# Tuple unpacking
fruit1, fruit2, fruit3 = fruits
print("Unpacked fruits:", fruit1, fruit2, fruit3)   

# Nested tuple  

nested_tuple = (1, 2, (3, 4), 5)
print("Nested tuple:", nested_tuple)
print("Accessing nested element:", nested_tuple[2][1])  # Accessing element '4' from the nested tuple   

# Tuple methods
count_banana = fruits.count("banana")  # Counting occurrences of 'banana'
index_cherry = fruits.index("cherry")  # Finding index of 'cherry'
print("Count of 'banana':", count_banana)
print("Index of 'cherry':", index_cherry)

# Single-element tuple
single_element_tuple = ("only_one",)
print("Single-element tuple:", single_element_tuple)

# Tuple concatenation
more_fruits = ("date", "elderberry")
all_fruits = fruits + more_fruits
print("Concatenated tuple:", all_fruits) 

# Tuple repetition
repeated_fruits = fruits * 2
print("Repeated tuple:", repeated_fruits)

# Length of the tuple
tuple_length = len(fruits)
print("Length of the tuple:", tuple_length)

# Iterating through the tuple
print("Iterating through the tuple:")
for fruit in fruits:
    print(fruit)

