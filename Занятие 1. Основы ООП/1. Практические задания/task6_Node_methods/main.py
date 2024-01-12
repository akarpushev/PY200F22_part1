from typing import Any, Optional


class Node:
    """ Класс, который описывает узел связного списка. """

    def __init__(self, value: Any, next_: Optional["Node"] = None):
        """
        Создаем новый узел для односвязного списка
        :param value: Любое значение, которое помещено в узел
        :param next_: следующий узел, если он есть
        """
        self.value = value
        self.next = next_
        # TODO добавить атрибуты

    def get_value(self) -> Any:
        """Метод, который возвращает значение атрибута value"""
        return self.value
        # TODO вернуть значение узла

    # TODO добавить метод get_next
    def get_next(self) -> Optional['Node']:
        return self.next




if __name__ == '__main__':
    second_node = Node(2) # второй узел
    first_node = Node(1, second_node)  # первый узел
    nul_node = Node(0, first_node)

    print(second_node.get_value())



    # TODO с помощью метода распечатать значение первого узла
    # TODO  с помощью метода распечатать следующий узел второго узла
