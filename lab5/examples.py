class Shape:
    index = 0
    def __init__(self, setVar1, setVar2):
        self.var1 = setVar1
        self.var2 = setVar2
        Shape.index += 1

    def display(self):
        print(self.var1," ",self.var2)

    @staticmethod 
    def count():
        return f"number of objects class Shape: {Shape.index}"

    @classmethod
    def createFromList(cls, List=[0, 0]):
        return cls(List[0], List[1])

    def __str__(self):
        return f""


newShape = Shape(3,5)
newShape.display()
print(newShape.count())

listShape = Shape.createFromList([5,6])

