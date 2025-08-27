# parent class 
class Smartphone:
    def __init__(self, brand, model, camera_megapixels):
        # Attributes
        self.brand = brand 
        self.model = model
        self.camera_megapixels = camera_megapixels

    def call(self, number):
        print(f"{self.brand} {self.model} is calling {number}...")

    def take_photo(self):
        print(f"{self.brand} {self.model} takes a photo with {self.camera_megapixels}MP camera.")
            

# child class inherits from smartphone
class SmartphoneWithCamera(Smartphone):
    def __init__(self, brand, model, camera_megapixels):
        # Call the constructor to reuse code
        super().__init__(brand.model)
        self.camera_megapixels = camera_megapixels

    def take_photo(self):
        print(f"{self.brand} {self.model} takes a {self.camera_megapixels}MP photo.")

# Create objects
phone1 = Smartphone("Pixel", "9", 50)
phone2 = Smartphone("Samsung", "S23 plus", 108)

# Use methods
phone1.call("123-456-7890")
phone2.call("987-654-3210")
phone1.take_photo()
phone2.take_photo()

# Activity 2: Polymorphism
class Vehicle:
    def move(self):
        # Default move method
        print("The vehicle is moving.")

class Car(Vehicle):
    def move(self):
        print("The car is driving on the road.")

class Plane(Vehicle):
    def move(self):
        print("Flying in the sky.")

class Boat(Vehicle):
    def move(self):
        print("Sailing on water")

vehicles = [Car(), Plane(), Boat()]
for v in vehicles:
    v.move()                
                    