class Superhero:
  def __init__(self, name, power):
    self.name = name
    self.power = power

  def use_power(self):
    print(f"{self.name} uses {self.power}!")

  def introduce(self):
    print(f"Hello, I'm {self.name} and my power is {self.power}.")

class FlyingSuperhero(Superhero):
  def __init__(self, name, power, flight_speed):
    super().__init__(name, power)
    self.flight_speed = flight_speed

  def fly(self):
    print(f"{self.name} is flying at {self.flight_speed} mph!")

  # Override the use_power method
  def use_power(self):
    print(f"{self.name} is using {self.power} while flying!")

# Create a Superhero object
superman = FlyingSuperhero("Superman", "flight", 1000)

class Vehicle:
  def move(self):
    pass

class Car(Vehicle):
  def move(self):
    print("Driving 🚗")

class Plane(Vehicle):
  def move(self):
    print("Flying ✈️")

# Create instances of the classes
my_car = Car()
my_plane = Plane()

# Call the move() method on each instance
my_car.move()
my_plane.move()
