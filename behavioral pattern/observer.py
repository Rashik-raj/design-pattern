"""
Maintains one-to-many relationship.
Notifies other objects when there is change in one.
"""

class Subject:
    def __init__(self):
        self._observers = []

    def attach(self,observer):
        if observer not in self._observers:
            self._observers.append(observer)

    def dettach(self,observer):
        try:
            self._observers.remove(observer)
        except:
            pass

    def notify(self,modifier=None):
        for observer in self._observers:
            if modifier != observer:
                observer.update(self)

class Core(Subject):
    def __init__(self,name=""):
        Subject.__init__(self)
        self._name = name
        self._temp = 0
    
    @property #getter method
    def temp(self):
        return self._temp

    @temp.setter #setter method
    def temp(self,temp):
        self._temp = temp
        self.notify()

class TempViewer:
    def update(self,subject):
        print('Temperature Viewer: {} has temperature {}'.format(subject._name,subject._temp))

c1 = Core('core1')
c2 = Core('core2')

v1 = TempViewer()
v2 = TempViewer()

c1.attach(v1)
c1.attach(v2)

c1.temp = 80
c1.temp = 90