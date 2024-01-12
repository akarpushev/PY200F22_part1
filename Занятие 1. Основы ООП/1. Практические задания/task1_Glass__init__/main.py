from typing import Union


class Glass:
    def __init__(self, capacity_volume: Union[int, float], occupied_volume: Union[int, float]):
        if not isinstance((capacity_volume),(int,float)):
            raise TypeError("Неправильный тип данных")
        if capacity_volume <= 0:
            raise ValueError("Объем не может быть отрицательным")
        if not isinstance((occupied_volume),(int,float)):
            raise TypeError("Неправильный тип данных")
        if occupied_volume <= 0:
            raise ValueError("Объем не может быть отрицательным")
        if capacity_volume < occupied_volume:
            raise TypeError("Занятый объем не может быть больше вместимости")
        self.capacity_volume = capacity_volume
        self.occupied_volume = occupied_volume
        # теперь они стали атрибутами, до этого они были переменными
        #  TODO инициализировать объект "Стакан"


if __name__ == "__main__":
    glass_1 = Glass(200, 100)
    glass_2 = Glass(300, 300)
    glass_3 = Glass(500, 100)
    glass_1 = glass_1.occupied_volume + 100
    glass_2 = glass_2.occupied_volume - 100

    print(glass_3, glass_2)
    print(glass_1.capacity_volume, glass_1.occupied_volume)
    ...  # TODO инициализировать два объекта типа Glass

    # TODO попробовать инициализировать не корректные объекты
