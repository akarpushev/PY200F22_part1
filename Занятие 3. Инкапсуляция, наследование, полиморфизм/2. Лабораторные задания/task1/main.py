class Book:
    """ Базовый класс книги. """
    def __init__(self, name: str, author: str):
        self.name = name
        self.author = author

    def __str__(self):
        return f"Книга {self.name}. Автор {self.author}"

    def __repr__(self):
        return f"{self.__class__.__name__}(name={self.name!r}, author={self.author!r})"


class PaperBook:
    def __init__(self, name: str, author: str, pages: int):
        super().__init__(name, author)
        self._name = name
        self._author = author
        self._pages = pages

    def __str__(self):
        return f"Книга {self._name}. Автор {self._author}"

    def is_valid(self, pages: int) -> None:
        if not isinstance(pages, int):
            raise TypeError

    @property
    def name(self):
        return self._name

    @property
    def author(self):
        return self._author

    @property
    def pages(self):
        return self._pages

    @pages.setter
    def pages(self, value):
        print('Вызван setter')
        self.is_valid(value)
        self._pages = value


class AudioBook:
    def __init__(self, name: str, author: str, duration: float):
        super().__init__(name, author)
        self._name = name
        self._author = author
        self.duration = duration

    def __str__(self):
        return f"Книга {self._name}. Автор {self._author}"

    def is_valid(self, duration: float) -> None:
        if not isinstance(duration, float):
            raise TypeError

    @property
    def name(self):
        return self._name

    @property
    def author(self):
        return self._author
