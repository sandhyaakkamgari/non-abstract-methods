from abc import ABC, abstractmethod

class Parent(ABC):
    def __init__(self, x):
        self.x = x

    @abstractmethod
    def abstract_method(self):
        pass

    def non_abstract_method(self):
        print("Calling non-abstract method from Parent, x:", self.x)

class Child(Parent):
    def __init__(self, x, y):
        super().__init__(x)
        self.y = y

    def abstract_method(self):
        print("Implementing abstract method in Child")

    def call_parent_non_abstract(self):
        self.non_abstract_method()

    def create_child_instance_and_call(self):
        child_instance = Child(10, 20)
        child_instance.non_abstract_method()

child = Child(5, 10)
child.call_parent_non_abstract() 
child.create_child_instance_and_call()