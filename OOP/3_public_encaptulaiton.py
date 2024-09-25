
#public encapsulation refers to class members (attributes and methods) that are accessible from outside the class without any restrictions. I

class Car:
    def __init__(self, make, model, year):
        self.make = make  # Public attribute eigola baire teke access kora jai
        self.model = model 
        self.year = year  
    
    def start_engine(self):  # Public method
        print('grgrgrgrgrgrgrggr')


my_car = Car("lambo", "1212", 2022)


print(my_car.make)  
print(my_car.model)  
print(my_car.year)  

my_car.year = 2023
print(my_car.year)  


my_car.start_engine() 


















# class A:
#     __value = 5
#     def __init__(self) -> None:
#         pass
#     def display(self):
#         print(self.__value)

# obj = A()

# obj.__value = 10
# print(obj.__value)
# obj.display()

# print(obj.__dict__)