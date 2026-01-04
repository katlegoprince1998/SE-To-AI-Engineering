class Computer:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def start(self):
        return f"{self.brand} {self.model} is starting up."

    def shutdown(self):
        return f"{self.brand} {self.model} is shutting down."

    def battery_life(self):
        print("Battery life: 80%")

class Laptop(Computer):
    def __init__(self, brand, model, weight):
        super().__init__(brand, model)
        self.weight = weight

    def battery_life(self):
        print("Battery life: 10 hours")

class Desktop(Computer):
    def __init__(self, brand, model, form_factor):
        super().__init__(brand, model)
        self.form_factor = form_factor

    def battery_life(self):
        print("Battery life: N/A (requires constant power supply)")

# Example usage

laptop = Laptop("Dell", "XPS 13", "1.2 kg")
desktop = Desktop("HP", "Pavilion", "Tower")

for device in (laptop, desktop):
    print(device.start())
    device.battery_life()
    print(device.shutdown())
    print()