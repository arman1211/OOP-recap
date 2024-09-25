class Arman:
    age=20
    def __init__(self,newage) -> None:
        print('hello there.')
        self.age=newage
    def show(self):
        print('something is wrong')
        self.age+=5
    def __del__(self):
        print('I am the last part, destructor. ')
    def __str__(self):
        return  f'what are you doing {self.age}'

myGhost = Arman(12)
myGhost.show()
print(myGhost.age)
print(myGhost)
        











# class A:
#     value = 5 #class variable
#     def __init__(self) -> None:
#         print("I am Constructor")
    
#     def display(self):
#         print("I am method")

#     def __del__(self):
#         print("I am destructor")

#     def __str__(self) -> str:
#         return "I am ClasS A"




# obj = A()
# obj1 = A()
# obj.display()
# obj.value = 5

# print(obj.__dict__)





# print(obj.value)
# print(A.value)











