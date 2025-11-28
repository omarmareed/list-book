# class stack():
#     def __init__(self):
#         self.items = []
# def push(self,item):
#         self.items.append(item)
# from itertools import product
# from random import random
# from inspect import stack
# from ast import Index
# from enum import member
#
#
# def pop(self):
#         if not self.isEp():
#             return self.items.pop()
#
#     def isEp(self):
#         return len(self.items) == 0
#
#     def peek(self):
#         return self.items[-1]
#
#     stack = stack()
#     stack.push(7)
#     stack.push("y")
#import math
#from inspect import stack
#############################################################################################################################################################
#
# def countries_filter(dict):
#     happy_country=list()
#     sad_country=list()
#     for i in dict:
#        if i["GDP Growth"]>3 and dict["Inflation Rate"]<2:
#            happy_country.append()
#        else:
#            sad_country.append()
#     return happy_country
#
#
# countries_filter()
#
###############################################################################################################################################################
#
# tuple_numbers = (10, 20, 30, 40, 50)
# print(tuple_numbers[3])
#
# mixed_tuple = ("Hello", 42, 3.14)
# print(len(mixed_tuple))
# for item in mixed_tuple:
#     print(len(str(item)))
#
###############################################################################################################################################################
# #Airplane and Airport System : Part 2 cont
# import random
#
#
# class Airplane():
#     def __init__(self,name,manufacturer,seating_capacity,max_speed,fuel_capacity):
#         self.name = name
#         self.manufacturer = manufacturer
#         self.seating_capacity = seating_capacity
#         self.max_speed = max_speed
#         self.fuel_capacity= fuel_capacity
#         self.current_fuel_level = 0
#         self.current_altitude =0
#         self.status = "grounded"
#
#     def change_status(self,new_status):
#         self.status= new_status
#
#     def refuel(self,amount):
#         if self.current_fuel_level + amount > self.fuel_capacity:
#             self.current_fuel_level = self.fuel_capacity
#             print(f"{self.name} is now fully refueled")
#         else:
#             self.current_fuel_level += amount
#             print(f"{self.name} is  refueled with {amount} of liters")
#
#     def take_off(self):
#         if self.current_fuel_level == 0:
#             print("Cannot take off, please refuel the airplane ")
#         else:
#             self.status ="in flight"
#             self.current_altitude = 10000
#             print(f"{self.name}, the plane is ready to take off and now in flight")
#     def land(self):
#         if self.status == "in flight":
#             self.status ='grounded'
#             self.current_altitude =0
#             print("The airplane is landed safely")
#
#         else:
#             print("The airplane is already on the ground")
#
#     def display_status(self):
#         print(f"""
#                 Airplane ; {self.name}
#                 Manufacturer ; {self.manufacturer}
#                 Status ; {self.status}
#                 Current Altitude ; {self.current_altitude} ft
#                 Max Speed ; {self.max_speed} km/h
#                 Fuel level ; {self.current_fuel_level} liters
#                """)
# class Flight():
#     def __init__(self,flight_id,departure_airport,arrival_airport,distance,required_seating_capacity):
#         self.flight_id = flight_id
#         self.departure_airport = departure_airport
#         self.arrival_airport = arrival_airport
#         self.distance = distance
#         self.required_seating_capacity = required_seating_capacity
#         self.status = 'scheduled'
#         self.assigned_airplane = None
#
#
#     def assign_airplane(self,airplanes):
#         for airplane  in airplanes :
#             if airplane.seating_capacity >= self.required_seating_capacity and airplane.current_fuel_level*10 >= self.distance and airplane.status =='grounded' :
#                 self.assigned_airplane = airplane
#                 airplane.change_status('occupied')
#                 print(f" flight {self.flight_id} assigned to airplane {airplane.name}")
#                 self.update_status('in progress')
#                 return True
#
#         return False
#
#     def update_status(self,new_status):
#         self.status = new_status
#
#
#     def display_status(self):
#         print(f"""
#                 Flight ; {self.flight_id}
#                 Departure Airport ; {self.departure_airport}
#                 Arrival Airport ; {self.arrival_airport}
#                 Distance ; {self.distance} ft
#                """)
#
#
# class AirportSystem:
#
#     def __init__(self):
#         self.available_airplanes  = []
#         self.flights  = []
#
#     def add_airplane(self,airplane):
#         airplane.display_status()
#         self.available_airplanes.append(airplane)
#
#     def add_flight(self,flight):
#         self.flights.append(flight)
#
#     def find_and_assign_airplane(self, flight: Flight):
#
#         if flight.assign_airplane(self.available_airplanes):
#             print(f"Airplane Successfully assigned to flight {flight.flight_id}")
#         else:
#             print(f"Faild to assigned an airplane to flight {flight.flight_id}")
#
#
#     def update_flight_status(self,flight_id,new_status):
#         for flight in self.flights:
#             if flight.flight_id == flight_id:
#                 flight.update_status(new_status)
#                 print(f"Flight {flight.flight_id} status updated to {new_status}")
#                 return
#         print(f"Flight with {flight_id}was not found")
#
#
# def create_random_airplane():
#     names = ['Boeing 737','Airbus A320','Concorde','Cessna 172','Gulfstream G700']
#     manufacturers = ['Boeing','Airbus','Lockheed Martin','Cessna','Gulfstream']
#     name = random.choice(names)
#     manufacturer =   'Lockheed Martin' if name =='Concorde' else name.split(' ')[0]
#     seating_capacity = random.randint(4,600)
#     max_speed = random.randint(300,1000)
#     fuel_capacity = random.randint(1000,250000)
#
#     return Airplane(name=name,manufacturer=manufacturer,seating_capacity=seating_capacity,
#                     max_speed=max_speed,fuel_capacity=fuel_capacity)
#
#
#
# random_airplanes = [create_random_airplane() for i in range(5)]
# for i ,airplane in enumerate(random_airplanes):
#     airplane.display_status()
#
#
#
from audioop import reverse


