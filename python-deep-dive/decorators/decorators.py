def my_decorator_1(func):
    def wrapper():
        print("I am about to call the function.")
        func()
        print("I have called the function.")
    return wrapper

def say_hello():
    print("Hello!")

decorated_say_hello = my_decorator_1(say_hello)

decorated_say_hello()  # This will print messages before and after calling say_hello

@my_decorator_1
def say_goodbye():
    print("Goodbye!")

say_goodbye()  # This will also print messages before and after calling say_goodbye

def my_decorator_2(func):
    def wrapper(name):
        print(f"Preparing to greet {name}.")
        func(name)
        print(f"Greeted {name}.")
    return wrapper

@my_decorator_2
def greet(name):
    print(f"Hello, {name}!")

greet("Alice")  # This will print messages before and after greeting Alice


def my_decorator_3(func):
    def wrapper(*args, **kwargs):
        print("Starting the function with arguments:", args, kwargs)
        result = func(*args, **kwargs)
        print("Function finished executing.")
        return result
    return wrapper

@my_decorator_3
def add(a, b):
    return a + b    

result = add(3, 5)  # This will print messages before and after adding

print("Result of add:", result)

def my_decorator_4(func):
    def wrapper(*args, **kwargs):
        print("Before function call.")
        result = func(*args, **kwargs)
        print("After function call.")
        return result
    return wrapper

@my_decorator_4
def multiply(a, b):
    return a * b    

result = multiply(4, 6)  # This will print messages before and after multiplying
print("Result of multiply:", result)
