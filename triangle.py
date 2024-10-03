from math import hypot


class Point:
    def __init__(self, x=0.0, y=0.0):
        self.__x = x
        self.__y = y

    def getx(self):
        return self.__x

    def gety(self):
        return self.__y

    def distance_from_xy(self, x, y):
        return hypot(self.__x - x, self.__y - y)

    def distance_from_point(self, point):
        return hypot(self.__x - point.getx(), self.__y - point.gety())


class Triangle:
    def __init__(self, vertice1: Point, vertice2: Point, vertice3: Point):
        self.__vertice1 = vertice1
        self.__vertice2 = vertice2
        self.__vertice3 = vertice3

    def perimeter(self):
        return (self.__vertice1.distance_from_point(self.__vertice2) +
                self.__vertice2.distance_from_point(self.__vertice3) +
                self.__vertice3.distance_from_point(self.__vertice1))


triangle = Triangle(Point(0, 0), Point(1, 0), Point(0, 1))
print(triangle.perimeter())
