from abc import ABC, abstractmethod


class Vehicle(ABC):
    def __init__(self, number_of_wheels, engine_capacity):
        self.number_of_wheels= number_of_wheels
        self.engine_capacity = engine_capacity
    @abstractmethod
    def get_description(self):
        return f"the number_of_wheels: {self.number_of_wheels}, the engine_capacity: {self.engine_capacity}"

    def calculate_tax(self):
        return self.engine_capacity * 100


class Car(Vehicle):
    def __init__(self, number_of_wheels, engine_capacity, number_of_doors):
        Vehicle.__init__(self,number_of_wheels,engine_capacity)
        self.number_of_doors = number_of_doors
    def get_description(self):
        return Vehicle.get_description(self) + f" the number_of_doors: {self.number_of_doors}"
    # def calculate_tax(self):
    #     return Vehicle.calculate_tax(self)


class Motorcycle(Vehicle):
    def __init__(self, number_of_wheels, engine_capacity, lights):
        Vehicle.__init__(self,number_of_wheels,engine_capacity)
        self.lights = lights

    def get_description(self):
        return Vehicle.get_description(self) + f" the lights: {self.lights}"

myCar = Car(10,1000,4)
print(myCar.calculate_tax())
print(myCar)
