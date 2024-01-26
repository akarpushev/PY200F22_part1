class Calculator:

    # def calc(self, *args):
    #     self.add(*args)
    #     self.mul(*args)


    # TODO написать статические методы
    @staticmethod
    def add(self, a, b):  # TODO сделать статическим методом
        result = a + b
        return result

    @staticmethod
    def mul(self, a, b):  # TODO сделать статическим методом

        return a * b


if __name__ == "__main__":
    print(Calculator.add(5, 6))  # 11
    print(Calculator.mul(5, 6))  # 30
