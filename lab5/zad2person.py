class Person:
    n = 0
    def __init__(self, pesel, name, surname, height=0, weight=0):
        self.pesel = pesel
        self.name = name
        self.surname = surname
        self.height = height
        self.height = weight
        self.birthDate = ("19"+pesel[0:2], pesel[2:4], pesel[4:6])
        Person.n += 1

    @staticmethod 
    def count():
        return f"number of people: {Person.n}"

    def __del__(self):
        Person.n -= 1

jack = Person('83112958101', "Jack", "Slim")

print(jack.birthDate)
print(Person.count())
