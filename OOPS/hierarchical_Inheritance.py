class Vehicle: 
    def __init__(self, brand, model): 
        self.brand = brand 
        self.model = model 

    def display_info(self): 
        print(f"Brand: {self.brand}, Model: {self.model}")

class Car(Vehicle):
    def __init__(self, brand, model, num_doors): 
        super().__init__(brand, model) 
        self.num_doors = num_doors 

    def display_info(self): 
        super().display_info() 
        print(f"Number of doors: {self.num_doors}")

class Motorcycle(Vehicle):
    def __init__(self, brand, model, has_sidecar): 
        super().__init__(brand, model) 
        self.has_sidecar = has_sidecar 

    def display_info(self): 
        super().display_info() 
        print(f"Has sidecar: {self.has_sidecar}")

# Creating instances of Car and Motorcycle
car = Car("Toyota", "Camry", 4)
motorcycle = Motorcycle("Harley-Davidson", "Street 750", False)

# Displaying information about the vehicles
car.display_info()
print()
motorcycle.display_info()   