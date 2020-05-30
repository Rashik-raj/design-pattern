class DrawingAPIOne:
    def draw_circle(self,x,y,radius):
        print("API 1 drawing circle at ({},{} with radius {})".format(x,y,radius))

class DrawingAPITwo:
    def draw_circle(self,x,y,radius):
        print("API 2 drawing circle at ({},{} with radius {})".format(x,y,radius))

class Circle:
    def __init__(self,x,y,radius,drawing_api):
        self._x = x
        self._y = y
        self._radius = radius
        self._api = drawing_api

    def draw(self):
        self._api.draw_circle(self._x,self._y,self._radius)

    def scale(self, percentage):
        self._radius *= percentage

circle1 = Circle(5,1,15,DrawingAPIOne())
circle2 = Circle(5,1,15,DrawingAPITwo())
circle1.draw()
circle2.draw()