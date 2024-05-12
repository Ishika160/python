#simple 
class ParentClass:
    def parent_method(self):
        print("This is a method from the parent class.")

class ChildClass(ParentClass):
    def child_method(self):
        print("This is a method from the child class.")

child_obj = ChildClass()

child_obj.parent_method()
child_obj.child_method()

#multiple
class ParentClass1:
    def method1(self):
        print("Method from ParentClass1")

class ParentClass2:
    def method2(self):
        print("Method from ParentClass2")

class ChildClass(ParentClass1, ParentClass2):
    def child_method(self):
        print("Method from ChildClass")

# Create an instance of the child class
child_obj = ChildClass()

# Access methods from all parent classes and child class
child_obj.method1()
child_obj.method2()
child_obj.child_method()