#########################################################################################################################
#
# # Initialize Airport System
# airport_system = AirportSystem()
#
# # Add Airplanes
# airplane1= Airplane("Boeing 737", "Boeing", 200, 850, 20000)
# airplane1.refuel(1000000)
# airplane2= Airplane("Airbus A320", "Airbus", 180, 830, 19000)
# airplane2.refuel(1000000)
# airplane3 = Airplane("Cessna 172", "Cessna", 4, 300, 200)
# airplane3.refuel(1000000)
#
#
# airport_system.add_airplane(airplane1)
# airport_system.add_airplane(airplane2)
# airport_system.add_airplane(airplane3)
#
# # Add Flights
# flight1 = Flight("FL001", "JFK", "LAX", 4000, 150)
# flight2 = Flight("FL002", "LHR", "DXB", 5500, 200)
# flight3 = Flight("FL003", "SFO", "SEA", 1300, 4)
#
#
# airport_system.add_flight(flight1)
# airport_system.add_flight(flight2)
# airport_system.add_flight(flight3)
#
# # Assign Airplanes to Flights
# airport_system.find_and_assign_airplane(flight1)
# airport_system.find_and_assign_airplane(flight2)
# airport_system.find_and_assign_airplane(flight3)
#
#  #Print Status of Flights and Airplanes
# print("\nAll Flights:")
# for flight in airport_system.flights:
#     flight.display_status()
#
# print("\nAll Airplanes:")
# for airplane in airport_system.available_airplanes:
#     airplane.display_status()

##########################################################################################################################
# # תרגיל מספר 9
# def Prime_check(n,dev=2):
#     if n < 2:
#         return False
#     if dev * dev > n:
#         return True
#     if n % dev == 0:
#         return False
#     return Prime_check(n,dev + 1)
#
# print(Prime_check(17))
# print(Prime_check(16))
#
# def gcd(a,b):
#     if b == 0:
#         return a
#     return gcd(b,a%b)
# gcd(60,42)
#
#
# def Tr(n):
#     if n == 0:
#         return
#     print("*"*n)
#     Tr(n-1)
#     Tr(5)
#
#     def decTobin(n):
#         if n ==0:
#             return '0'
#         return decTobin(n // 2)+ str(n % 2)
#     print(decTobin(5))
#
#     arr = [1,5,9,13,17]
#
#     def sumQ(arr):
#         if len(arr)== 0:
#             return 1
#         return sumQ(arr[1:]) * arr[0]
#
#     def Find_min(arr):
#         if len(arr) == 1:
#             return arr[0]
#         reastNum = Find_min(arr[1:])
#         if arr[0] < reastNum:
#             return arr[0]
#         else:
#             return reastNum
#
#         def bSort(arr):
#             n = len(arr)
#         if n == 1:
#             return arr
#         for i in range(n - 1):
#             if arr[i] > arr[i + 1]:
#                     arr[i], arr[i + 1] = arr[i + 1], arr[i]
#                     return bSort(arr[:-1]), [arr[-1]]
#
#         print(bSort([23, 5, 13, 70, 2]))
#
#######################################################################################################################
# class Product:
#     def __init__(self,name,category,price):
#         self.name = name
#         self.category = category
#         self.price = price
#
#     def info(self):
#         print(f"the name is {self.name},the category is {self.category},the price is {self.price}")
#
# Products_list = [Product('pro1','medicine','84'),
#                   Product('pro2','plants' ,'180'),
#                   Product('pro3','stuff','110'),
#                   Product('pro4','tools','62'),
#                   Product('pro5','cars','5500')]
#
# class ShoppingCart:
#     def __init__(self):
#         self.items = dict()
#     def add_product(self,name,quantity):
#         if name in self.items:
#             self.items[name] += quantity
#         else:
#             self.items[name] = quantity
#
#     def display_cart(self):
#         for key,value in self.items.items():
#             for j in self.templist:
#              if key == j.name:
#                 j.info()
#                 print("the quantity is :",value)
#                 print("for this pro is :",j.price *value)
#
#     def checkout(self):
#         if self.items =={}:
#             print("is empty")
#         else:
#             sumPrice = 0
#             for key , value in self.items.items():
#                 for j in self.templist:
#                     if key == j.name:
#                         sumPrice +=j.price * value
#
#                 print("total price is:",sumPrice)
#
#########################################################################################################################
#
# class binarytree:
#     def __init__(self,value):
#         self.value = value
#         self.R=None
#         self.L=None
#     def depth(self,depth,maxvalue):
#         if depth == 0:
#             return None
#
#         node=binarytree(random.randint(1,maxvalue))
#         if random.choice([True,False]):
#
#           node.L=depth(depth-1,maxvalue)
#         else:
#             node.L==None
#
#         return node
#
# def is_bst(node,min_value=float('inf'),max_value = float('inf')):
#     if node is None :
#         return True
#     if not (min_value < node.value and node.value < max_value):
#         return False
#     return is_bst(node.left,min_value,node.value) and is_bst(node.right,node.value,max_value)
#
########################################################################################################################
#
# #מחסנית
#
# class Stack :
#     def __init__(self):
#         self.item = []
#     def is_empty(self):
#         return len(self.item) == 0
#     def push(self, item):
#         self.item.append(item)
#     def pop(self):
#         if not self.is_empty():
#             return self.item.pop()
#     def peek(self):
#         if not self.is_empty():
#             return self.item[-1]
#     def size(self):
#         return len(self.item)
#
# def reverse_stack(stack1):
#     print("bf:" , stack1.show())
#     stack2 = stack()
#     while not  stack1.is_empty():
#         stack2.push(stack1.pop())
#     print("af stack 1:" , stack2.show())
#     return stack2
#
########################################################################################################################
#
# from abc import ABC, abstractmethod
#
#
# class Vehicle(ABC):
#     def __init__(self, number_of_wheels, engine_capacity):
#         self.number_of_wheels= number_of_wheels
#         self.engine_capacity = engine_capacity
#     @abstractmethod
#     def get_description(self):
#         return f"the number_of_wheels: {self.number_of_wheels}, the engine_capacity: {self.engine_capacity}"
#
#     def calculate_tax(self):
#          return self.engine_capacity * 100
#
#
# class Car(Vehicle):
#     def __init__(self, number_of_wheels, engine_capacity, number_of_doors):
#         Vehicle.__init__(self,number_of_wheels,engine_capacity)
#         self.number_of_doors = number_of_doors
#     def get_description(self):
#         return Vehicle.get_description(self) + f" the number_of_doors: {self.number_of_doors}"
#      def calculate_tax(self):
#          return Vehicle.calculate_tax(self)
#
#
# class Motorcycle(Vehicle):
#     def __init__(self, number_of_wheels, engine_capacity, lights):
#         Vehicle.__init__(self,number_of_wheels,engine_capacity)
#         self.lights = lights
#
#     def get_description(self):
#         return Vehicle.get_description(self) + f" the lights: {self.lights}"
#
# myCar = Car(10,1000,4)
# print(myCar.calculate_tax())
# print(myCar)
#
# class shape(ABC):
#     def __init__(self):...
#     @abstractmethod
#     def calculate_area(self):
#     @abstractmethod
#
########################################################################################################################

