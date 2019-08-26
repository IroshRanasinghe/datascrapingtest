# x=1
# if x==1:
#     print("true")
# else:
#     print("false")
#

# 01
# while loop
# j = 10
# while j > 5:
#     print(j)
#     j = j - 1
# 02
# i = 1
# while i < 100:
#     if i % 2 == 0:
#         print(i)
#     else:
#         print("ODD")
#     i = i + 1

# 01
# for loop
# for x in range(1000):
#     print(x)
# 02
# for i in range(100):
#     if i % 2 == 0:
#         print(i)
#     else:
#         print("ODD")

# function
# def method(a):
#     print(a + 1)
#
# method(10)


# class MyClass:
#     x = 5
# print(MyClass)

# class MyClass:
#     x=5
# p1=MyClass()
# print (p1.x)


# OOPC
# class Person:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#
#
# person = Person("Jhon", 32)
# print(person.name)
# print(person.age)


# class Person:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#
#     def my_func(self):
#         print("hello my name is " + self.name)
#         print(self.age)
#
#
# p1 = Person("Iroshana", 24)
# p1.my_func()


# class Person:
#     def __init__(self_or_any_name, name, age):
#         self_or_any_name.name = name
#         self_or_any_name.age = age
#
#     def my_funk(self_or_any_name):
#         print("My name is " + self_or_any_name.name)
#         print(24)
#
# p1=Person("Chalana",26)
# p1.my_funk()

# class Person:
#     def __init__(self,name,age):
#         self.name=name
#         self.age=age
#
#     def my_funck(self):
#         print("My name is "+self.name)
#
# p1=Person("iroshana",24)
# p1.my_funck()
# del p1.age
# print (p1.age)

# del p1
# print(p1)

# 01
# class Person:  # parent class
#     def __init__(self, f_name, l_name):
#         self.f_name = f_name
#         self.l_name = l_name
#
#     def my_funk(self):
#         print(self.f_name, self.l_name)
#
#
# class Student(Person):  # child class
#     pass
#
#
# s1 = Student("dilshan", "Iroshana")
# s1.my_funk()

# 02
# class Person:  # parent class
#     def __init__(self, f_name, l_name):
#         self.f_name = f_name
#         self.l_name = l_name
#
#     def my_funk(self):
#         print(self.f_name, self.l_name)
#
#
# class Student(Person):  # child class
#     def __init__(self, f_name, l_name):
#         Person.__init__(self, f_name, l_name)
#
# s1=Student("dilshan","iroshana")
# s1.my_funk()

# 03
# class Person:  # parent class
#     def __init__(self, f_name, l_name):
#         self.f_name = f_name
#         self.l_name = l_name
#
#     def my_funk(self):
#         print(self.f_name, self.l_name)
#
#
# class Student(Person):  # child class
#     def __init__(self, f_name, l_name):
#         super(Student, self).__init__(f_name, l_name)
#         # properties
#         self.graduate_year = 2018
#
#
# s1 = Student("dilshan", "iroshana")
# s1.my_funk()
# print(s1.graduate_year)

# import mymodule
# mymodule.greeting("dilshan")

# obj=mymodule.person["age"]
# print(obj)

# import mymodule as module
# obj=module.person["name"]
# print(obj)

# import platform
# print(platform.system())
# print(platform.python_version())
# # print(platform.machine())
# print(platform.processor())
# print(platform.python_compiler())
# print(platform.release())
#
# print (dir(platform))


# from mymodule import person
#
# print(person["name"])


# JSON

# import json
#
# person = '{"name":"iroshana","age":24}'
#
# json_obj = json.loads(person)
#
# print(json_obj["age"])


# Convert from Python to JSON

# import json
#
# person = {
#     "name": "iroshana",
#     "age": 24
# }
# obj = json.dumps(person)
# print(obj)

# import json

# print(json.dumps({"name": "iroshana", "age": 24}))
# print(json.dumps(["iroshana", 24]))
# print(json.dumps(("apple","banana")))
# print(json.dumps("hello"))
# print(json.dumps(24))
# print(json.dumps(24.4))
# print(json.dumps(True))
# print(json.dumps(False))
# print(json.dumps(None))

# x = {
#   "name": "John",
#   "age": 30,
#   "married": True,
#   "divorced": False,
#   "children": ("Ann","Billy"),
#   "pets": None,
#   "cars": [
#     {"model": "BMW 230", "mpg": 27.5},
#     {"model": "Ford Edge", "mpg": 24.1}
#   ]
# }
#
# print(json.dumps(x))


# x = {
#     "name": "John",
#     "age": 30,
#     "married": True,
#     "divorced": False,
#     "children": ("Ann", "Billy"),
#     "pets": None,
#     "cars": [
#         {"model": "BMW 230", "mpg": 27.5},
#         {"model": "Ford Edge", "mpg": 24.1}
#     ]
# }
#
# print(json.dumps(x,indent=3))
# # print(json.dumps(x, indent=4, separators=(".", "=")))
# print(json.dumps(x, indent=4, sort_keys=True))


# Exception Handling
# try:
#   print(x)
# except:
#   print("An exception occurred")

# try:
#   print(x)
# except:
#   print("Something went wrong")
# finally:
#   print("The 'try except' is finished")


# try:
#     price = 40
#     txt = "The price is {} $"
#     print(txt.format(price))
# except NameError:
#     print("Variable x is not defined")

# try:
#     price=40
#     txt="the price is {:.2f} dollars"
#     print(txt.format(price))
# except NameError:
#     print("Variable x is not defined")

# try:
#     price = 40
#     qty = 5
#     item_no = 10
#
#     my_oder = "I want {} pieces of item number {} for {:.2f} dollars"
#     print(my_oder.format(qty, item_no, price))
# except NameError:
#     print("Variable x is not defined")

# try:
#     price = 40
#     qty = 5
#     item_no = 10
#
#     my_oder = "I want {0} pieces of item number {1} for {2:.2f} dollars"
#     print(my_oder.format(qty, item_no, price))
# except NameError:
#     print("Variable x is not defined")

# my_order="I have a {car_name}, it is a {model}"
# print(my_order.format(car_name="Ford",model="Mustang"))


# Python File Open

# "r" - Read - Default value. Opens a file for reading, error if the file does not exist
#
# "a" - Append - Opens a file for appending, creates the file if it does not exist
#
# "w" - Write - Opens a file for writing, creates the file if it does not exist
#
# "x" - Create - Creates the specified file, returns an error if the file exists


# Python File Write

# f = open("demo.csv", "a")
# f.write("Now the file has more content")
# f.close()
#
# f = open("demo.csv", "r")
# print(f.read())

# f = open("demo.csv","w")
# f.write("Woops! I have deleted the content!")
# f.close()
#
# f = open("demo.csv","r")
# print(f.read())

f = open("demo.txt", "w")
f.write("Hello! Welcome to demofile.txt\nThis file is for testing purposes.\nGood Luck!")
f.close()

# f = open("demo.csv","r")
# for x in f:
#     print(x)

# f = open("demo.csv","r")
# print(f.readline())
# print(f.readline())
# f.close()