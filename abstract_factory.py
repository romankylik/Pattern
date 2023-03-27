from abc import ABC, abstractmethod

"""Загальні інтерфейси для продуктів """
class AbstractPants(ABC):
    def __init__(self, pants: str):
        self._pants = pants
    @abstractmethod
    def create(self): pass

class AbstractSweater(ABC):
    def __init__(self, sweater: str):
        self._sweater = sweater
    @abstractmethod
    def create(self): pass

class AbstractShose(ABC):
    def __init__(self, shose: str):
        self._shose = shose
    @abstractmethod
    def create(self): pass


"""Одяг класичного стилю """


class ClassicPants(ABC):
    def __init__(self):
        self._pants = "Classic Pants"


    def create(self):
        print(f'Створено {self._pants}')


class ClassicSweater(ABC):
    def __init__(self):
        self._sweater = "Classic Sweater"

    def create(self):
        print(f'Створено {self._sweater}')

class ClassicShose(ABC):
    def __init__(self):
        self._shose = "Classic Shose"
    def create(self):
        print(f'Створено {self._shose}')


"""Одяг спортивного стилю """


class SportsPants(ABC):
    def __init__(self):
        self._pants = "Sports Pants"


    def create(self):
        print(f'Створено {self._pants}')


class SportsSweater(ABC):
    def __init__(self):
        self._sweater = "Sports Sweater"

    def create(self):
        print(f'Створено {self._sweater}')

class SportsShose(ABC):
    def __init__(self):
        self._shose = "Sports Shose"
    def create(self):
        print(f'Створено {self._shose}')



"""Базовий клас абстрактної фабрики одягу"""
class AbstractFactory(ABC):

    @abstractmethod
    def get_pants(self) -> AbstractPants:  #створити штани
        pass

    @abstractmethod
    def get_sweater(self) -> AbstractSweater:  #створити светер
        pass

    @abstractmethod
    def get_shose(self) -> AbstractShose:    #створити взуття
        pass

"""Конкретна фабрика класичного одягу"""

class ClassicFactory(AbstractFactory):
    def get_pants(self) -> ClassicPants:
        return ClassicPants()

    def get_sweater(self) -> ClassicSweater:
        return ClassicSweater()

    def get_shose(self) -> ClassicShose:
        return ClassicShose()


"""Конкретна фабрика спортивного одягу"""

class SportsFactory(AbstractFactory):
    def get_pants(self) -> SportsPants:
        return SportsPants()

    def get_sweater(self) -> SportsSweater:
        return SportsSweater()

    def get_shose(self) -> SportsShose:
        return SportsShose()


"""Клієнтський клас створення одягу"""
class Application:
    @staticmethod
    def select_factory(style_name: str) -> AbstractFactory:
        factory_dict = {
            "Classic": ClassicFactory,
            "Sports": SportsFactory
        }
        return factory_dict[style_name]()


    def create_clothes(self, style: str):       #створюємо одяг
        sweater = self.select_factory(style).get_sweater()
        pants = self.select_factory(style).get_pants()
        shose = self.select_factory(style).get_shose()
        sweater.create()
        pants.create()
        shose.create()




if __name__ == '__main__':

    app = Application()
    app.create_clothes("Classic")
    app.create_clothes("Sports")