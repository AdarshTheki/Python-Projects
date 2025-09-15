# OOP (Object-Oriented Programming)

# 22.Create a class Car with attributes like brand, model, and methods to display details.
def class_create():
    class Car:
        def __init__(self, brand, model):
            self.brand = brand
            self.model = model
        def display_info(self):
            print(f"Car Brand: {self.brand}, Model: {self.model}")
    # Example Usage
    my_car = Car("Toyota", "Corolla")
    my_car.display_info()

# 23. Implement inheritance: Create a Vehicle class and inherit Car from it.
def class_inheritance():
    class Vehicle:
        def __init__(self, brand):
            self.brand = brand
        def show_brand(self):
            print(f"Vehicle brand: {self.brand}")
    class Car(Vehicle):
        def __init__(self, brand, model):
            super().__init__(brand)
            self.model = model
        def show_car_info(self):
            print(f"Car Model: {self.model}")
    my_car = Car("Honda", "Civic")
    my_car.show_brand()
    my_car.show_car_info()

# 24. Use encapsulation to make class attributes private.
def class_encapsulation():
    class Person:
        def __init__(self, name, age):
            self.__name = name  # Private attribute
            self.__age = age  # Private attribute
        def get_info(self):
            return f"Name: {self.__name}, Age: {self.__age}"
    person = Person("Alice", 30)
    print(person.get_info())
    # Attempting to access private attribute directly (will raise error)
    # print(person.__name)  # AttributeError

