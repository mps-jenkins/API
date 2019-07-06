import math
class Point:

    def __init__(self, initX, initY):
        self.x = initX
        self.y = initY

    def getX(self):
        return self.x

    def getY(self):
        return self.y

    def distancefromorigin(self):
        return ((self.x ** 2) + (self.y ** 2)) ** 0.5


def distance(point1, point2):
    xdiff = point1.getX() - point2.getX()
    ydiff = point1.getY() - point2.getY()

    dist = math.sqrt(xdiff ** 2 + ydiff ** 2)
    return dist


p1 = Point(5, 6)
p2 = Point(3 , 0)
print(distance(p1, p2))


