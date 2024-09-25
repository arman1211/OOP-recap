class Status:
    def __init__(self) -> None:
        self.__status = 'Single' #eta private var jeta baire teke directly access kora jabenaa
        self.name = 'Arman' #eta k abr access kora jabe
    def __married(self):
        print('eta private method')
    def get_status(self):
        return self.__status #private var er value deka jabe
    def get_married(self):
        return self.__married() #private method access korar jnno
    def set_status(self,status):
        self.__status = status #eta diye private variable set korte parbo
        return 'done'

class New(Status):
    def __init__(self) -> None:
        super().__init__()
    def get_status(self):
        return super().get_status()

myobj = Status()
newObj = New()
print(newObj.set_status('mm'))
# print(myobj.__status) eta kaj korbena
print(myobj.get_status()) 
print(myobj.get_married())
print(myobj.__dict__)
myobj.set_status('Engaged')
print(myobj.get_status())