class Parent:
    class_public_attr = "class_public_attr"
    class_protected_attr = "class_protected_attr"
    class__private_attr = "class_private_attr"


    def __init__(self, public_attr, protected_attr, private_attr):
        self.public_attr = public_attr
        self._protected_attr = protected_attr
        self.__private_attr = private_attr

    def public_method(self):
        print('public method')


    def _protected_method(self):
        print('protected_method')


    def __private_method(self):
        print('private mathod')


if __name__ == "__main__":
    # Write your solution here

    print(Parent(1, 2, 3)._protected_method())
    object = Parent(1, 2, 3)
    print(object._Parent__private_method())