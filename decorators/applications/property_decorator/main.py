class Property(object):
    def __init__(self, getter) -> None:
        self.getter = getter
        self.setter_ = None

    def setter(self, func):
        self.setter_ = func
        return self

    def __get__(self, instance, cls):
        return self.getter(instance)

    def __set__(self, instance, value):
        return self.setter_(instance, value)


class Abc(object):
    def __init__(self):
        self.__a = 1

    @Property
    def a(self):
        return self.__a

    @a.setter
    def a(self, value):
        self.__a = value


instance = Abc()
print(instance.a)
instance.a = 2
print(instance.a)

# instance.a -> instance.__dict__['a'].__get__(instance, Property)
