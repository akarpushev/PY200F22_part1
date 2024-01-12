# TODO Написать 3 класса с документацией и аннотацией типов
class Books:
    def __init__(self, total_pages: int, pages_nave_read: int, missing_pages: int):
        if not isinstance(total_pages, int):
            raise TypeError("Неправильный тип данных")
        if not isinstance(pages_nave_read, int):
            raise TypeError("Неправильный тип данных")
        if not isinstance(missing_pages, int):
            raise TypeError("Неправильный тип данных")
        if total_pages <= 0:
            raise ValueError("Страниц должно быть положительное количество")
        if pages_nave_read < 0:
            raise ValueError("Страниц должно быть положительное количество")
        if missing_pages < 0:
            raise ValueError("Страниц должно быть положительное количество")
        if pages_nave_read > total_pages:
            raise ValueError("Столько страниц нельзя потерять")
        if missing_pages > total_pages:
            raise ValueError("Столько страниц нельзя потерять")
        self.total_pages = total_pages
        self.pages_nave_read = None
        self.missing_pages = None
    def book_reading(self, pages: int):
        """
        Чтение книги.
        :param pages: количество прочитанных страниц
        :raise ValueError: Если количество прочитанных страниц превышает количество страниц в книге,
        то вызываем ошибку
        Примеры:
        >>> book = Books(500)
        >>> book.book_reading(self, 200)
        """
        if pages < 0:
            raise ValueError("Страниц должно быть положительное количество")


    def page_missing(self, pages: int):
        """
        Выпадение страниц.
        :param pages: количество выпавших страниц
        :raise ValueError: Если количество выпавших страниц превышает количество страниц в книге,
        то вызываем ошибку
        Примеры:
        >>> book = Books(500)
        >>> book.page_missing(self, 200)
        """
        if pages < 0:
            raise ValueError("Страниц должно быть положительное количество")







# class Plants:
#
#
# class Animals:


if __name__ == "__main__":

    book_1 = Books(500)
    print(book_1.total_pages)
    # TODO работоспособность экземпляров класса проверить с помощью doctest
    pass
