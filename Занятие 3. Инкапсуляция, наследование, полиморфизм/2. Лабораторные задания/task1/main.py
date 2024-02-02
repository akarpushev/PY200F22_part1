class Book:
    """ Базовый класс книги. """
    def __init__(self, name: str, author: str):
        self.name = name
        self.author = author

    def __str__(self):
        return f"Книга {self.name}. Автор {self.author}"

    def __repr__(self):
        return f"{self.__class__.__name__}(name={self.name!r}, author={self.author!r})"


class PaperBook(Book):
    def __init__(self, name: str, author: str, pages: int):
        super().__init__(name, author)
        self.__name = name
        self.__author = author
        self.pages = pages

    def __str__(self):
        return f"Книга {self.__name}. Автор {self.__author}"

    @property
    def pages(self):
        return self._pages

    @pages.setter
    def pages(self, value):
        if not isinstance(value, int):
            raise TypeError("Количество страниц должно быть типа int")
        if value <= 0:
            raise ValueError("Количество страниц должно быть положительным числом")
        self._pages = value


class AudioBook(Book):
    def __init__(self, name: str, author: str, duration: float):
        super().__init__(name, author)
        self.__name = name
        self.__author = author
        self.duration = duration

    def __str__(self):
        return f"Книга {self.__name}. Автор {self.__author}"

    @property
    def duration(self):
        return self._duration

    @duration.setter
    def duration(self, value):
        if not isinstance(value, int):
            raise TypeError("Длительность должна быть типа int")
        if value <= 0:
            raise ValueError("Длительность должна быть положительным числом")
        self._duration = value


# book = PaperBook('1', '5', 6)
# print(book)
# print([PaperBook('a', 's', i) for i in range(1, 5, 1)])
# book.name = 'aa'
# book.__name = 'aa'
# print(book)
# book.pages = 30
# print(book.pages)
