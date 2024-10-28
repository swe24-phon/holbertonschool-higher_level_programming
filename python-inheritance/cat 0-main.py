#!/usr/bin/python3
lookup = __import__('0-lookup').lookup

class MyClass1(object):
    pass

class MyClass2(object):
    my_attr1 = 3
    def my_meth(self):
        pass

print("list of attributes and methods for Myclass1 - pure object")
print(lookup(MyClass1))
print()
print("list of attributes and methods for Myclass2 - with my_attr1, my_meth")
print("note the last two item in the list are my_attr1 and my_meth")
print(lookup(MyClass2))
print()
print("list of attributes and methods for int - in built")
print(lookup(int))
