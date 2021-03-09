#1. Create a Vehicle class with max_speed and mileage instance attributes
class Vehicle:

    def __init__(self, max_speed, mileage):
        self.max_speed = max_speed
        self.mileage = mileage

    def print_vehicle(self):
        print(f'Car specifications: maximum speed {self.max_speed} and mileage {self.mileage}')


car = Vehicle("120 km/h", "1000 km")
car.print_vehicle()

#2. Create a child class Bus that will inherit all of the variables and methods of the Vehicle class
# and will have seating_capacity own method


class Bus(Vehicle):

    def __init__(self, max_speed, mileage, sitting_capacity):
        super().__init__(max_speed, mileage)
        self.max_speed = max_speed
        self.mileage = mileage
        self.sitting_capacity = sitting_capacity

    def seat_capacity(self, sitting_capacity):
        self.sitting_capacity = sitting_capacity

    def seating(self):
        print(f'A bus has {self.sitting_capacity} seating.')


bus = Bus('160 km/h', '3000 km', 42)
bus.print_vehicle()
bus.seating()


#3. Determine which class a given Bus object belongs to (Check type of an object).

school_bus = Bus('90 km/h', '800 km', 23)
print(type(Bus))

#4. Determine if School_bus is also an instance of the Vehicle class:

print(isinstance(school_bus, Vehicle))

#5. Create a new class School with get_school_id and number_of_students instance attributes:


class School:
    def __init__(self, get_school_id, number_of_students):
        self.get_school_id = get_school_id
        self.number_of_students = number_of_students

    def student(self):
        print(f'My number_of_students is {self.number_of_students} and get_school_id is {self.get_school_id}')


school = School("123456", "25")
school.student()

#6*. Create a new class SchoolBus that will inherit all of the methods from School and Bus and
# will have its own - bus_school_color:


class SchoolBus(School, Bus):

    def __init__(self, get_school_id, number_of_students, max_speed, mileage, sitting_capacity,
                 bus_school_color):
        School.__init__(self, get_school_id,number_of_students)
        Bus.__init__(self, max_speed, mileage, sitting_capacity)
        self.bus_school_color = bus_school_color

    def bus_color(self):
        print(f'My bus school color is: {self.bus_school_color}')


school_bus = SchoolBus(123456, 25, 120, 1000, 3, "Green")
school_bus.bus_color()

#7. Polymorphism: Create two classes: Bear, Wolf. Both of them should have make_sound method.
# Create two instances, one of Bear and one of Wolf,
#make a tuple of it and by using for call their action using the same method.


class Bear:

    def __init__(self, name):
        self.name = name

    def make_sound(self):
        print(f'Bear {self.name} said gr-gr-gr.')


    def about_me(self):
        print("I'm a bear.")


class Wolf:
    def __init__(self, name):
        self.name = name

    def make_sound(self):
        print(f'Wolf {self.name} said puff-puff')

    def about_me(self):
        print("I'm a wolf.")


bear = Bear('Umka')
wolf = Wolf('Akella')

for animal in (bear, wolf):
    animal.about_me()
    animal.make_sound()


#8 Magic methods: Create class City with name, population instance attributes, return a new instance only
# when population > 1500, otherwise return message: "Your city is too small".
#9. Override a printable string representation of the City class and return:
# The population of the city {name} is {population}

class City:

    def __init__(self, name, population):
        self.name = name
        self.population = population

    def __new__(cls, name, population):
        instance = super(City, cls).__new__(cls)
        if population > 1500:
            return instance
        else:
            return f'Your city is too small.'


    def __str__(self):
        return f'The population of the city {self.name} is {self.population}'


city = City('Odessa', 2000000)
print(city)
city = City('Bolgrad', 1000)
print(city)
