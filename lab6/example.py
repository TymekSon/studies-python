from abc import ABC, abstractmethod

class Parent:
    def __init__(self, privateField):
        self.__priv = privateField

    @property
    def getPriv(self):
        return self.__priv

    @privateField.setter
    def setPriv(self, value):
        self.__priv = value


class Derived(Parent):
    def __init__(self, privateField1, privateField2):
        super().__init__(self, privateField1)
        self.__priv2 = privateField2

class Figure(ABC):
    @abstractmethod
    def obw(delf):
        pass

class Square(Figure):
    def __init__(self, a):
        self.__a = a

    def obw(self):
        return 4*a