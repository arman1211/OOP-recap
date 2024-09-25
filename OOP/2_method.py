class Genz:
    def __init__(self) -> None:
        print('hello')
    def display(self):
        print('this is genz')
        return 'ok'

def display():
    print('this is another display')
    return 'fine'

a = Genz()
a.display = display()
print(a.display)










# class A:
#     pass

# def display():
#     print("I am Methods")

# obj = A()
# obj.value = display

# print(obj.value)
# print(obj)
