person = {
    "name": "Alice",
    "age": 30,
    "city": "New York",
    "is_student": False,
    "skills": ["Python", "Data Analysis", "Machine Learning"],
    "address": {
        "street": "123 Main St",
        "zip_code": "10001"
    },
    "greet": lambda: "Hello, my name is Alice!"
}

person["age"] = 31
print(person["greet"]())
print(person)

person["address"]["zip_code"] = "10002" 

print(person["address"]["zip_code"])

person["skills"].append("Deep Learning")
print(person["skills"])


