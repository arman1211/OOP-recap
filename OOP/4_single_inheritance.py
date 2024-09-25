# kono ekta parent class teke inherit korle tokon etake amra single inheritance boli 

class Boss:
    def __init__(self,name) -> None:
        self.name = name
    def names(self):
        return (self.name)

class Ghost(Boss):
    def __init__(self, name,power) -> None:
        super().__init__(name)
        self.power = power
    # overriding the base class method
    def names(self):
        return (f'{self.name} has power {self.power}')

newghost = Ghost('halum',90)
print(newghost.names())


















# class A:
#     def __init__(self,name) -> None:
#         self.name = name

#     def display(self):
#         print(self.name)


# class B(A):
#     def __init__(self, name) -> None:
#         super().__init__(name)

# obj = B("Sayed")
# obj.display()