from abc import ABC, abstractmethod

"""Загальні інтерфейси для светра та взуття"""

class AbstractSweater(ABC):
    def __init__(self, sweater: str):
        self._sweater = sweater

    def create(self):
        return self._sweater
    def __str__(self):
        return self.create()

class AbstractShose(ABC):
    def __init__(self, shose: str):
        self._shose = shose

    def create(self):
        return self._shose
    def __str__(self):
        return self.create()


"""Створюємо одяг Класичного стилю"""

class ClassicSweater(AbstractSweater):
    def __init__(self):
        self._sweater = "Classic Sweater"

    def create(self):
        return self._sweater


class ClassicShose(AbstractShose):
    def __init__(self):
        self._shose = "Classic Shose"


"""Одяг спортивного стилю """

class SportsSweater(AbstractSweater):
    def __init__(self):
        self._sweater = "Sports Sweater"


class SportsShose(AbstractShose):
    def __init__(self):
        self._shose = "Sports Shose"




"""Базовий клас абстрактної фабрики одягу"""
class AbstractFactory(ABC):
    def __init__(self, style):
        self.style = style

    @abstractmethod
    def get_sweater(self) -> AbstractSweater:  #створити светер
        pass

    @abstractmethod
    def get_shose(self) -> AbstractShose:    #створити взуття
        pass
    def __str__(self):
        return f'Ви замовляли одяг стилю {self.style}? ось вам {self. get_shose()}  та {self. get_sweater()} '

"""Конкретна фабрика класичного одягу"""

class ClassicFactory(AbstractFactory):

    def get_sweater(self) -> ClassicSweater:
        return ClassicSweater()

    def get_shose(self) -> ClassicShose:
        return ClassicShose()


"""Конкретна фабрика спортивного одягу"""

class SportsFactory(AbstractFactory):

    def get_sweater(self) -> SportsSweater:
        return SportsSweater()

    def get_shose(self) -> SportsShose:
        return SportsShose()


"""клієнтський код"""



def create_clothes(style: str):       #створюємо одяг

    factory_dict = {
        "Cl": ClassicFactory("Classic"),
        "Sp": SportsFactory("Sports")
        }
    return factory_dict[style]


if __name__ == '__main__':

    app = create_clothes('Cl')
    print(app)



"""Ми створили інтерфейси двох продуктів ( светер та взуття). 
Дальше реалізували інтерфес, для кожного продукту створили по одній моделі 
    спортивного продутку( спортивний светер та взуття) та по одній моделі класичного продукту( спортивний светер та взуття).
Дальше створили інтерфейс фабрики яка створюватиме нам екземпляри двох продуктів (сетер, взуття)  одинакового стилю.
Реалізували інтерфес, створили фабрики класичного та спортивного стилю.
Дальше клієнський код, якому ти задаєш одяг якого стилю хочеш отримати, він викликає фабрику конкретного стилю, яка повертає два продукти цього стилю"""