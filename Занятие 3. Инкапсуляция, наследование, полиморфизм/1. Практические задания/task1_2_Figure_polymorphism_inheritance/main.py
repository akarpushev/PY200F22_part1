import math


class Figure:
    """ Базовый класс. """

    def area(self):
        print(f"Вызван метод класса {self.__class__.__name__}")
        return None


class Rectangle(Figure):
    """ Производный класс. Прямоугольник. """

     # TODO определить конструктор и перегрузить метод area
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def area(self):
        super().area()
        return self.a * self.b

class Circle(Figure):
    """ Производный класс. Круг. """

     # TODO определить конструктор и перегрузить метод area
    def __init__(self, a):
        self.a = a

    def area(self):
        super().area()
        return math.pi * (self.a**2)


if __name__ == "__main__":
    fig = Figure()
    fig.area()


    rect = Rectangle(5, 10)
    rect.area()
    #print(rect.area())

    circle = Circle(5)
    circle.area()
    #print(circle.area())
