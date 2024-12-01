import datetime

class Person:
    __liczba_osob = 0

    def __init__(self, pesel, imie, nazwisko, waga = 0.0, wzrost = 0.0):
        self.__pesel = pesel
        self.__imie = imie
        self.__nazwisko = nazwisko
        if(int(pesel[2:4]) > 20):
            self.__rok_urodzenia = 2000 + int(pesel[0:2])
        else:
            self.__rok_urodzenia = 1900 + int(pesel[0:2])   
        self.__wzrost = wzrost
        self.__waga = waga
        Person.__liczba_osob += 1

    def __del__(self):
        Person.__liczba_osob -= 1

    @staticmethod
    def getInstances():
        return Person.__liczba_osob

    # zadanie 4
    def __str__(self):
        return self.__pesel + ', ' + self.__imie + ' ' + self.__nazwisko 

    def __repr__(self):
        return f'Person("{self.__pesel}","{self.__imie}","{self.__nazwisko}")'

    def __hash__(self):
        return int(self.__pesel) 

    # zadanie 5
    def getWiek(self):
        now = datetime.datetime.now()
        return now.year - self.__rok_urodzenia

    
    def getWaga(self):
        return self.__waga

    def getWzrost(self):
        return self.__wzrost

    @property
    def waga(self):
        return self.__waga

    @waga.setter
    def setWaga(self, waga):
        if(waga < 0):
            self.__waga = 0
        else:
            self.__waga = waga

    @property
    def wzrost(self):
        return self.__wzrost

    @wzrost.setter
    def setWzrost(self, wzrost):
        if(wzrost < 0):
            self.__wzrost = 0
        else:
            self.__wzrost = wzrost
        
    @classmethod
    def createPerson(cls, pesel, imie, nazwisko, waga = 0.0, wzrost = 0.0):
        return cls(pesel, imie, nazwisko, waga, wzrost/100)

person1 = Person("05211111111", "Adrian", 'Nowak')
person2 = Person("06111111112", "Jan", 'Nowak', 89, 1.81)

print(person1.getInstances())
del person2
print(person1.getInstances())

print(person1.getWiek())
print(repr(person1))
person2 = eval(repr(person1))
print(person2.getWzrost())
person2.setWzrost(1.83)
print(person2.getWzrost())
