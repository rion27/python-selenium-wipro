#descriptor - control the access of the object attributes

#_get-()
#_set_()
#_delete()

class Desc:
    def __get__(self, instance, owner):
        print("Getting the value: ")
        return 2**3

class Test:
    x=Desc()

t=Test()
print(t.x)

#non - data descriptor ----- uses only the get descriptor
#data desc uses both get and set method
class mydesc:
    def __get__(self, instance, owner):
        return instance._value
    def __set__(self, instance, value):
        print("Setting the value")
        instance._value=value

class Test:
    x=mydesc()

t=Test()
t.x = 5      # calls __set__
print(t.x)   # calls __get__

# delete
class Name:
    def __get__(self, instance, owner):
        return instance._name
    def __set__(self, instance, value):
        instance._name=value
    def __delete__(self, instance):
        print("Deleting name")
        del instance._name
class Person:
    name=Name()
p=Person()
p.name="rion"
print(p.name)
del p.name