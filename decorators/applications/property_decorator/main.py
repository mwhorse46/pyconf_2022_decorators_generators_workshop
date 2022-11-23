class Property(object):
    pass


class Abc(object):
    def __init__(self):
        self.__a = 1

    @Property
    def a(self):
        return self.__a

    @Property.setter
    def a(self, value):
        self.__a = value
