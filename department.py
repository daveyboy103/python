from person import Person


class Department:
    def __init__(self, name, manager: Person):
        self.__name__ = name
        self.__manager__ = manager

    @property
    def name(self):
        return self.__name__

    @property
    def manager(self):
        return  self.__manager__