# class Node:
#     def __init__(self, value):
#         self.value = value
#         self.left = None
#         self.right = None
#
# def pre_order(node):
#     if node:
#         print(node.value, end=" ")
#         pre_order(node.left)
#         pre_order(node.right)
#
# def in_order(node):
#     if node:
#         in_order(node.left)
#         print(node.value, end=" ")
#         in_order(node.right)
#
# def post_order(node):
#     if node:
#         post_order(node.left)
#         post_order(node.right)
#         print(node.value, end=" ")
#
# root1 = Node("A")
# root1.left = Node("B")
# root1.right = Node("C")
# root1.left.left = Node("D")
# root1.left.right = Node("E")
#
# print("Tree 1 :")
# print("Pre-order:")
# pre_order(root1)
# print("\nIn-order:")
# in_order(root1)
# print("\nPost-order:")
# post_order(root1)
# print("\n")
#
# class TreeNode:
#     def __init__(self, value):
#         self.value = value
#         self.left = None
#         self.right = None
#
# def pre_order_result(node, result):
#     if node:
#         result.append(node.value)
#         pre_order_result(node.left, result)
#         pre_order_result(node.right, result)
#
# def in_order_result(node, result):
#     if node:
#         in_order_result(node.left, result)
#         result.append(node.value)
#         in_order_result(node.right, result)
#
# def post_order_result(node, result):
#     if node:
#         post_order_result(node.left, result)
#         post_order_result(node.right, result)
#         result.append(node.value)
#
# root2 = TreeNode(1)
# root2.right = TreeNode(2)
# root2.right.right = TreeNode(3)
# root2.right.right.right = TreeNode(4)
# root2.right.right.right.right = TreeNode(5)
#
# pre_order_result_list = []
# in_order_result_list = []
# post_order_result_list = []
#
# pre_order_result(root2, pre_order_result_list)
# in_order_result(root2, in_order_result_list)
# post_order_result(root2, post_order_result_list)
#
# print("Tree 2 :")
# print("Pre-order:", pre_order_result_list)
# print("In-order:", in_order_result_list)
# print("Post-order:", post_order_result_list)
# print("\n")
#
#
# class Node:
#     def __init__(self, value):
#         self.value = value
#         self.left = None
#         self.right = None
#
# root = Node("M")
# root.left = Node("N")
# root.right = Node("O")
# root.left.left = Node("P")
# root.left.right = Node("Q")
# root.right.left = Node("R")
# root.right.right = Node("S")
#
# def pre_order(node):
#     if node:
#         print(node.value, end=" ")
#         pre_order(node.left)
#         pre_order(node.right)
#
# def in_order(node):
#     if node:
#         in_order(node.left)
#         print(node.value, end=" ")
#         in_order(node.right)
#
# def post_order(node):
#     if node:
#         post_order(node.left)
#         post_order(node.right)
#         print(node.value, end=" ")
#
# print("Tree 3:")
# print("Pre-order Traversal:")
# pre_order(root)
# print("\nIn-order Traversal:")
# in_order(root)
# print("\nPost-order Traversal:")
# post_order(root)
# print("\n")
#
# class Node:
#     def __init__(self, value):
#         self.value = value
#         self.left = None
#         self.right = None
#
# def pre_order(node):
#     if node:
#         print(node.value, end=" ")
#         pre_order(node.left)
#         pre_order(node.right)
#
# def in_order(node):
#     if node:
#         in_order(node.left)
#         print(node.value, end=" ")
#         in_order(node.right)
#
# def post_order(node):
#     if node:
#         post_order(node.left)
#         post_order(node.right)
#         print(node.value, end=" ")
#
# root = Node("X")
# root.left = Node("Y")
# root.right = Node("Z")
# root.left.left = Node("A")
# root.left.right = Node("B")
#
# print("Tree 4:")
# print("Pre-order Traversal:")
# pre_order(root)
# print("\nIn-order Traversal:")
# in_order(root)
# print("\nPost-order Traversal:")
# post_order(root)
# print("\n")
#
# class Node:
#     def __init__(self, value):  # Corrected constructor
#         self.value = value
#         self.left = None
#         self.right = None
#
# def pre_order(node):
#     if node:
#         print(node.value, end=" ")
#         pre_order(node.left)
#         pre_order(node.right)
#
# def in_order(node):
#     if node:
#         in_order(node.left)
#         print(node.value, end=" ")
#         in_order(node.right)
#
# def post_order(node):
#     if node:
#         post_order(node.left)
#         post_order(node.right)
#         print(node.value, end=" ")
#
#
# root = Node(10)
# root.left = Node(20)
# root.right = Node(30)
# root.left.left = Node(40)
# root.left.right = Node(50)
# root.right.left = Node(60)
# root.right.right = Node(70)
#
# print("Tree 5:")
# print("Pre-order Traversal:")
# pre_order(root)
# print("\nIn-order Traversal:")
# in_order(root)
# print("\nPost-order Traversal:")
# post_order(root)
#
########################################################################################################################
# class car:
#     def __init__(self,brand,model):
#         self.brand = brand
#         self.model = model
#
#     def display_info(self):
#         print(f"Brand:{self}, Model:{self}")
#
# car =car("Toyota","Corolla")
# car.display_info()
# class ElectricCar(car):
#     def __init__(self,brand, model,battery_size):
#         super().__init__(brand,model)
#         self.battery_size = battery_size
#
#     def display_info(self):
#         print(f"Bmember2.borrow_book(book2)member2.borrow_book(book2)member2.borrow_book(book2)member2.borrow_book(book2)member2.borrow_book(book2)member2.borrow_book(book2)member2.borrow_book(book2)member2.borrow_book(book2)member2.borrow_book(book2)member2.borrow_book(book2)member2.borrow_book(book2)member2.borrow_book(book2)member2.borrow_book(book2)member2.borrow_book(book2)member2.borrow_book(book2)member2.borrow_book(book2)member2.borrow_book(book2)member2.borrow_book(book2)member2.borrow_book(book2)member2.borrow_book(book2)member2.borrow_book(book2)member2.borrow_book(book2)rand:{self.brand}, Model:{self.model}, Battery size:{self.battery_size}")e_car = ElectricCar("Tesla", "Model S", 75)
#         e_car.display_info()
#
#
# class ShoppingCart:
#     def __init__(self):
#         self.items = []
#     def add_item(self, item):
#         self.items.append(item)
#
#     def remove_item(self, item):
#         if item in self.items:
#             self.items.remove(item)
#
#     def display_items(self):
#         print(f"Items in cart: {self.items}")
#
# cart = ShoppingCart()
# cart.add_item("Apple")
# cart.add_item("Banana")
# cart.display_items()
# cart.remove_item("Apple")
# cart.display_items()
#
# class InsufficientFundsError(Exception):
#     def __init__(self, message):
#         self.message = message
#
# class BankAccount:
#     def __init__(self,balance):
#         self.balance = balance
#
#     def withdraw(self, amount):
#         if amount > self.balance:
#             raise InsufficientFundsError("Not enough funds!")
#         self.balance -= amount
# account = BankAccount(100)
# try:
#     account.withdraw(150)
# except InsufficientFundsError as e:
#     print(e.message)
#
# class Animal:
#     def __init__(self, name, species):
#         self.name = name
#         self.species = species
#
#     def make_sound(self):
#         raise NotImplementedError("Each animal must implement make_sound.")
#
#     def info(self):
#         return f"{self.name} is a {self.species}"
#
# class Mammal(Animal):
#     def __init__(self, name, species, is_domesticated):
#         super().__init__(name, species)
#         self.is_domesticated = is_domesticated
#
#     def make_sound(self):
#         return "Growl" if not self.is_domesticated else "Bark"
#
#     def info(self):
#         domestic_status = "domesticated" if self.is_domesticated else "wild"
#         return f"{super().info()} it is a {domestic_status} mammal"
########################################################################################################################
# class Queue:
#     def __init__(self):
#         self.item = []
#
#     def enqueue(self, item):
#         self.item.append(item)
#
#     def dequeue(self):
#         if not self.is_empty():
#             return self.item.pop(0)
#         else:
#             raise IndexError("Dequeue from an empty queue")
#
#     def peek(self):
#         if not self.is_empty():
#             return self.item[-1]
#
#     def is_empty(self):
#         return len(self.item) == 0
#
########################################################################################################################

