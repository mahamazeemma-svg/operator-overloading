class A:

    def __init__(self,a):
        self.a = a

    def __lt__(self,other):
        if(self.a < other.a):
            print("obj1 is less than obj2")
        else:
            print("obj2 is less than obj1")

    def __eq__(self,other):
        if self.a == other.a:
            print("obj1 is the same as obj2")

        else:
            print("both are not same")

obj1 = A(1)
obj2 = A(2)
print("passed values are",obj1.a,obj2.a)
obj1 < obj2

obj3 = A(3)
obj4 = A(4)
print("passed values are",obj3.a,obj4.a)
obj3 == obj4