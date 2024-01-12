from typing import Union


class Glass:
    def __init__(self, capacity_volume: Union[int, float], occupied_volume: Union[int, float]):
        if not isinstance((capacity_volume),(int,float)):
            raise TypeError("Неправильный тип данных")
        if capacity_volume <= 0:
            raise TypeError("Объем не может быть отрицательным")
        if capacity_volume < occupied_volume:
            raise TypeError("Занятый объем не может быть больше вместимости")
        self.capacity_volume = capacity_volume
        self.occupied_volume = occupied_volume
        # теперь они стали атрибутами, до этого они были переменными
        #  TODO инициализировать объект "Стакан"


if __name__ == "__main__":
    glass_1 = Glass(200,100)
    glass_2 = Glass(300,300)
    ...  # TODO инициализировать два объекта типа Glass

    # TODO попробовать инициализировать не корректные объекты