#שאלה 1 תרגול

# from abc import ABC, abstractmethod
# class Web(ABC):
#     def __init__(self,name, url,num_pages):
#         self.name = name
#         self.url = url
#         self.num_pages = num_pages
#
#     @abstractmethod
#     def get_monthly_traffic(self):
#         pass
#     @abstractmethod
#     def get_website_details(self):
#         pass
#
# class ShoppingWebsite(Web):
#     def __init__(self,name, url, num_pages , num_products):
#         Web.__init__(self ,name, url,num_pages)
#         self.num_products = num_products
#
#     def get_monthly_traffic(self):
#         return self.num_products * 500
#
#     def get_website_details(self):
#         return f"ShoppingWebsite is my dt{self.num_products},{self.num_products},{self.num_pages},{self.name}"
#
# class InformationWebsite(Web):
#     def __init__(self,name, url, num_pages , num_articles):
#         Web.__init__(self,name, url, num_pages )
#         self.num_articles = num_articles
#
#     def get_monthly_traffic(self):
#         return self.num_articles * 200
#
#     def get_website_details(self):
#         return f"InformationWebsite {self.num_articles},{self.num_pages},{self.name},{self.url}"
#
# class BlogWebsite(Web):
#     def __init__(self, name, url, num_pages, num_posts):
#         Web.__init__(self, name, url, num_pages)
#         self.num_posts = num_posts
#
#     def get_monthly_traffic(self):
#          return self.num_posts * 300
#
#     def get_website_details(self):
#         return f"BlogWebsite {self.num_posts},{self.num_pages},{self.name},{self.url}"

