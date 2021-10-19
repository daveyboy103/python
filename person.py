from gender import Gender


class Person:
    def __init__(self, first_name, last_name, title, gender: Gender):
        self.__gender = gender
        self.__title = title
        self.__last_name = last_name
        self.__first_name = first_name
        self.__fired = False

    gender: Gender

    @property
    def first_name(self):
        return self.__first_name

    @property
    def last_name(self):
        return self.__last_name

    @property
    def title(self):
        return self.__title

    @property
    def gender(self):
        return self.__gender

    @property
    def fired(self):
        return self.__fired

    def tostring(self):
        return self.__title + " " + self.first_name + " " + self.__last_name + " " + str(self.__gender)

    def fire(self):
        self.__fired = True
        print("fired")

    def sex_change(self, new_gender: Gender, new_first_name, new_title=""):
        self.__gender = new_gender
        self.__first_name = new_first_name

        if len(new_title) == 0:
            if new_gender == Gender.Male:
                self.__title = "Mr"
            else:
                self.__title = "Ms"
        else:
            self.__title = new_title
