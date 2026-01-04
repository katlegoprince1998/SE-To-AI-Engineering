class Address:
    def __init__(self, street, city, state, zip_code):
        self.__street = street
        self.__city = city
        self.__state = state
        self.__zip_code = zip_code

    def get_street(self):
        return self.__street

    def set_street(self, street):
        self.__street = street

    def get_city(self):
        return self.__city

    def set_city(self, city):
        self.__city = city

    def get_state(self):
        return self.__state

    def set_state(self, state):
        self.__state = state

    def get_zip_code(self):
        return self.__zip_code

    def set_zip_code(self, zip_code):
        self.__zip_code = zip_code

    def __str__(self):
        return f"{self.__street}, {self.__city}, {self.__state} {self.__zip_code}"
    
# Example usage:
if __name__ == "__main__":
    address = Address("123 Main St", "Springfield", "IL", "62701")
    print(address)  # Output: 123 Main St, Springfield, IL 62701

    address.set_city("Chicago")
    print(address.get_city())  # Output: Chicago

    print(address)  # Output: 123 Main St, Chicago, IL 62701