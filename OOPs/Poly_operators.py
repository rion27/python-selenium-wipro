# operator polymorphism means the same operator behaves differently for different data types or the object
# + add numbers,join strings,merges list -> operator overloading in python
# _add() ,sub(),mul(),eq() , __lt() , __gt_()


class number:
    def __init__(self, value):
        self.value = value

    def __add__(self, other):
        return self.value + other.value


n1 = number(10)
n2 = number(20)
print(n1 + n2)


# now + will work for the custom objects

###
class number:
    def __init__(self, value):
        self.value = value

    def __sub__(self, other):
        return self.value - other.value

    def __mul__(self, other):
        return self.value * other.value

    def __eq__(self, other):
        return self.value == other.value

    def __lt__(self, other):
        return self.value < other.value

    def __gt__(self, other):
        return self.value > other.value


n1 = number(10)
n2 = number(20)
print(n1 == n2)
print(n1 < n2)
print(n1 > n2)
print(n1 * n2)
print(n2 - n1)