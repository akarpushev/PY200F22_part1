# TODO Написать 3 класса с документацией и аннотацией типов

import doctest
class Books:
    def __init__(self, total_pages: int, pages_read: int, lost_pages: int):
        """
        Создание и подготовка к работе объекта "book"
        :param total_pages: количество страниц в книге
        :param pages_read: количество прочитанных страниц
        :param lost_pages: количество потерянных страниц
        """
        self.total_pages = total_pages
        self.pages_read = pages_read
        self.lost_pages = lost_pages
        if not isinstance(total_pages, int):
            raise TypeError("Неправильный тип данных")
        if not isinstance(pages_read, int):
            raise TypeError("Неправильный тип данных")
        if not isinstance(lost_pages, int):
            raise TypeError("Неправильный тип данных")
        if total_pages <= 0:
            raise ValueError("Количество страниц должно быть положительное")
        if pages_read < 0:
            raise ValueError("Страниц не может быть отрицательное количество")
        if lost_pages < 0:
            raise ValueError("Страниц не может быть отрицательное количество")
        if pages_read > total_pages:
            raise ValueError("Столько страниц нельзя прочитать")
        if lost_pages > total_pages:
            raise ValueError("Столько страниц нельзя потерять")

    def book_reading(self, pages: int):
        """
        Чтение книги.
        :param pages: количество прочитанных страниц
        :raise ValueError: Если количество прочитанных страниц превышает количество страниц в книге,
        то вызываем ошибку
        :return: read_pages
        Примеры:
        >>> book = Books(500, 0, 0)
        >>> book.book_reading(200)
        """
        if pages < 0:
            raise ValueError("Страниц должно быть положительное количество")

    def loss_of_pages(self, pages: int):
        """
        Потеря страниц.
        :param pages: количество выпавших страниц
        :raise ValueError: Если количество выпавших страниц превышает количество страниц в книге,
        то вызываем ошибку
        :return: lost_pages
        Примеры:
        >>> book = Books(500, 10, 10)
        >>> book.loss_of_pages(200)
        """
        if pages < 0:
            raise ValueError("Страниц должно быть положительное количество")

class Plants:
    def __init__(self, total_leaves: int, yellowed_leaves: int, fallen_leaves: int):
        """
        Создание и подготовка к работе объекта "tree"
        :param total_leaves: количество листьев на дереве
        :param yellowed_leaves: количество пожелтевших листьев
        :param fallen_leaves: количество опавших страниц
        """
        self.total_pages = total_leaves
        self.yellowed_leaves = yellowed_leaves
        self.fallen_leavs = fallen_leaves
        if not isinstance(total_leaves, int):
            raise TypeError("Неправильный тип данных")
        if not isinstance(yellowed_leaves, int):
            raise TypeError("Неправильный тип данных")
        if not isinstance(fallen_leaves, int):
            raise TypeError("Неправильный тип данных")
        if total_leaves <= 0:
            raise ValueError("Количество листьев должно быть положительное")
        if yellowed_leaves < 0:
            raise ValueError("Листьев не может быть отрицательное количество")
        if fallen_leaves < 0:
            raise ValueError("Листьев должно быть положительное количество")
        if yellowed_leaves > total_leaves:
            raise ValueError("Столько листьев не может пожелтеть")
        if fallen_leaves > total_leaves:
            raise ValueError("Столько листьев не может опасть")

    def yellowing_leaves(self, leaves: int):
        """
        Пожелтение листьев.
        :param leaves: количество пожелтевших листьев
        :raise ValueError: Если количество пожелтевших листьев превышает количество листьев на дереве,
        то вызываем ошибку
        :return: yellowed_leaves

        Примеры:
        >>> tree = Plants(1500, 0, 0)
        >>> tree.yellowing_leaves(300)
        """
        if leaves < 0:
            raise ValueError("Листьев должно быть положительное количество")

    def leaf_fall(self, leaves: int):
        """
        Опадение листьев.
        :param leaves: количество опавших листьев
        :raise ValueError: Если количество опавших листьев превышает количество листьев на дереве,
        то вызываем ошибку
        :return: fallen_leaves
        Примеры:
        >>> tree = Plants(2500, 10, 10)
        >>> tree.leaf_fall(200)
        """
        if leaves < 0:
            raise ValueError("Листьев должно быть положительное количество")


class Animals:
    def __init__(self, species: str, weight: int, color: str):
        """
        Создание и подготовка к работе объекта "animal"
        :param species: название вида
        :param weight: вес животного
        :param color: окрас животного
        """
        self.species = species
        self.size = weight
        self.color = color
        if not isinstance(species, str):
            raise TypeError("Неправильный тип данных")
        if not isinstance(weight, int):
            raise TypeError("Неправильный тип данных")
        if not isinstance(color, str):
            raise TypeError("Неправильный тип данных")
        if weight <= 0:
            raise ValueError("Вес должен быть положительным")

    def weight_growth(self, kg: int):
        """
        Прирост веса.
        :param kg: прирост веса в кг
        :return: weight
        Примеры:
        >>> animal = Animals('dog', 10, 'black')
        >>> animal.weight_growth(3)
        """
        if kg < 0:
            raise ValueError("Вес не может быть отрицательным")

    def color_change(self, pigment: str):
        """
        Изменение окраса.
        :param pigment: цвет пигмента
        :return: color
        Примеры:
        >>> animal = Animals('cat', 4, 'grey')
        >>> animal.color_change('white')
        """

if __name__ == "__main__":
    doctest.testmod()
    # TODO работоспособность экземпляров класса проверить с помощью doctest
    pass
