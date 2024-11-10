# Alex Miracle
# SDEV220-M03CaseStudy

# This program collects details about a car, including its year, make, model, number of doors, 
# and roof type. It then displays the information in a clear format.

# variables: 
# vehicle_type: stores the type of vehicle(car)
# year: stores the car's year
# make: Stores the car's make(brand)
# model: store the car's model
# door: stores the number of door 2 or 4
# roof: stores the type of roof solid or sunroof




# superclass 
class Vehicle:
    def __init__(self, vehicle_type):
        self.vehicle_type = vehicle_type

# subclass inherits from vehicle
class Automobile(Vehicle):
    def __init__(self, vehicle_type, year, make, model, doors, roof):
        super().__init__(vehicle_type)
        self.year = year
        self.make = make
        self.model = model
        self.doors = doors
        self.roof = roof

    # display vehicle information
    def display_info(self):
        print(f"Vehicle type: {self.vehicle_type}")
        print(f"Year: {self.year}")
        print(f"Make: {self.make}")
        print(f"Number of doors: {self.doors}")
        print(f"Type of roof: {self.roof}")

# main function to get user input and display data
def main():
    vehicle_type = "car"
    year = input("Enter the year of the car: ")
    make = input("Enter the make of the car: ")
    model = input("Enter the model of the car: ")
    doors = input("Enter the number of doors (2 or 4): ")
    roof = input("Enter the type of roof (solid or sunroof): ")

    
    car = Automobile(vehicle_type, year, make, model, doors, roof)

    car.display_info()

# run program
if __name__ == "__main__":
    main()
    