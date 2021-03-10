# 1.
class Laptop:
    """
    Make the class with composition.
    """
class Battery:
    """
    Make the class with composition.
    """

class Laptop:
    def __init__(self):
        display = Battery('Consumes more than 50 % of the battery charge.')
        keyboard = Battery('Consumes 15 % of the battery charge.')
        touchpad = Battery('Consumes 10 % of the battery charge.')
        self.components = [display, keyboard, touchpad]


class Battery:
    def __init__(self, charge):
        self.charge = charge


laptop = Laptop()



# 2.
class Guitar:
    """
    Make the class with aggregation
    """
class GuitarString:
    """
    Make the class with aggregation
    """


class Guitar:
    def __init__(self, guitar_string):
        self.guitar_string = guitar_string


class GuitarString:
    def __init__(self):
        pass


guitar_string = GuitarString()
guitar = Guitar(guitar_string)


# 3
class Calc:
    """
    Make class with one method "add_nums" with 3 parameters, which returns sum of these parameters.
    Note: this method should not take instance as first parameter.
    """


class Calc:

    @staticmethod
    def add_num(a, b, c):
        return a + b + c


print(Calc.add_num(3, 8, 15))

# 4*.
# class Pasta:
#     """
#     Make class which takes 1 parameter on init - list of ingredients and defines instance attribute ingredients.
#     It should have 2 methods:
#     carbonara (['forcemeat', 'tomatoes']) and bolognaise (['bacon', 'parmesan', 'eggs'])
#     which should create Pasta instances with predefined list of ingredients.
#     Example:
#         pasta_1 = Pasta(["tomato", "cucumber"])
#         pasta_1.ingredients will equal to ["tomato", "cucumber"]
#         pasta_2 = Pasta.bolognaise()
#         pasta_2.ingredients will equal to ['bacon', 'parmesan', 'eggs']
#     """

class Pasta:

    def __init__(self, list_of_ingredients):
        self.list_of_ingredients = list_of_ingredients

    @classmethod
    def carbonara(cls):
        return Pasta(['forcemeat', 'tomatoes'])

    @classmethod
    def bolognaize(cls):
        return Pasta(['bacon', 'parmesan', 'eggs'])


pasta_1 = Pasta(['tomato', 'cucumber'])
pasta_2 = Pasta.bolognaize()

print(pasta_1.list_of_ingredients)
print(pasta_2.list_of_ingredients)




# 5*.
class Concert:
    """
    Make class, which has max_visitors_num attribute and its inst ances will have visitors_count attribute.
    In case of setting visitors_count - max_visitors_num should be checked,
    if visitors_count value is bigger than max_visitors_num - visitors_count should be assigned with max_visitors_num.
    Example:
Concert.max_visitor_num = 50
concert = Concert()
concert.visitors_count = 1000
print(concert.visitors_count)  # 50
    """

class Concert:

    max_visitor_num = 0

    def __init__(self, visitors_count=0):
        self.visitors_count = visitors_count

    @property
    def visitors_count(self):
        return self.visitors_count

    @visitors_count.setter
    def visitors_count(self, visitors_count):
        if self.visitors_count > self.max_visitor_num:
            self._visitors_count = self.max_visitor_num
        else:
            self._visitors_count = self.visitors_count


Concert.max_visitor_num = 50
concert = Concert()
concert.visitors_count = 1000
print(concert.visitors_count)



# 6.
class AddressBookDataClass:
    """
    Create dataclass with 7 fields - key (int), name (str), phone_number (str),
    address (str), email (str), birthday (str), age (int)
    """

import dataclasses

@dataclasses.dataclass


class AddressBookDataClass:
    key: int
    name: str
    phone_number: str
    address: str
    email: str
    birthday: str
    age: int


address_book = AddressBookDataClass(10, 'Jane', '123456', 'Fifth Avenue', 'cloud.gmail.com',
                                 '14 may 2004', 20)

print(address_book)
print(address_book.address)

# 7. Create the same class (6) but using NamedTuple

import collections

AddressBookDataClass = collections.namedtuple('AddressBook', ['key', 'name', 'phone_number',
                                            'address', 'email', 'birthday', 'age'])

address_book = AddressBookDataClass(10, 'Jane', '123456', 'Fifth Avenue',
                                            'cloud.gmail.com', '14 may 2004', 20)

print(address_book[5])
print(address_book.name)

# 8.
class AddressBook:
    """
    Create regular class taking 7 params on init - key, name, phone_number, address, email, birthday, age
    Make its str() representation the same as for AddressBookDataClass defined above.
    """


class AddressBook:

    def __init__(self, key, name, phone_number, address, email, birthday, age):
        self.key = key
        self.name = name
        self.phone_number = phone_number
        self.address = address
        self.email = email
        self.birthday = birthday
        self.age = age

    def __str__(self):
        return f'The pupil {self.name} lives an street {self.address}, she was born {self.birthday}'


addressbook1 = AddressBook(10, 'Jane', '123456', 'Fifth Avenue',
                                'cloud.gmail.com', '14 may 2004', 20)
print(addressbook1)


# 9.
class Person:
    """
    Change the value of the age property of the person object
    """
    name = "John"
    age = 36
    country = "USA"


person = Person()

setattr(person, 'age', 25)
print(person.age)



# #10.
class Student:

    """
    Add an 'email' attribute of the object student and set its value
    Assign the new attribute to 'student_email' variable and print it by using getattr
    """
    id = 0
    name = ""

    def __init__(self, id, name):
        self.id = id
        self.name = name


student = Student(5, "Jane")
student.email = "cloud.gmail.com"
setattr(student, student.email, "cloud.gmail.com")

print(getattr(student, student.email))

#
#11*

class Celsius:
    """
    By using @property convert the celsius to fahrenheit
    Hint: (temperature * 1.8) + 32)
    """
    def __init__(self, temperature=0):
        self._temperature = temperature

    @property
    def temperature(self):
        return (self._temperature * 1.8) + 32


# create an object:
fahrenheit = Celsius(233)

print(fahrenheit.temperature)