########################################################################################################################
#  #בן יאיר (exams)
# from abc import ABC, abstractmethod
#
# from unicodedata import numeric
#
#
# class Transportation(ABC):
#     def __init__(self, vehicle_id, capacity, average_speed):
#         self.vehicle_id = vehicle_id
#         self.capacity = capacity
#         self.average_speed = average_speed
#
#     @staticmethod
#     def  compare_capacity(vehicle1, vehicle2):
#         if vehicle1.capacity > vehicle2.capacity:
#             #return f"{vehicle1.__class__.__name__}(ID: {vehicle1.vehicle_id}) has a larger capacity "
#         elif vehicle1.capacity < vehicle2.capacity:
#             #return f"{vehicle2.__class__.__name__} (ID: {vehicle2.vehicle_id}) has a larger capacity."
#         return "Both vehicles have the same capacity."
#
# class Bus(Transportation):
#     def __init__(self, vehicle_id, capacity, average_speed,num_stations):
#         super.__init__(self.vehicle_id, capacity, average_speed)
#         self.num_stations = num_stations
#
#     def calculate_cost(self, distance):
#         return

########################################################################################################################
# class Book :
#     def __init__(self,title,author,isbn):
#         self.title = title
#         self.author = author
#         self.isbn = isbn
#     def get_details(self):
#         return f"Title:{self.title}, Author:{self.author}, ISBN:{self.isbn}"
#
# class Member:
#     def __init__(self,name,):
#         self.name = name
#         self.borrowed_book=[]
#     def borrow_book(self,book):
#         self.borrowed_book.append(book)
#     def return_book(self,book):
#         if book in self.borrowed_book :
#             self.borrowed_book.remove(book)
# class library:
#     def __init__(self):
#         self.books = []
#         self.members = []
#     def add_book(self,book):
#         self.books.append(book)
#     def remove_book(self,book):
#         if book in self.books:
#             self.books.remove(book)
#     def register_member(self,member):
#         self.members.append(member)
#
# book1 = Book('1984','George Orwell','1234567890')
# member1 = member('Alice')
# lib1 = library()
# lib1.register_member(member1)
# lib1.add_book(book1)
# member1.borrow_book(book1)
# member1.return_book(book1)
# for bk in member1.borrowed_books:
#     print(bk.get_details())
########################################################################################################################
#
# class stack:
#     def __init__(self):
#         self.items = []
#     def push(self, item):
#         self.items.append(item)
#     def is_empty(self):
#         return len(self.items) == 0
#     def pop(self):
#         if not self.is_empty():
#             return self.items.pop()
#     def peek(self):
#         if not self.is_empty():
#             return self.items[-1]
#     def size(self):
#         return len(self.items)
#
# stack1=stack()
#
# def has_increasing_subsequence(stack, k):
#     pass
#
#
#
# def remove_adjacent_duplicates(stack):
#     aux = stack()
#
#     aux.push(stack.pop())
#     while not stack.is_empty():
#         if stack.peek() ==aux.peek():
#             stack.pop()
#             aux.pop()
#         else:
#             aux.push(stack.pop())
#
#     return aux
#
# def max_frequency(stack):
#     dict_occ={}
#     while not stack.is_empty():
#
#         x=stack.pop()
#         if x in dict_occ.keys():
#             dict_occ[x]=  dict_occ[x]+1
#         else:
#             dict_occ[x]=1
#     maxvalue = 0
#     for item, value in dict_occ.items():
#         if value > maxvalue:
#             maxitem = item
#             maxvalue = value
#     return maxitem
########################################################################################################################
#
# class Economist():
#     def __init__(self,name, id, experience):
#         self.name = name
#         self.id = id
#         self.experience = experience
# class JuniorEconomist(Economist):
#     def __init__(self,name, id, experience,num_small_investors):
#         Economist.__init__(self,name, id, experience)
#         self.num_small_investors = num_small_investors
#     def calculate_bonus(self):
#         return self.num_small_investors * 100
#     def get_details(self):
#         return f"Economist:{self.name},{self.id},{self.experience},{self.num_small_investors}"
#
# class ProfessionalEconomist(Economist):
#     def __init__(self,name, id, experience,portfolio_value):
#         Economist.__init__(self,name, id, experience)
#         self.portfolio_value = portfolio_value
#     def calculate_bonus(self):
#         return self.portfolio_value * 0.02
#     def get_details(self):
#         return f"ProfessionalEconomist:{self.name},{self.id},{self.experience},{self.portfolio_value}"
#
# class SeniorEconomist(Economist):
#     def __init__(self,name, id, experience,num_economists_managed):
#         Economist.__init__(self,name, id, experience)
#         self.num_economists_managed = num_economists_managed
#     def calculate_bonus(self):
#         return self.num_economists_managed * 2000
#     def get_details(self):
#         return f"SeniorEconomist:{self.name},{self.id},{self.experience},{self.num_economists_managed}"
# economists = [
#     JuniorEconomist('Alice',101,2,1000),
#     ProfessionalEconomist('Bob',102,10,1),
#     SeniorEconomist('Carol',103,10,10000)
# ]
########################################################################################################################
# from abc import ABC, abstractmethod
# from itertools import product
#
#
# class Product(ABC):
#     def __init__(self, name, product_id, base_price):
#         self.name = name
#         self.product_id = product_id
#         self.base_price = base_price
#     @abstractmethod
#     def get_final_price(self):
#         pass
#     @abstractmethod
#     def get_details(self):
#         pass
#
# class ElectronicProduct(Product):
#     def __init__(self, name, product_id, base_price, warranty_years):
#         Product.__init__(self, name, product_id, base_price)
#         self.warranty_years = warranty_years
#     def get_final_price(self):
#         discount = 1-(self.warranty_years * 0.1)
#         return self.warranty_years * self.base_price
#     def get_details(self):
#         return f"ElectronicProduct:{self.name},{self.product_id},{self.base_price},{self.warranty_years}"
# class ClothingProduct(Product):
#     def __init__(self, name, product_id, base_price, clothing_type, size):
#         Product.__init__(self, name, product_id, base_price)
#         self.clothing_type = clothing_type
#         self.size = size
#     def get_final_price(self):
#         discount = (self.size * 0.9)
#         return self.size * self.base_price
#     def get_details(self):
#         return f"ClothingProduct:{self.name},{self.product_id},{self.base_price},{self.size},{self.clothing_type}"
# class FoodProduct(Product):
#      def __init__(self, name, product_id, base_price, expiration_date, discount_rate):
#          Product.__init__(self, name, product_id, base_price)
#          self.expiration_date = expiration_date
#          self.discount_rate = discount_rate
#      def get_final_price(self):
#          discount = 1-(self.discount_rate * 0.1)
#          return self.expiration_date * self.base_price
#      def get_details(self):
#          return f"FoodProduct:{self.name},{self.product_id},{self.base_price},{self.expiration_date},{self.discount_rate}"
#
# class Cart:
#     def __init__(self):
#         self.products = []
#     def add_product(self, product):
#         self.products.append(product)
#     def remove_product(self, product_id):
#         for product in self.products:
#             if product.product_id == product_id:
#                 self.products.remove(product)
#                 return
#     def get_total_price(self):
#         sum1=0
#         for product in self.products:
#             sum1 += product.get_final_price()
#             return sum1
#     def get_cart_summary(self):
#         summary = [product.get_details() for product in self.products]
#         summary.append(f"Total price: {self.get_total_price():.2f}")
#         return "\n".join(summary)
########################################################################################################################
# class Stack:
#     def __init__(self):
#         self.item = []
#     def push(self, item):
#         self.item.append(item)
#     def pop(self):
#         if not self.is_empty():
#             return self.item.pop()
#     def peek(self):
#         if not self.is_empty():
#             return self.item[-1]
#     def is_empty(self):
#         return len(self.item) == 0
########################################################################################################################
# class Customer:
#     def __init__(self,name,customer_id):
#         self.name = name
#         self.customer_id = customer_id
#         self.drink_history = {}
#     def purchase_drink(self,drink):
#         raise NotImplementedError("This method should be implemented by subclasses")
#
#     def get_customer_basic_info(self):
#         return f"Customer:{self.name},{self.customer_id}"
# class RegularCustomer(Customer):
#     def __init__(self,name,customer_id):
#         Customer.__init__(name,customer_id)
#     def purchase_drink(self,drink):
#         if drink.name in self.drink_history.keys():
#             self.drink_history[drink.name] += 1
#         else:
#             self.drink_history[drink.name] = 1
########################################################################################################################
# class Pet :
#     def __init__(self,name,animaltype):
#         self.name = name
#         self.animaltype = animaltype
#     def make_sound(self):
#        raise NotImplementedError("This method should be implemented by subclasses")
#
#     def daily_care(self):
#         raise NotImplementedError("This method should be implemented by subclasses")
#     def get_info(self):
#         return f"Pet:{self.name},{self.animaltype}"
#
# class Dog:
#     def __init__(self,name,breed):
#         super().__init__(self,name)
#         self.breed = breed
#     def make_sound(self):
#         return f"Woof"
#     def daily_care(self):
#         return f"Daily walk"
#     def food_type(self):
#         return f"Dry dog food"
# class Parrot:
#     def __init__(self):
########################################################################################################################
# from abc import ABC, abstractmethod
# import math
#
# class Shape(ABC):
#     @abstractmethod
#     def calculate_area(self):
#         pass
#
#     @abstractmethod
#     def calculate_perimeter(self):
#         pass
#
# class Rectangle(Shape):
#     def __init__(self, width, height):
#         self.width = width
#         self.height = height
#     def calculate_area(self):
#         return self.width * self.height
#     def calculate_perimeter(self):
#         return 2 * (self.width + self.height)
# class Circle(Shape):
#     def __init__(self, radius):
#         self.radius = radius
#     def calculate_area(self):
#         return math.pi * self.radius ** 2
#     def calculate_perimeter(self):
#         return 2 * math.pi * self.radius
########################################################################################################################
# class vehicle(ABC):
#     def __init__(self,number_of_wheels,engine_capacity):
#         self.number_of_wheels = number_of_wheels
#         self.engine_capacity = engine_capacity
# class Car(vehicle):
#     def __init__(self,number_of_wheels,engine_capacity,number_of_doors):
#         vehicle.__init__(self,number_of_wheels,engine_capacity)
#         self.number_of_doors = number_of_doors
#     def get_description(self):
#         return f"Car:{self.number_of_wheels},{self.engine_capacity},{self.number_of_doors}"
#     def calculate_tax(self):
#         return self.engine_capacity * 100
#
# class Motorcycle(vehicle):
#     def __init__(self,number_of_wheels,engine_capacity,lights):
#         vehicle.__init__(self,number_of_wheels,engine_capacity)
#         self.lights = lights
#
#     def get_description(self):
#         return f"Motorcycle:{self.number_of_wheels},{self.engine_capacity},{self.lights}"
#     def calculate_tax(self):
#         return self.engine_capacity * 100
#
# class Shape(ABC):
#     def __init__(self):
#         self.shape = []
# class Rectangle(Shape):
#     def __init__(self, width, height):
#         self.width = width
#         self.height = height
#     def calculate_area(self):
#         return self.width * self.height
#     def calculate_perimeter(self):
#         return (self.height+self.width)*2
# class Circle(Shape):
#     def __init__(self, radius):
#         self.radius = radius
#     def calculate_area(self):
#         return math.pi * self.radius ** 2
#     def calculate_perimeter(self):
#         return math.pi * self.radius * 2
#
# class Employee(ABC):
#     def __init__(self,name):
#         self.name = name
# class FullTimeEmployee(Employee):
#         def __init__(self, name, base_salary, bonus):
#             Employee.__init__(self, name)
#             self.base_salary = base_salary
#             self.bonus = bonus
#         def calculate_salary(self):
#             return self.base_salary + self.bonus
#         def get_details(self):
#             return f"FullTimeEmployee:{self.name},{self.base_salary},{self.bonus}"
# class PartTimeEmployee(Employee):
#         def __init__(self, name, hourly_rate, hours_worked):
#             self.name = name
#             self.hourly_rate = hourly_rate
#             self.hours_worked = hours_worked
#         def calculate_salary(self):
#             return self.hourly_rate * self.hours_worked
#         def get_details(self):
#             return f"PartTimeEmployee:{self.name},{self.hourly_rate},{self.hours_worked}"
# class Course:
#        def __init__(self, course_name):
#            self.course_name = course_name
#         def add_student(self, student_name):
#######################################################################################################################
# class Course:
#     def __init__(self, course_name):
#         self.course_name = course_name
#         self.students =[]
#     def add_student(self, student_name):
#         self.students.append(student_name)
#     def remove_student(self, student_name):
#         if student_name in self.students:
#             self.students.remove(student_name)
#     def list_students(self):
#         print(f"student_name in {self.course_name}: {self.students}")
#         for student in self.students:
#             print(student)
# class University:
#     def __init__(self):
#         self.courses_list = []
#     def add_course(self, course):
#         self.courses_list.append(course)
#     def find_course(self, course_name):
#         for course_name in self.courses_list:
#                 return course_name
#     def list_courses(self):
#         for course in self.courses_list:
#             print(course.course_name)
# class Table:
#     def __init__(self,table_number,capacity):
#         self.table_number = table_number
#         self.capacity = capacity
# class Reservation:
#     def __init__(self,customer_name, table, time):
#         self.customer_name = customer_name
#         self.table = table
#         self.time = time
# class ReservationSystem:
#     def __init__(self):
#         self.reservations = []
#     def add_reservation(self, reservation):
#         self.reservations.append(reservation)
#     def find_reservation(self, customer_name):
#         for reservation in self.reservations:
#             return reservation
#     def list_reservations(self):
#         for reservation in self.reservations:
#             print(reservation)
########################################################################################################################
# class Customer:
#     def __init__(self,name,customer_id):
#         self.name = name
#         self.customer_id = customer_id
#         self.drink_history = {}
#     def purchase_drink(self,drink):
#         raise NotImplementedError("This method should be implemented by subclasses")
#     def get_customer_basic_info(self):
#         return f"Customer:{self.name},{self.customer_id}"
# class RegularCustomer(Customer):
########################################################################################################################
# def reverse_stack(stack1):
#     stack2 = Stack()
#     while not stack1.is_empty():
#         stack2.push(stack1.pop())
#         return stack2
#     stack2=reverse_stack(s)
#     print(stack2.items)
########################################################################################################################
# def find_minimum(self):
#     S1 = stack()
#     min = float.int()
#     while not self.is_empty():
#         x = self.pop()
#         if x < min:
#             min = x
#             S1.push(x)
#             while not S1.is_empty():
#                 self.push(S1.pop())
#             return min
########################################################################################################################
# from abc import ABC , abstractmethod
#
# class Book(ABC):
#     def __init__(self,title,author):
#         self.title = title
#         self.autor = author
#     @abstractmethod
#     def get_price(self):
#         pass
#     @abstractmethod
#     def get_details(self):
#         pass
#
# class PrintedBook(Book):
#     def __init__(self,title,author,pages):
#         Book.__init__(self,title,author)
#         self.pages = pages
#     def get_price(self):
#         return f"{self.pages * 10}"
#     def get_details(self):
#         return f"Book:{self.title},{self.autor},{self.pages}"
#
# class EBook(Book):
#     def __init__(self,title,author,file_size):
#         Book.__init__(self,title,author)
#         self.file_size = file_size
#     def get_price(self):
#         return f"{self.file_size * 2}"
#     def get_details(self):
#         return f"EBook:{self.title},{self.autor},{self.file_size}"
#
# class Library:
#     def __init__(self):
#         self.book_list = []
#     def add_book(self,book):
#         self.book_list.append(book)
########################################################################################################################
# class Stack:
#     def __init__(self):
#         self.item = []
#     def push(self,item):
#         self.item.append(item)
#     def pop(self):
#         if not self.is_empty():
#             return self.item.pop()
#     def is_empty(self):
#         return len(self.item)== 0
#
# def find_minimum(self):
#     s1 = stack()
#     min = float.int()
#     while not self.is_empty():
#         x = self.pop()
#         if x < min:
#             min = x
#             s1.push(x)
#         while not s1.is_empty():
#             self.push(s1.pop())
#             return min
########################################################################################################################
# from abc import ABC, abstractmethod
# import math
#
# class Shape(ABC):
#     @abstractmethod
#     def calculate_area(self):
#         pass
#
#     @abstractmethod
#     def calculate_perimeter(self):
#         pass
#
# class Rectangle(Shape):
#     def __init__(self,width,height):
#         self.width = width
#         self.height = height
#     def calculate_area(self):
#         return self.height * self.width
#     def calculate_perimeter(self):
#         return (self.height + self.width) * 2
# class Circle(Shape):
#     def __init__(self,radius):
#         self.radius = radius
#     def calculate_area(self):
#         return math.pi * self.radius ** 2
#     def calculate_perimeter(self):
#         return math.pi * self.radius * 2
#
# class ShapeManager:
#     def __init__(self):
#         self.list = []
#     def add_list(self,list):
#         self.list.append(list)
########################################################################################################################
# class Queue:
#     def __init__(self):
#         self.item = []
#     def enqueue(self,item):
#         self.item.append(item)
#     def dequeue(self):
#         if not self.is_empty():
#             return self.item.pop()
#     def is_empty(self):
#         return len(self.item)== 0
#     def size(self):
#         sum = 0
#         for i in self.is_empty():
#             sum += 1
#             return sum
# ##########################################################################################################################
# from abc import ABC, abstractmethod
#
# class Animal(ABC):
#     @abstractmethod
#     def speak(self):
#         pass
#     @abstractmethod
#     def get_details(self):
#         pass
# class Lion(Animal):
#     def __init__(self,name,age):
#         self.name = name
#         self.age = age
#     def speak(self):
#         return f"Roar!"
#     def get_details(self):
#         return f"Lion:{self.name},{self.age}"
# class Elephant(Animal):
#     def __init__(self,weight):
#         Animal.__init__(self)
#         self.weight = weight
#     def speak(self):
#         return f"Trumpet!"
#     def get_details(self):
#         return f"Elephant:{self.weight}"
# class Monkey(Animal):
#     def __init__(self,favorite_food):
#         Animal.__init__(self)
#         self.favorite_food = favorite_food
#     def speak(self):
#         return f"Ooh Ooh Ah Ah!"
#     def get_details(self):
#         return f"Monkey:{self.favorite_food}"
#
# class Zoo:
#     def __init__(self):
#         self.Animal_list = []
#     def add_animal(self,animal):
#         self.Animal_list.append(animal)
#     def show_animal(self):
########################################################################################################################
class stack:
    def __init__(self):
        self.item = []
    def push(self,item):
        self.item.append(item)
    def pop(self):
        if not self.is_empty():
            return self.item.pop()
    def is_empty(self):
        return len(self.item)== 0
    def peek(self):
        if not self.is_empty():
            return self.item[-1]
    def size(self):
        sum = 0
        for i in self.is_empty():
            sum += 1
            return sum

    def reverse_stack(s1):
        s2 = stack()
        while not s1.is_empty():
            s2.push(s1.pop())
            return s2























