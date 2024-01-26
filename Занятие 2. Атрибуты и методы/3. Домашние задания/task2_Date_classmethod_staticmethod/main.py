class Date:
    """Класс для работы с датами"""
    DAY_OF_MONTH = (
        (31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31),  # обычный год
        (31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31)  # високосный
    )

    def __init__(self, day: int, month: int, year: int):
        self.day = day
        self.month = month
        self.year = year

        self.is_valid_date(self.day, self.month, self.year)

    def is_leap_year(self, year: int):
        """Проверяет, является ли год високосным"""
        # TODO реализовать метод
        if year % 4 == 0:
            result = 2
        elif year % 100 == 0:
            if year % 400 == 0:
                result = 2
        else:
            result = 1
            return result


    def get_max_day(self, month: int, year: int):
        """Возвращает максимальное количество дней в месяце для указанного года"""
        # TODO используя атрибут класса DAY_OF_MONTH вернуть количество дней в запрашиваемом месяце и году
        days = Date.DAY_OF_MONTH[self.is_leap_year(year)][month]
        return days

    def is_valid_date(self, day: int, month: int, year: int):
        """Проверяет, является ли дата корректной"""
        # TODO проверить валидность даты
        if not 0 < day < self.get_max_day(month, year):
            raise ValueError


if __name__ == "__main__":
    print(Date.is_valid_date(5, 6, 2024))  #

