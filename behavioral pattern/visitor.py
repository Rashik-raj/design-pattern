class House:
    def accept(self,visitor):
        visitor.visit(self)

    def work_on_hvac(self, hvac_specialist):
        print(self,'worked on by', hvac_specialist)

    def work_on_electrician(self, electrician):
        print(self,'worked on by', electrician)

    def __str__(self):
        return self.__class__.__name__

class Visitor:
    def __str__(self):
        return self.__class__.__name__

class HvacSpecialist(Visitor):
    def visit(self, house):
        house.work_on_hvac(self)

class Electrician(Visitor):
    def visit(self, house):
        house.work_on_electrician(self)

v1 = HvacSpecialist()
v2 = Electrician()

h1 = House()
print(h1)
print(v1)
print(v2)

h1.accept(v1)
h1.accept(v2)
