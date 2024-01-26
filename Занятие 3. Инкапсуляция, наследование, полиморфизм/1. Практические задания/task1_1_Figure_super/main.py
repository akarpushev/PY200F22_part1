class Figure: # базовый или родительский класс
    def __init__(self, name=None):
        self.name = name

    def print_name(self):
        print(self.name) # печатает атрибут экземпляра


class Rectangle(Figure):
    def __init__(self, a, b, name=None):
        # TODO вызвать конструктор базового класса с помощью super
        super().__init__(name)
        self.a = a
        self.b = b


if __name__ == "__main__":
    rect = Rectangle(5, 10, 'rect_fig')
    rect.print_name()
